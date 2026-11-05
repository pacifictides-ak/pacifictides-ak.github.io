#!/usr/bin/env python3
"""Generate a static town tide page from NOAA CO-OPS predictions.

Usage:
  python3 generate_tide_page.py --station 9451439 --slug petersburg --name "Petersburg, AK"
  python3 generate_tide_page.py --station 9452210 --slug juneau --name "Juneau, AK" --days 7
  python3 generate_tide_page.py --station 9455920 --slug anchorage --name "Anchorage, AK" --dry-run

Fetches high/low predictions from the NOAA CO-OPS API and writes:
  pages/<slug>-tides.html
  Updates pages.json in the site root.

Never invents tide heights or times — all values come from NOAA.
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.parse
import urllib.request
from datetime import date, datetime, timedelta
from pathlib import Path

from directory_snippets import (
    affiliate_html,
    ads_placeholder_html,
    directory_html,
    local_news_html,
    footer_html,
    nav_html,
    signup_html,
    sponsor_html,
)

SITE_ROOT = Path(__file__).resolve().parent.parent
PAGES_DIR = SITE_ROOT / "pages"
MANIFEST = SITE_ROOT / "pages.json"
API = "https://api.tidesandcurrents.noaa.gov/api/prod/datagetter"
NOAA_PRED = "https://tidesandcurrents.noaa.gov/noaatidepredictions.html"
NOAA_STATION = "https://tidesandcurrents.noaa.gov/stationhome.html"


def fetch_predictions(station: str, begin: date, end: date) -> list[dict]:
    params = {
        "product": "predictions",
        "application": "pacific-tides",
        "begin_date": begin.strftime("%Y%m%d"),
        "end_date": end.strftime("%Y%m%d"),
        "datum": "MLLW",
        "station": station,
        "time_zone": "lst_ldt",
        "units": "english",
        "interval": "hilo",
        "format": "json",
    }
    url = API + "?" + urllib.parse.urlencode(params)
    with urllib.request.urlopen(url, timeout=30) as resp:
        raw = resp.read().decode("utf-8")
    data = json.loads(raw)
    if "error" in data:
        raise RuntimeError(f"NOAA API error: {data['error']}")
    preds = data.get("predictions")
    if not preds:
        raise RuntimeError(f"No predictions returned for station {station}")
    return preds


def fetch_station_meta(station: str) -> dict:
    url = f"https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/{station}.json"
    try:
        with urllib.request.urlopen(url, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        stations = data.get("stations") or []
        return stations[0] if stations else {}
    except Exception as exc:  # noqa: BLE001
        print(f"warning: could not fetch station meta: {exc}", file=sys.stderr)
        return {}


def fmt_height(v: str) -> str:
    try:
        return f"{float(v):.1f}"
    except ValueError:
        return v


def fmt_time(t: str) -> tuple[str, str]:
    """Return (date_label, time_label) from NOAA 'YYYY-MM-DD HH:MM'."""
    dt = datetime.strptime(t, "%Y-%m-%d %H:%M")
    return dt.strftime("%a %b %-d, %Y"), dt.strftime("%-I:%M %p")


def group_by_day(preds: list[dict]) -> list[tuple[str, list[dict]]]:
    days: dict[str, list[dict]] = {}
    order: list[str] = []
    for p in preds:
        day = p["t"][:10]
        if day not in days:
            days[day] = []
            order.append(day)
        days[day].append(p)
    result = []
    for day in order:
        label = datetime.strptime(day, "%Y-%m-%d").strftime("%A, %B %-d, %Y")
        result.append((label, days[day]))
    return result


def render_page(
    *,
    name: str,
    slug: str,
    station: str,
    preds: list[dict],
    meta: dict,
    begin: date,
    end: date,
    fetched_at: datetime,
) -> str:
    lat = meta.get("lat")
    lng = meta.get("lng")
    coord = ""
    if lat is not None and lng is not None:
        coord = f"{lat}, {lng}"

    rows = []
    for day_label, day_preds in group_by_day(preds):
        cells = []
        for p in day_preds:
            _, tlabel = fmt_time(p["t"])
            kind = "High" if p["type"] == "H" else "Low"
            height = fmt_height(p["v"])
            cells.append(
                f'<tr><td>{kind}</td><td>{tlabel}</td><td>{height} ft</td></tr>'
            )
        rows.append(
            f"<h2>{day_label}</h2>\n"
            f'<table class="tides">\n'
            f"<thead><tr><th>Tide</th><th>Time (local)</th><th>Height (MLLW)</th></tr></thead>\n"
            f"<tbody>\n{chr(10).join(cells)}\n</tbody>\n</table>"
        )

    table_html = "\n".join(rows)
    pred_url = f"{NOAA_PRED}?id={station}"
    station_url = f"{NOAA_STATION}?id={station}"
    api_note = (
        f"Fetched {fetched_at.strftime('%Y-%m-%d %H:%M %Z')} from NOAA CO-OPS "
        f"datagetter (product=predictions, interval=hilo, datum=MLLW, "
        f"time_zone=lst_ldt, units=english) for station {station}, "
        f"{begin.isoformat()} through {end.isoformat()}."
    )

    windy = ""
    if lat is not None and lng is not None:
        windy = f'      <a class="btn btn-ghost" href="https://www.windy.com/{lat}/{lng}" rel="noopener">View on Windy</a>\n'
    print_link = f'      <a class="btn btn-ghost" href="../print/{slug}-tide-calendar.html">Printable tide calendar</a>\n'

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{name} Tide Predictions | Pacific Tides</title>
  <meta name="description" content="High and low tide predictions for {name} from NOAA CO-OPS station {station}, plus local marine and shore directory.">
  <link rel="stylesheet" href="../style.css">
</head>
<body>
{nav_html("../")}
  <main class="wrap">
    <p class="crumb"><a href="../index.html">Directory</a> / {name}</p>
    <h1>{name} tide predictions</h1>
    <p class="lede">
      High and low tides for the coming week from NOAA station
      <strong>{station}</strong>
      {"(" + coord + ")" if coord else ""}.
      Times are local (LST/LDT). Heights are feet above Mean Lower Low Water (MLLW).
    </p>

    <p class="actions">
      <a class="btn" href="{pred_url}" rel="noopener">Official NOAA predictions</a>
      <a class="btn btn-ghost" href="{station_url}" rel="noopener">Station home</a>
{print_link}{windy}    </p>

    <aside class="notice">
      <strong>Not for navigation.</strong> Always verify with
      <a href="{pred_url}" rel="noopener">NOAA Tides &amp; Currents</a>
      before you work or play on the water.
    </aside>

{sponsor_html(name, "../")}

    <section class="tide-tables">
{table_html}
    </section>

    <section>
      <h2>Marine weather &amp; cameras</h2>
      <p class="actions">
        <a class="btn btn-ghost" href="https://marine.weather.gov/" rel="noopener">NWS Marine Weather</a>
        <a class="btn btn-ghost" href="https://www.ndbc.noaa.gov/" rel="noopener">NOAA buoys</a>
{windy if windy else "      "}      </p>
      <p style="color:var(--muted);font-size:0.92rem;">Harbor webcam links added when a free public camera is verified.</p>
    </section>

{directory_html(slug, "../")}
{local_news_html(slug, name)}
{signup_html(name, "../")}
{affiliate_html()}
{ads_placeholder_html()}

    <section class="sources">
      <h2>Sources</h2>
      <ul>
        <li>NOAA CO-OPS station <a href="{station_url}" rel="noopener">{station} — {name.split(",")[0]}</a></li>
        <li>Predictions API: <code>api.tidesandcurrents.noaa.gov/api/prod/datagetter</code></li>
        <li>{api_note}</li>
      </ul>
    </section>
  </main>
{footer_html("../")}
</body>
</html>
"""



def update_manifest(entry: dict) -> None:
    if MANIFEST.exists():
        manifest = json.loads(MANIFEST.read_text())
    else:
        manifest = {"site": "Pacific Tides", "pages": []}
    pages = [p for p in manifest.get("pages", []) if p.get("path") != entry["path"]]
    pages.append(entry)
    pages.sort(key=lambda p: p.get("date_added", ""), reverse=True)
    manifest["pages"] = pages
    MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--station", required=True, help="NOAA CO-OPS station id")
    parser.add_argument("--slug", required=True, help="URL slug, e.g. petersburg")
    parser.add_argument("--name", required=True, help='Display name, e.g. "Petersburg, AK"')
    parser.add_argument("--days", type=int, default=7, help="Days of predictions (default 7)")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Fetch and validate only; do not write HTML or update pages.json",
    )
    args = parser.parse_args()

    begin = date.today()
    end = begin + timedelta(days=args.days)
    print(f"Fetching {args.name} ({args.station}) {begin} → {end} …")
    preds = fetch_predictions(args.station, begin, end)
    meta = fetch_station_meta(args.station)
    fetched_at = datetime.now().astimezone()

    meta_name = meta.get("name") or "(no meta name)"
    print(
        f"OK station meta: {meta_name} | state={meta.get('state')} "
        f"| lat={meta.get('lat')} lng={meta.get('lng')} | preds={len(preds)}"
    )
    if preds:
        print(f"  first={preds[0]} last={preds[-1]}")

    if args.dry_run:
        # Still render to catch template errors, but do not write.
        html = render_page(
            name=args.name,
            slug=args.slug,
            station=args.station,
            preds=preds,
            meta=meta,
            begin=begin,
            end=end,
            fetched_at=fetched_at,
        )
        print(f"Dry-run: would write pages/{args.slug}-tides.html ({len(html)} bytes); no files changed.")
        return 0

    PAGES_DIR.mkdir(parents=True, exist_ok=True)
    out = PAGES_DIR / f"{args.slug}-tides.html"
    html = render_page(
        name=args.name,
        slug=args.slug,
        station=args.station,
        preds=preds,
        meta=meta,
        begin=begin,
        end=end,
        fetched_at=fetched_at,
    )
    out.write_text(html)
    print(f"Wrote {out} ({len(preds)} predictions)")

    update_manifest(
        {
            "title": f"{args.name} tide predictions",
            "path": f"pages/{args.slug}-tides.html",
            "date_added": begin.isoformat(),
            "station": args.station,
            "sources": [
                f"https://tidesandcurrents.noaa.gov/stationhome.html?id={args.station}",
                "https://api.tidesandcurrents.noaa.gov/api/prod/datagetter",
            ],
        }
    )
    print(f"Updated {MANIFEST}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
