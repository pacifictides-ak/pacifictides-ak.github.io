#!/usr/bin/env python3
"""Build/refresh pages/prince-william-sound-tides.html (Prince William Sound ports overview).
Pulls fresh NOAA CO-OPS hi/lo predictions for five PWS stations, NWS coastal zone text for
nine zones, and NDBC realtime obs. Directory rows come from data/businesses.csv (Valdez,
Whittier, Cordova). Never invents data. Throttled (1 s between requests, per-run cache)."""
import re, json, time, urllib.request, datetime, html, csv, sys
from pathlib import Path
from zoneinfo import ZoneInfo
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from directory_snippets import (nav_html, footer_html, signup_html, sponsor_html, affiliate_html,
                                ads_placeholder_html, CATEGORY_LABELS, MARINE_ORDER)
UA = {"User-Agent": "PacificTides (pacifictides.ak@gmail.com)"}
AK = ZoneInfo("America/Anchorage")
E = html.escape
URL = "https://pacifictides-ak.github.io/pages/prince-william-sound-tides.html"

STATIONS = [  # (key, NOAA id, label, page or None)
 ("whittier", "9454949", "Whittier (Passage Canal)", "whittier-tides.html"),
 ("valdez", "9454240", "Valdez (Port Valdez)", "valdez-tides.html"),
 ("cordova", "9454050", "Cordova (Orca Inlet)", "cordova-tides.html"),
 ("tatitlek", "9454374", "Busby Island (near Tatitlek)", None),
 ("chenega", "9454764", "Sawmill Bay, Evans Island (near Chenega Bay)", None),
]
ZONES = [  # west -> east, inside -> outside
 ("pkz723", "Whittier"), ("pkz724", "Whittier / NW Sound"), ("pkz726", "Chenega Bay / SW Sound"),
 ("pkz720", "Valdez"), ("pkz721", "Valdez"), ("pkz722", "Valdez / Tatitlek"),
 ("pkz725", "Cordova / central Sound"), ("pkz711", "Hinchinbrook Entrance (outside)"), ("pkz710", "Cordova / Copper River Delta (outside)"),
]
BUOYS = [
 ("WIXA2", "Whittier AMHS terminal (WIXA2)"), ("PPXA2", "Point Pigot (PPXA2)"),
 ("46081", "Western Prince William Sound buoy (46081)"), ("VDZA2", "Valdez (VDZA2, NOAA 9454240)"),
 ("46060", "West Orca Bay buoy (46060)"), ("46061", "Seal Rocks buoy (46061, Hinchinbrook Entrance)"),
 ("CRVA2", "Cordova (CRVA2, NOAA 9454050)"),
]
cache = {}
def get(url):
    if url in cache: return cache[url]
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r: cache[url] = r.read().decode("utf-8", "replace")
    time.sleep(1); return cache[url]
now = datetime.datetime.now(AK)
start = (now + datetime.timedelta(days=1)).date() if now.hour >= 18 else now.date()
fetched = now.strftime("%Y-%m-%d %H:%M AKST")
def preds(station, days):
    b = start.strftime("%Y%m%d"); e = (start + datetime.timedelta(days=days)).strftime("%Y%m%d")
    u = (f"https://api.tidesandcurrents.noaa.gov/api/prod/datagetter?product=predictions&application=PacificTides"
         f"&begin_date={b}&end_date={e}&datum=MLLW&station={station}&time_zone=lst_ldt&units=english&interval=hilo&format=json")
    return [(("High" if p["type"] == "H" else "Low"), datetime.datetime.strptime(p["t"], "%Y-%m-%d %H:%M"), float(p["v"]))
            for p in json.loads(get(u))["predictions"]]
def tstr(t): return t.strftime("%I:%M %p").lstrip("0")
def hstr(v): return f"{(0.0 if abs(v) < 0.05 else v):.1f}".replace("-", "&minus;") + "&nbsp;ft"
def forecast(zone):
    txt = get(f"https://tgftp.nws.noaa.gov/data/forecasts/marine/coastal/pk/{zone}.txt")
    ex = re.search(r"^Expires:(\d{12})", txt, re.M)
    if ex:
        exp = datetime.datetime.strptime(ex.group(1), "%Y%m%d%H%M").replace(tzinfo=datetime.timezone.utc)
        if exp < datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=2):
            raise RuntimeError(f"stale NWS product {zone}")
    m = re.search(rf"^{zone.upper()}-\d+-\n(.*?)\n\$\$", txt, re.S | re.M)
    blk = m.group(1).strip().split("\n")
    name = blk[0].rstrip("-"); issued = blk[1].strip(); body = "\n".join(blk[2:]).strip()
    heads = re.findall(r"^\.\.\.(.+?)\.\.\.$", body, re.M)
    per = [" ".join(p.split()) for p in re.findall(r"^(\.[A-Z][A-Z ]+\.\.\..*?)(?=^\.[A-Z]|\Z)", body, re.S | re.M)]
    if not per: raise RuntimeError("no periods " + zone)
    return name, issued, heads, per
def obs(st):
    try: txt = get(f"https://www.ndbc.noaa.gov/data/realtime2/{st}.txt")
    except Exception: return None
    rows = [l.split() for l in txt.splitlines() if not l.startswith("#")]
    if not rows: return None
    r = rows[0]
    t = datetime.datetime(int(r[0]), int(r[1]), int(r[2]), int(r[3]), int(r[4]), tzinfo=datetime.timezone.utc).astimezone(AK)
    parts = []
    if r[5] != "MM": parts.append(f"wind {r[5]}°")
    if r[6] != "MM": parts.append(f"{float(r[6])*1.94384:.0f} kt")
    if r[7] != "MM": parts.append(f"gust {float(r[7])*1.94384:.0f} kt")
    if r[8] != "MM": parts.append(f"seas {float(r[8])*3.28084:.1f} ft")
    if r[13] != "MM": parts.append(f"air {float(r[13])*9/5+32:.0f}°F")
    if r[12] != "MM": parts.append(f"{r[12]} hPa")
    if len(r) > 14 and r[14] != "MM": parts.append(f"water {float(r[14])*9/5+32:.0f}°F")
    return (", ".join(parts), t) if parts else None

# ---------- data ----------
week = {k: preds(sid, 7) for k, sid, _, _ in STATIONS}
long = {k: preds(sid, 35) for k, sid, _, p in STATIONS if p}
# timing spread between the three town stations for matching events in the 8-day window
spreads = []
for i, (kind, t, v) in enumerate(week["valdez"]):
    others = []
    for k in ("whittier", "cordova", "tatitlek", "chenega"):
        c = min(week[k], key=lambda x: abs((x[1] - t).total_seconds()))
        if c[0] == kind and abs((c[1] - t).total_seconds()) < 3 * 3600: others.append(c[1])
    ts = [t] + others
    spreads.append((max(ts) - min(ts)).total_seconds() / 60)
max_spread = int(round(max(spreads)))
# biggest high->low drop in 5 weeks, per town
def biggest(ev):
    best = None
    for a, b in zip(ev, ev[1:]):
        if a[0] == "High" and b[0] == "Low":
            d = a[2] - b[2]
            if not best or d > best[0]: best = (d, a, b)
    return best
big = {k: biggest(v) for k, v in long.items()}
bk = max(big, key=lambda k: big[k][0])
bd, ba, bb = big[bk]
minus_days = sorted({t.date() for k in long for (kind, t, v) in long[k] if kind == "Low" and v < 0})
fc = {z: forecast(z) for z, _ in ZONES}
ob = {b: obs(b) for b, _ in BUOYS}
warn = [(z, fc[z][0], fc[z][2]) for z, _ in ZONES if fc[z][2]]

# directory rows
rows = [r for r in csv.DictReader(open(ROOT / "data" / "businesses.csv")) if r["port_slug"] in ("whittier", "valdez", "cordova")]
TOWN = {"whittier": "Whittier", "valdez": "Valdez", "cordova": "Cordova"}
DIR_CATS = MARINE_ORDER + ["airport_floatplane"]
def listing(it):
    meta = [f'<strong>{TOWN[it["port_slug"]]}</strong>']
    if it.get("phone"): meta.append(f'<a href="tel:{E(it["phone"].replace("-", ""))}">{E(it["phone"])}</a>')
    if it.get("email"): meta.append(f'<a href="mailto:{E(it["email"])}">{E(it["email"])}</a>')
    if it.get("website"): meta.append(f'<a href="{E(it["website"])}" rel="noopener">Website</a>')
    if it.get("address"): meta.append(E(it["address"]))
    cls = "listing featured" if it.get("featured") == "yes" else "listing"
    return f'      <div class="{cls}"><div class="name">{E(it["name"])}</div><div class="meta">{" · ".join(meta)}</div></div>'
dir_out, dir_count = [], 0
order = {"whittier": 0, "valdez": 1, "cordova": 2}
for cat in DIR_CATS:
    items = sorted([r for r in rows if r["category"] == cat], key=lambda x: (0 if x.get("featured") == "yes" else 1, order[x["port_slug"]], x["name"].lower()))
    label = "Getting there: ferry, rail, air & water taxi" if cat == "airport_floatplane" else CATEGORY_LABELS[cat]
    dir_out.append(f'      <h4 class="dir-cat" style="font-size:0.95rem;margin-top:0.7rem;">{E(label)}</h4>')
    if not items:
        dir_out.append('      <p class="dir-empty">No verified listing yet in the three Sound towns — <a href="../advertise.html#list-free">list your business free</a>.</p>'); continue
    for it in items: dir_out.append(listing(it)); dir_count += 1
n_proc = sum(1 for r in rows if r["category"] == "seafood_processors")
proc_by = {k: sum(1 for r in rows if r["category"] == "seafood_processors" and r["port_slug"] == k) for k in TOWN}

# ---------- html pieces ----------
def day_tables():
    out = ['<section class="tide-tables">']
    days = sorted({t.date() for k in week for (_, t, _) in week[k]})[:8]
    for d in days:
        out.append(f"<h2>{d.strftime('%A, %B')} {d.day}, {d.year}</h2>")
        out.append('<div style="overflow-x:auto;"><table class="tides">\n<thead><tr><th>Station</th><th>Tides (local time, height above MLLW)</th></tr></thead>\n<tbody>')
        for k, sid, label, page in STATIONS:
            ev = [f"{'H' if kind == 'High' else 'L'} {tstr(t)} {hstr(v)}" for kind, t, v in week[k] if t.date() == d]
            name = f'<a href="{page}">{E(label)}</a>' if page else E(label)
            out.append(f"<tr><td>{name}<br><span style=\"color:var(--muted);font-size:0.85rem;\">NOAA {sid}</span></td><td>{' · '.join(ev)}</td></tr>")
        out.append("</tbody>\n</table></div>")
    out.append("    </section>")
    return "\n".join(out)
def weather():
    out = []
    for z, area in ZONES:
        name, issued, heads, per = fc[z]; Z = z.upper()
        out += [f'      <h3>NWS marine forecast — {E(name)} ({Z})</h3>',
                f'      <p style="color:var(--muted);font-size:0.92rem;">For {E(area)}. Issued {E(issued)}. Snapshot fetched {fetched} from NWS text product. <a href="https://marine.weather.gov/MapClick.php?zoneid={Z}&amp;TextType=1" rel="noopener">Official zone forecast</a> · <a href="https://tgftp.nws.noaa.gov/data/forecasts/marine/coastal/pk/{z}.txt" rel="noopener">Raw text</a></p>']
        for h in heads: out.append(f"<p><strong>...{E(h)}...</strong></p>")
        out.append('      <ul class="forecast-periods">')
        for p in per[:4]: out.append(f"        <li>{E(p)}</li>")
        out.append("      </ul>")
    for b, label in BUOYS:
        out.append(f"      <h3>Nearby NDBC observation — {label}</h3>")
        o = ob[b]
        if o:
            out.append(f"      <p><strong>{o[0]}</strong></p>")
            out.append(f'      <p style="color:var(--muted);font-size:0.92rem;">Observation time {o[1].strftime("%Y-%m-%d %H:%M")} AKST (converted to AKST). Attribution: NOAA NDBC station <a href="https://www.ndbc.noaa.gov/station_page.php?station={b}" rel="noopener">{b}</a>. Snapshot fetched {fetched}.</p>')
        else:
            out.append(f'      <p style="color:var(--muted);font-size:0.92rem;">Live values not cached on this page (realtime file unavailable at fetch {fetched}). Check NOAA NDBC <a href="https://www.ndbc.noaa.gov/station_page.php?station={b}" rel="noopener">{b}</a>.</p>')
    return "\n".join(out)

warn_txt = ""
if warn:
    groups = {}
    for z, n, h in warn: groups.setdefault(" / ".join(h).title(), []).append(z.upper())
    calm = [z.upper() for z, _ in ZONES if not fc[z][2]]
    w = "; ".join(f"<strong>{E(h)}</strong> for {', '.join(zs)}" for h, zs in groups.items())
    warn_txt = f" In the forecast issued {E(fc['pkz725'][1])}: {w}" + (f"; no headline for {', '.join(calm)}." if calm else ".")
# first upcoming low for each town to show the synchrony
def first_low(k):
    return next((t, v) for kind, t, v in week[k] if kind == "Low" and t > now.replace(tzinfo=None))
fl = {k: first_low(k) for k in ("whittier", "valdez", "cordova")}
title = "Prince William Sound Tides &amp; Ports — Whittier, Valdez, Cordova (NOAA stations, marine zones, harbors) | Pacific Tides"
desc = ("Free Prince William Sound tide tables for Whittier, Valdez, Cordova, Busby Island (Tatitlek) and Sawmill Bay (Chenega Bay) from NOAA, "
        "all nine NWS marine zones from Passage Canal to Hinchinbrook Entrance, buoy obs, harbor/harbormaster contacts, fuel, haul-outs, and seafood processors.")
ld = {"@context": "https://schema.org", "@graph": [
  {"@type": "WebPage", "@id": URL + "#webpage", "url": URL, "name": html.unescape(title), "description": desc,
   "isPartOf": {"@id": "https://pacifictides-ak.github.io/#website"}, "about": {"@id": URL + "#dataset"}},
  {"@type": "BreadcrumbList", "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://pacifictides-ak.github.io/"},
    {"@type": "ListItem", "position": 2, "name": "Prince William Sound tides & ports", "item": URL}]},
  {"@type": "Dataset", "@id": URL + "#dataset", "name": "Prince William Sound tide predictions (NOAA 9454949, 9454240, 9454050, 9454374, 9454764)",
   "description": "High and low tide predictions for five NOAA CO-OPS stations in Prince William Sound, Alaska. Informational only; not for navigation.",
   "creator": {"@type": "Organization", "name": "NOAA Center for Operational Oceanographic Products and Services (CO-OPS)"},
   "license": "https://www.commerce.gov/page/license-noaa-data", "url": URL,
   "isBasedOn": "https://api.tidesandcurrents.noaa.gov/api/prod/datagetter",
   "spatialCoverage": {"@type": "Place", "name": "Prince William Sound, Alaska", "geo": {"@type": "GeoCoordinates", "latitude": 60.75, "longitude": -147.0}}}]}

def row(cells): return "<tr>" + "".join(f"<td>{c}</td>" for c in cells) + "</tr>"
compare = "\n".join([
 row(['<a href="whittier-tides.html"><strong>Whittier</strong></a>', 'NOAA <a href="https://tidesandcurrents.noaa.gov/stationhome.html?id=9454949" rel="noopener">9454949</a> Passage Canal', 'PKZ723 Passage Canal · PKZ724 NW Sound · PKZ726 SW Sound', 'WIXA2 · PPXA2 · 46081',
      'City of Whittier Harbor <a href="tel:9074722327">907-472-2327</a>; VHF 16/68 (Pilothouse Guide); 360 slips to 60&nbsp;ft; Cliffside Marina (private, 99 slips)',
      'Shoreside Petroleum harbor fuel dock', 'No published travelift; Cliffside Marina hydraulic trailer haul', f'{proc_by["whittier"]}',
      'Road &amp; rail through the one-lane <a href="https://dot.alaska.gov/creg/whittiertunnel/" rel="noopener">Anton Anderson Memorial Tunnel</a> (scheduled openings); AMHS ferry']),
 row(['<a href="valdez-tides.html"><strong>Valdez</strong></a>', 'NOAA <a href="https://tidesandcurrents.noaa.gov/stationhome.html?id=9454240" rel="noopener">9454240</a> Port Valdez', 'PKZ720 Port of Valdez · PKZ721 Valdez Narrows · PKZ722 Valdez Arm', 'VDZA2 · 46060 · 46061',
      'City of Valdez Harbors <a href="tel:9078354981">907-835-4981</a>; hail VHF 16, work Ch 7; North Basin 489 + South Basin 127 slips',
      'Crowley Fuels, North &amp; South harbor docks', '<a href="https://www.valdezak.gov/258/Boat-Yard" rel="noopener">City boat yard</a>: 75-ton travelift + tidal grid (to 120&nbsp;ft / 250&nbsp;GT)', f'{proc_by["valdez"]}',
      'Richardson Highway (year-round road); AMHS ferry; Valdez airport']),
 row(['<a href="cordova-tides.html"><strong>Cordova</strong></a>', 'NOAA <a href="https://tidesandcurrents.noaa.gov/stationhome.html?id=9454050" rel="noopener">9454050</a> Orca Inlet', 'PKZ725 Central &amp; Eastern Sound · PKZ710 Cape Suckling–Gravel Pt (outside)', 'CRVA2 · 46060 · 46061',
      'City of Cordova Harbor <a href="tel:9074246400">907-424-6400</a>; VHF 16, work Ch 68; office 7 days 8&ndash;5',
      'Shoreside Petroleum commercial fuel dock', '<a href="https://www.cityofcordova.net/150-ton-travel-lift-and-shipyard/" rel="noopener">City 150-ton travel lift</a> + 160&nbsp;ft and 180&nbsp;ft tidal grids', f'{proc_by["cordova"]}',
      'No road to the rest of Alaska: AMHS ferry or air (CDV)']),
 row(['Tatitlek', 'NOAA <a href="https://tidesandcurrents.noaa.gov/stationhome.html?id=9454374" rel="noopener">9454374</a> Busby Island (6.7&nbsp;km)', 'PKZ722 Valdez Arm (Tatitlek Narrows)', 'VDZA2 · 46060', 'Small state/community harbor (Alaska DOT&amp;PF harbor list); no Pacific Tides page yet', '&mdash;', '&mdash;', '&mdash;', 'Boat or air only']),
 row(['Chenega Bay', 'NOAA <a href="https://tidesandcurrents.noaa.gov/stationhome.html?id=9454764" rel="noopener">9454764</a> Sawmill Bay, Evans Island (3.4&nbsp;km; subordinate to Cordova)', 'PKZ726 Southwest Prince William Sound', '46081 · PPXA2', 'Small state/community harbor (Alaska DOT&amp;PF harbor list); no Pacific Tides page yet', '&mdash;', '&mdash;', '&mdash;', 'Boat or air only']),
])

lows_line = " · ".join(f"{TOWN[k]} {tstr(t)} ({hstr(v)})" for k, (t, v) in fl.items())
md = minus_days
minus_txt = (f"Minus lows fall on {len(md)} days between {md[0].strftime('%b')} {md[0].day} and {md[-1].strftime('%b')} {md[-1].day}" if md else "No minus lows in the window")

page = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{E(desc)}" />
  <link rel="canonical" href="{URL}" />
  <meta property="og:type" content="article" />
  <meta property="og:site_name" content="Pacific Tides" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{E(desc)}" />
  <meta property="og:url" content="{URL}" />
  <meta property="og:image" content="https://pacifictides-ak.github.io/assets/ports/prince-william-sound/pws-seiner-2007-cart5819-web.jpg" />
  <meta name="twitter:card" content="summary_large_image" />
  <script type="application/ld+json">
{json.dumps(ld, indent=2, ensure_ascii=False)}
  </script>
  <link rel="stylesheet" href="../style.css">
</head>
<body class="port port-pws">
{nav_html("../")}
  <main class="wrap">
    <p class="crumb"><a href="../index.html">Directory</a> / Southcentral Alaska / Prince William Sound</p>
    <div class="pws-mast" role="img" aria-label="Stylized Prince William Sound: Chugach peaks and a tidewater glacier above island-dotted water, a purse seiner and a ferry running between Whittier, Valdez and Cordova"></div>
    <h1>Prince William Sound tides &amp; ports — Whittier, Valdez, Cordova</h1>
    <p class="lede">
      One page for the whole Sound: this week&rsquo;s high and low tides from five NOAA stations side by side, all nine National Weather Service marine zones from
      Passage Canal to Hinchinbrook Entrance, live buoy readings, and the harbor, fuel, haul-out, and seafood-processor contacts for the three road/ferry towns.
      Times are local (AKST/AKDT). Heights are feet above Mean Lower Low Water (MLLW). For a full port directory, open the
      <a href="whittier-tides.html">Whittier</a>, <a href="valdez-tides.html">Valdez</a>, or <a href="cordova-tides.html">Cordova</a> page.
    </p>

    <section class="pws-callout" aria-labelledby="pws-callout-heading">
      <h2 id="pws-callout-heading">One tide, three towns &mdash; but nine different forecasts</h2>
      <p><strong>The tide barely changes across the Sound.</strong> In the NOAA predictions fetched {fetched}, every high and low this week at Whittier, Valdez, Cordova,
      Busby Island and Sawmill Bay lands within <strong>{max_spread}&nbsp;minutes</strong> of the others. Next low tide: {lows_line}.
      The biggest drop in the next five weeks is at <strong>{TOWN[bk]}</strong> on <strong>{ba[1].strftime('%A, %B')} {ba[1].day}, {ba[1].year}</strong>:
      a <strong>{hstr(ba[2])}</strong> high at <strong>{tstr(ba[1])}</strong>, then a <strong>{hstr(bb[2])}</strong> low at <strong>{tstr(bb[1])}</strong> &mdash; about <strong>{bd:.1f}&nbsp;ft</strong> of water.
      {minus_txt}. Plan grid work and launches by your own station, but expect the same timing everywhere.</p>
      <p><strong>The weather is where the towns differ.</strong> NWS splits the Sound into seven inside zones plus two outside-coast zones. Passage Canal (Whittier) and
      Port of Valdez are often calm while Valdez Narrows, Valdez Arm, or Hinchinbrook Entrance blow. Read the zone you will actually cross.{warn_txt}</p>
      <p style="color:var(--muted);font-size:0.9rem;">Computed from NOAA CO-OPS hi/lo predictions for 9454949, 9454240, 9454050, 9454374 and 9454764 ({start} onward) and NWS coastal waters forecast text, fetched {fetched}. Not for navigation.</p>
    </section>

    <section class="port-photo-pair" aria-labelledby="pws-photos-heading">
      <p class="port-photo-pair__label" id="pws-photos-heading">Prince William Sound then &amp; now</p>
      <div class="port-photo-grid">
        <figure class="port-photo port-photo--historic">
          <p class="port-photo__era">Historic</p>
          <img
            src="../assets/ports/prince-william-sound/pws-steamer-bertha-1900-wilse-web.jpg"
            alt="Black-and-white photo of the steamship Bertha moored against a forested shore at Landlocked Bay, Prince William Sound, about 1900"
            loading="lazy" decoding="async" width="768" height="353">
          <figcaption class="port-photo__credit">
            Steamer <em>Bertha</em> at Copper Mountain, Landlocked Bay, about 1900, when copper prospects drew steamers into the Sound. Anders Beer Wilse, University of Washington Libraries Special Collections.
            <a href="https://commons.wikimedia.org/wiki/File:Steamer_BERTHA_in_Prince_William_Sound,_probably_1900_(TRANSPORT_411).jpg" rel="noopener">Source</a>
            <span class="port-photo__license port-photo__license--pd">Public domain</span>
          </figcaption>
        </figure>
        <figure class="port-photo port-photo--current port-photo--current-primary">
          <p class="port-photo__era">Current</p>
          <img
            src="../assets/ports/prince-william-sound/pws-seiner-2007-cart5819-web.jpg"
            alt="A purse seiner holding its corkline in a circle on blue water in Prince William Sound, with forested islands and snowy hills behind"
            loading="lazy" decoding="async" width="1000" height="566">
          <figcaption class="port-photo__credit">
            A seiner fishing for salmon in Prince William Sound. Photo by Cart5819 (English Wikipedia),
            <a href="https://commons.wikimedia.org/wiki/File:Seiner_fishing_for_salmon_Prince_William_Sound-2007.jpg" rel="noopener">via Wikimedia Commons</a>, resized.
            <span class="port-photo__license port-photo__license--pd">Public domain</span>
          </figcaption>
        </figure>
      </div>
    </section>

    <p class="actions">
      <a class="btn" href="https://tidesandcurrents.noaa.gov/noaatidepredictions.html?id=9454949" rel="noopener">NOAA Whittier</a>
      <a class="btn" href="https://tidesandcurrents.noaa.gov/noaatidepredictions.html?id=9454240" rel="noopener">NOAA Valdez</a>
      <a class="btn" href="https://tidesandcurrents.noaa.gov/noaatidepredictions.html?id=9454050" rel="noopener">NOAA Cordova</a>
      <a class="btn btn-ghost" href="https://nauticalcharts.noaa.gov/enconline/enconline.html" rel="noopener">NOAA chart viewer</a>
      <a class="btn btn-ghost" href="https://www.windy.com/60.75/-147.0" rel="noopener">View on Windy</a>
    </p>

    <aside class="notice">
      <strong>Not for navigation. Not official.</strong> We copy the tide times and heights below from NOAA CO-OPS predictions for convenience. Always check
      <a href="https://tidesandcurrents.noaa.gov/" rel="noopener">NOAA Tides &amp; Currents</a>
      and current NOAA charts before you work or play on the water. Pacific Tides is not affiliated with or endorsed by NOAA or the National Weather Service.
    </aside>

{sponsor_html("Prince William Sound")}

    <section id="pws-compare" aria-labelledby="pws-compare-heading">
      <h2 id="pws-compare-heading">Port comparison: stations, zones, harbors</h2>
      <p style="color:var(--muted);font-size:0.92rem;">Station IDs from NOAA MDAPI; zone IDs confirmed with the api.weather.gov zone lookup ({start}); harbor facts from each city&rsquo;s harbor pages (links on each port page). Processor counts are verified rows in our directory, not a census.</p>
      <div style="overflow-x:auto;">
      <table class="tides">
<thead><tr><th>Port</th><th>NOAA tide station</th><th>NWS marine zones</th><th>NDBC obs</th><th>Harbor &amp; harbormaster</th><th>Fuel</th><th>Haul-out</th><th>Seafood processors listed</th><th>Getting there</th></tr></thead>
<tbody>
{compare}
</tbody>
      </table>
      </div>
    </section>

{day_tables()}
    <p style="color:var(--muted);font-size:0.9rem;">Tide data: NOAA CO-OPS stations 9454949, 9454240, 9454050, 9454374 and 9454764, predictions (hi/lo, MLLW, local standard/daylight time). H = high, L = low. Refreshed with each nightly build; snapshot fetched {fetched}.</p>

    <section id="marine-weather">
      <h2>Marine weather &amp; cameras</h2>
      <aside class="notice">
        <strong>Not for navigation.</strong> NWS/NDBC data is for information only. Always check official marine forecasts, warnings, and notices before you go.
        Pacific Tides is not affiliated with or endorsed by NOAA or the National Weather Service. Each zone below shows the first four forecast periods; open the official zone forecast for the full text.
      </aside>
{weather()}
      <h3>Harbor webcams</h3>
      <ul class="news-list">
        <li><a href="https://www.borealisbroadband.net/cams/whittierharborcam/" rel="noopener">Borealis Broadband &mdash; Whittier Harbor cam</a> (free public live view; link only)</li>
        <li><a href="https://www.pwssalt.com/whittier-harbor-cam/" rel="noopener">Prince William Sound Salt Co. &mdash; Whittier 360&deg; harbor cam</a> (free public; link only)</li>
        <li><a href="https://www.cliffsidemarina.org/web-cams/" rel="noopener">Cliffside Marina web cams (Whittier)</a> (free public page; link only)</li>
        <li><a href="https://www.youtube.com/@cityofvaldezalaska" rel="noopener">City of Valdez live cams &mdash; South Boat Harbor</a> (free public YouTube stream; link only)</li>
        <li><a href="https://weathercams.faa.gov/cameras/cameraSite/2/details/camera/10001" rel="noopener">FAA WeatherCams &mdash; Whittier (PAWR)</a> · <a href="https://weathercams.faa.gov/cameras/cameraSite/411/details/station/11297" rel="noopener">Valdez (PAVD)</a> · <a href="https://weathercams.faa.gov/map/-145.4445,60.486,9/station/PACV/details/station" rel="noopener">Cordova (PACV)</a> (free public; may read &ldquo;image not available&rdquo; in winter darkness)</li>
      </ul>
      <p class="actions">
        <a class="btn btn-ghost" href="https://www.windy.com/60.75/-147.0" rel="noopener">View on Windy</a>
        <a class="btn btn-ghost" href="https://www.weather.gov/afc/" rel="noopener">NWS Anchorage</a>
        <a class="btn btn-ghost" href="https://www.ndbc.noaa.gov/" rel="noopener">NOAA NDBC</a>
        <a class="btn btn-ghost" href="https://marine.weather.gov/" rel="noopener">NWS Marine Weather</a>
      </p>
    </section>

    <section id="pws-notes" aria-labelledby="pws-notes-heading">
      <h2 id="pws-notes-heading">Sound-wide boater notes (official links)</h2>
      <ul class="news-list">
        <li><a href="https://dot.alaska.gov/amhs/" rel="noopener">Alaska Marine Highway</a>: the ferry links Whittier, Valdez, and Cordova (and is Cordova&rsquo;s only surface link).</li>
        <li><a href="https://dot.alaska.gov/creg/whittiertunnel/" rel="noopener">Anton Anderson Memorial Tunnel</a>: Whittier road access runs on a posted schedule; plan haul-outs and trailer trips around it.</li>
        <li><a href="https://dggs.alaska.gov/hazards/barry-arm-landslide.html" rel="noopener">Barry Arm landslide &amp; tsunami hazard (Alaska DGGS)</a>: read before running up Port Wells or Harriman Fiord.</li>
        <li><a href="https://www.adfg.alaska.gov/index.cfm?adfg=commercialbyareapws.main" rel="noopener">ADF&amp;G Prince William Sound &amp; Copper River commercial fisheries</a>: openers and announcements from the Cordova office.</li>
        <li><a href="https://www.pwsrcac.org/" rel="noopener">Prince William Sound Regional Citizens&rsquo; Advisory Council</a>: oil-tanker and terminal oversight for the Sound.</li>
        <li><a href="https://nauticalcharts.noaa.gov/enconline/enconline.html" rel="noopener">NOAA ENC chart viewer</a> (Prince William Sound is on NOAA chart 16700; we link to NOAA&rsquo;s viewer and do not host charts).</li>
      </ul>
    </section>

    <section class="directory" id="local-directory">
      <h2>Prince William Sound marine directory</h2>
      <p style="color:var(--muted);font-size:0.92rem;">Harbors, fuel, yards, marine services, and seafood processors in Whittier, Valdez, and Cordova &mdash; {dir_count} verified public listings pulled from each port&rsquo;s directory (each row has a public source in our data file). Groceries, lodging, and other shore needs are on each port page. <a href="../advertise.html#list-free">List free</a> · <a href="../advertise.html#local">Get featured ($10/mo or $100/yr)</a></p>
      <h3 class="dir-cat">Marine services</h3>
{chr(10).join(dir_out)}
    </section>
    <p style="color:var(--muted);font-size:0.92rem;">Listings are a courtesy, not an endorsement. Basic listings are free; a <a href="../advertise.html#local">Featured listing is $10/month or $100/year</a>. For corrections or a free listing, contact J.L. Miller at <a href="mailto:pacifictides.ak@gmail.com">pacifictides.ak@gmail.com</a> (email only).</p>

    <section class="local-news" id="local-news">
      <h2>Local news — Prince William Sound</h2>
      <p style="color:var(--muted);font-size:0.92rem;">Plain links to local outlets. Always check the source for the latest. <a href="../advertise.html#news-partner">Local news partners</a> welcome.</p>
      <ul class="news-list">
        <li><a href="https://thecordovatimes.com/?utm_source=pacifictides&amp;utm_medium=referral&amp;utm_campaign=prince-william-sound-news" rel="noopener">The Cordova Times</a> (Prince William Sound&rsquo;s oldest newspaper, est. 1914)</li>
        <li><a href="https://kchu.org/?utm_source=pacifictides&amp;utm_medium=referral&amp;utm_campaign=prince-william-sound-news" rel="noopener">KCHU Public Radio</a> (Valdez, with translators in Cordova, Whittier, Tatitlek, and Chenega Bay)</li>
        <li><a href="https://cordovaradio.com/?utm_source=pacifictides&amp;utm_medium=referral&amp;utm_campaign=prince-william-sound-news" rel="noopener">KLAM-AM / KCDV-FM Cordova Radio</a></li>
        <li><a href="https://www.adn.com/?utm_source=pacifictides&amp;utm_medium=referral&amp;utm_campaign=prince-william-sound-news" rel="noopener">Anchorage Daily News</a></li>
        <li><a href="https://alaskapublic.org/?utm_source=pacifictides&amp;utm_medium=referral&amp;utm_campaign=prince-william-sound-news" rel="noopener">Alaska Public Media</a></li>
        <li><a href="https://www.alaskasnewssource.com/?utm_source=pacifictides&amp;utm_medium=referral&amp;utm_campaign=prince-william-sound-news" rel="noopener">Alaska&#x27;s News Source</a></li>
        <li><a href="https://alaskabeacon.com/?utm_source=pacifictides&amp;utm_medium=referral&amp;utm_campaign=prince-william-sound-news" rel="noopener">Alaska Beacon</a></li>
      </ul>
    </section>
{signup_html("Prince William Sound", "../", "prince-william-sound")}
{affiliate_html()}
{ads_placeholder_html()}

    <section class="other-alaska-ports" aria-labelledby="other-ports-heading">
      <h2 id="other-ports-heading">Prince William Sound port pages</h2>
      <ul>
        <li><a href="whittier-tides.html">Whittier tides</a></li>
        <li><a href="valdez-tides.html">Valdez tides</a></li>
        <li><a href="cordova-tides.html">Cordova tides</a></li>
      </ul>
      <h2>Other Alaska ports</h2>
      <ul>
        <li><a href="kenai-tides.html">Kenai tides</a></li>
        <li><a href="homer-tides.html">Homer tides</a></li>
        <li><a href="kodiak-tides.html">Kodiak tides</a></li>
        <li><a href="juneau-tides.html">Juneau tides</a></li>
        <li><a href="sitka-tides.html">Sitka tides</a></li>
        <li><a href="wrangell-tides.html">Wrangell tides</a></li>
        <li><a href="yakutat-tides.html">Yakutat tides</a></li>
        <li><a href="skagway-tides.html">Skagway tides</a></li>
        <li><a href="haines-tides.html">Haines tides</a></li>
        <li><a href="ketchikan-tides.html">Ketchikan tides</a></li>
        <li><a href="elfin-cove-tides.html">Elfin Cove tides</a></li>
        <li><a href="gustavus-tides.html">Gustavus tides</a></li>
        <li><a href="hoonah-tides.html">Hoonah tides</a></li>
        <li><a href="pelican-tides.html">Pelican tides</a></li>
        <li><a href="craig-tides.html">Craig tides</a></li>
        <li><a href="petersburg-tides.html">Petersburg tides</a></li>
        <li><a href="dutch-harbor-tides.html">Dutch Harbor tides</a></li>
        <li><a href="unalaska-tides.html">Unalaska tides</a></li>
      </ul>
      <p><a href="../index.html">All Pacific Tides ports</a>
       · <a href="alaska-harbor-fuel-haulout.html">Harbor, fuel &amp; haul-out directory</a></p>
    </section>

    <section class="sources">
      <h2>Sources</h2>
      <ul>
        <li>NOAA CO-OPS stations (MDAPI, verified {start}): <a href="https://tidesandcurrents.noaa.gov/stationhome.html?id=9454949" rel="noopener">9454949 Whittier, Passage Canal</a>; <a href="https://tidesandcurrents.noaa.gov/stationhome.html?id=9454240" rel="noopener">9454240 Valdez, Port Valdez</a>; <a href="https://tidesandcurrents.noaa.gov/stationhome.html?id=9454050" rel="noopener">9454050 Cordova</a>; <a href="https://tidesandcurrents.noaa.gov/stationhome.html?id=9454374" rel="noopener">9454374 Busby Island</a> (chart 16707); <a href="https://tidesandcurrents.noaa.gov/stationhome.html?id=9454764" rel="noopener">9454764 Sawmill Bay, Evans Island</a> (subordinate to 9454050)</li>
        <li>Predictions API: <code>api.tidesandcurrents.noaa.gov/api/prod/datagetter</code> (product=predictions, interval=hilo, datum=MLLW, time_zone=lst_ldt)</li>
        <li>NWS Anchorage coastal waters forecast zones PKZ720, PKZ721, PKZ722, PKZ723, PKZ724, PKZ725, PKZ726 (inside the Sound) and PKZ711, PKZ710 (outside coast); zones confirmed via the api.weather.gov zone lookup</li>
        <li>NDBC observations: WIXA2, PPXA2, 46081, VDZA2, 46060, 46061, CRVA2</li>
        <li>Harbor facts: City of Whittier, City of Valdez, and City of Cordova harbor pages (see each port page for check dates)</li>
        <li>Directory: <code>data/businesses.csv</code> rows for port_slug whittier, valdez, cordova, each with its public source URL</li>
        <li>Photos: Anders Beer Wilse / University of Washington Libraries (public domain); Cart5819 (public domain) via Wikimedia Commons. Graphics: original Pacific Tides artwork.</li>
      </ul>
    </section>
  </main>
{footer_html("../")}
</body>
</html>
"""
(ROOT / "pages" / "prince-william-sound-tides.html").write_text(page)
print("wrote", dir_count, "directory rows;", n_proc, "processors;", proc_by, "max_spread", max_spread, "big", bk, round(bd, 1), ba[1], bb[1], "warn", [w[0] for w in warn])
print("obs", {b: bool(o) for b, o in ob.items()})
