#!/usr/bin/env python3
"""Nightly refresh of live port pages: NOAA tide tables, NWS zone forecast, NDBC obs.
Surgical: replaces only the tide-tables section and the forecast/obs block. Never invents data."""
import re, json, time, urllib.request, datetime, html, sys
from zoneinfo import ZoneInfo
UA = {"User-Agent": "PacificTides (pacifictides.ak@gmail.com)"}
AK = ZoneInfo("America/Anchorage")
PORTS = [
 ("petersburg","9451439","pkz034","CDEA2"),
 ("dutch-harbor","9462611","pkz771","DPXA2"),
 ("unalaska","9462620","pkz771","DPXA2"),
 ("kodiak","9457261","pkz738","KDAA2"),
]
def get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r: return r.read().decode("utf-8","replace")
cache = {}
def cached(url):
    if url not in cache: cache[url] = get(url); time.sleep(1)
    return cache[url]
now = datetime.datetime.now(AK)
start = (now + datetime.timedelta(days=1)).date() if now.hour >= 18 else now.date()
def tides(station):
    b = start.strftime("%Y%m%d"); e = (start+datetime.timedelta(days=7)).strftime("%Y%m%d")
    u = (f"https://api.tidesandcurrents.noaa.gov/api/prod/datagetter?product=predictions&application=PacificTides"
         f"&begin_date={b}&end_date={e}&datum=MLLW&station={station}&time_zone=lst_ldt&units=english&interval=hilo&format=json")
    d = json.loads(cached(u))
    preds = d["predictions"]
    days = {}
    for p in preds:
        t = datetime.datetime.strptime(p["t"], "%Y-%m-%d %H:%M")
        days.setdefault(t.date(), []).append((("High" if p["type"]=="H" else "Low"), t, float(p["v"])))
    out = ['<section class="tide-tables">']
    for dte in sorted(days)[:8]:
        out.append(f"<h2>{dte.strftime('%A, %B')} {dte.day}, {dte.year}</h2>")
        out.append('<table class="tides">\n<thead><tr><th>Tide</th><th>Time (local)</th><th>Height (MLLW)</th></tr></thead>\n<tbody>')
        for k,t,v in days[dte]:
            out.append(f"<tr><td>{k}</td><td>{t.strftime('%I:%M %p').lstrip('0')}</td><td>{v:.1f} ft</td></tr>")
        out.append("</tbody>\n</table>")
    out.append("    </section>")
    return "\n".join(out), len(preds)
def forecast(zone):
    txt = cached(f"https://tgftp.nws.noaa.gov/data/forecasts/marine/coastal/pk/{zone}.txt")
    m = re.search(rf"^{zone.upper()}-\d+-\n(.*?)\n\$\$", txt, re.S|re.M)
    blk = m.group(1).strip().split("\n")
    name = blk[0].rstrip("-"); issued = blk[1].strip()
    body = "\n".join(blk[2:]).strip()
    heads = re.findall(r"^\.\.\.(.+?)\.\.\.$", body, re.M)
    per = re.findall(r"^(\.[A-Z][A-Z ]+\.\.\..*?)(?=^\.[A-Z]|\Z)", body, re.S|re.M)
    per = [" ".join(p.split()) for p in per]
    if not per: raise RuntimeError("no periods "+zone)
    return name, issued, heads, per
def obs(st):
    try: txt = get(f"https://www.ndbc.noaa.gov/data/realtime2/{st}.txt")
    except Exception: return None
    rows = [l.split() for l in txt.splitlines() if not l.startswith("#")]
    if not rows: return None
    r = rows[0]
    t = datetime.datetime(int(r[0]),int(r[1]),int(r[2]),int(r[3]),int(r[4]),tzinfo=datetime.timezone.utc).astimezone(AK)
    parts=[]
    if r[5]!="MM": parts.append(f"wind {r[5]}°")
    if r[6]!="MM": parts.append(f"{float(r[6])*1.94384:.0f} kt")
    if r[7]!="MM": parts.append(f"gust {float(r[7])*1.94384:.0f} kt")
    if r[8]!="MM": parts.append(f"seas {float(r[8])*3.28084:.1f} ft")
    if r[13]!="MM": parts.append(f"air {float(r[13])*9/5+32:.0f}°F")
    if r[12]!="MM": parts.append(f"{r[12]} hPa")
    return ", ".join(parts), t
fetched = now.strftime("%Y-%m-%d %H:%M AKST")
report=[]
for slug, station, zone, buoy in PORTS:
    path=f"pages/{slug}-tides.html"; s=open(path).read()
    tt, n = tides(station)
    s, k = re.subn(r'[ \t]*<section class="tide-tables">.*?</section>', tt, s, count=1, flags=re.S)
    assert k==1, slug
    name, issued, heads, per = forecast(zone)
    Z=zone.upper()
    fc = [f'      <h3>NWS marine forecast — {html.escape(name)} ({Z})</h3>',
          f'      <p style="color:var(--muted);font-size:0.92rem;">Issued {html.escape(issued)}. Snapshot fetched {fetched} from NWS text product. <a href="https://marine.weather.gov/MapClick.php?zoneid={Z}&amp;TextType=1" rel="noopener">Official zone forecast</a> · <a href="https://tgftp.nws.noaa.gov/data/forecasts/marine/coastal/pk/{zone}.txt" rel="noopener">Raw text</a></p>']
    for h in heads: fc.append(f"<p><strong>...{html.escape(h)}...</strong></p>")
    fc.append('      <ul class="forecast-periods">')
    for p in per: fc.append(f"        <li>{html.escape(p)}</li>")
    fc.append("      </ul>")
    m = re.search(r'<h3>Nearby NDBC observation — (.*?)</h3>', s)
    fc.append(f"      <h3>Nearby NDBC observation — {m.group(1)}</h3>")
    o = obs(buoy)
    if o:
        fc.append(f"      <p><strong>{o[0]}</strong></p>")
        fc.append(f'      <p style="color:var(--muted);font-size:0.92rem;">Observation time {o[1].strftime("%Y-%m-%d %H:%M")} AKST (converted to AKST). Attribution: NOAA NDBC station <a href="https://www.ndbc.noaa.gov/station_page.php?station={buoy}" rel="noopener">{buoy}</a>. Snapshot fetched {fetched}.</p>')
    else:
        fc.append(f'      <p style="color:var(--muted);font-size:0.92rem;">Live values not cached on this page (realtime file unavailable at fetch {fetched}). Check the station page for current wind/seas: NOAA NDBC <a href="https://www.ndbc.noaa.gov/station_page.php?station={buoy}" rel="noopener">{buoy}</a>. Also <a href="https://www.ndbc.noaa.gov/" rel="noopener">NDBC home</a>.</p>')
    s, k = re.subn(r'[ \t]*<h3>NWS marine forecast.*?(?=[ \t]*<h3>Harbor webcams</h3>)', "\n".join(fc)+"\n", s, count=1, flags=re.S)
    assert k==1, slug
    open(path,"w").write(s)
    report.append((slug, n, issued, heads, bool(o)))
for r in report: print(r)
