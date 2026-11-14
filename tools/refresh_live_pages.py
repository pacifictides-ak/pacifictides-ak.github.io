#!/usr/bin/env python3
"""Nightly refresh of live port pages: NOAA tide tables, NWS zone forecast, NDBC obs.
Surgical: replaces only the tide-tables section and the forecast/obs block. Never invents data."""
import re, json, time, urllib.request, datetime, html, sys
from zoneinfo import ZoneInfo
UA = {"User-Agent": "PacificTides (pacifictides.ak@gmail.com)"}
AK = ZoneInfo("America/Anchorage")
# (slug, tide station, [NWS coastal zones], [NDBC stations])
PORTS = [
 ("petersburg","9451439",["pkz034"],["CDEA2"]),
 ("dutch-harbor","9462611",["pkz771"],["DPXA2"]),
 ("unalaska","9462620",["pkz771"],["DPXA2"]),
 ("kodiak","9457261",["pkz738"],["KGXA2","KDAA2"]),
 ("homer","9455558",["pkz741","pkz742"],["HMSA2","46108","FILA2"]),
 ("valdez","9454240",["pkz720","pkz721","pkz722"],["VDZA2","46060","46061"]),
 ("whittier","9454949",["pkz723","pkz724","pkz726"],["WIXA2","PPXA2","46081"]),
 ("kenai","9455742",["pkz740","pkz742"],["KNXA2","NKTA2","46108"]),
 ("cordova","9454050",["pkz725","pkz710"],["CRVA2","46060","46061"]),
 ("juneau","9452210",["pkz031","pkz013"],["JNEA2","PTLA2","SCXA2"]),
]
# Heading labels for NDBC stations (used when the page has no existing heading for that station)
BUOY_NAMES = {
 "HMSA2": "Homer Spit (HMSA2, Marine Exchange of Alaska)",
 "46108": "Lower Cook Inlet buoy (46108, Alaska Ocean Observing System)",
 "FILA2": "Flat Island Light (FILA2)",
 "KGXA2": "Kodiak Gull Island (KGXA2, Marine Exchange of Alaska)",
 "VDZA2": "Valdez (VDZA2, NOAA 9454240)",
 "46060": "West Orca Bay buoy (46060)",
 "46061": "Seal Rocks buoy (46061, Hinchinbrook Entrance)",
 "WIXA2": "Whittier AMHS terminal (WIXA2)",
 "PPXA2": "Point Pigot (PPXA2)",
 "46081": "Western Prince William Sound buoy (46081)",
 "KNXA2": "Kenai (KNXA2, Marine Exchange of Alaska)",
 "NKTA2": "Nikiski (NKTA2, NOAA 9455760)",
 "CRVA2": "Cordova (CRVA2, NOAA 9454050)",
 "JNEA2": "Juneau (JNEA2, NOAA 9452210)",
 "PTLA2": "Portland Island (PTLA2, off Auke Bay)",
 "SCXA2": "Scull Island (SCXA2, Stephens Passage)",
}
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
            out.append(f"<tr><td>{k}</td><td>{t.strftime('%I:%M %p').lstrip('0')}</td><td>{(0.0 if abs(v)<0.05 else v):.1f} ft</td></tr>")
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
    if len(r)>14 and r[14]!="MM": parts.append(f"water {float(r[14])*9/5+32:.0f}°F")
    if not parts: return None
    return ", ".join(parts), t
fetched = now.strftime("%Y-%m-%d %H:%M AKST")
report=[]
only = set(sys.argv[1:])
for slug, station, zones, buoys in PORTS:
    if only and slug not in only: continue
    path=f"pages/{slug}-tides.html"; s=open(path).read()
    tt, n = tides(station)
    s, k = re.subn(r'[ \t]*<section class="tide-tables">.*?</section>', tt, s, count=1, flags=re.S)
    assert k==1, slug
    fc = []
    issued_all = []
    for zone in zones:
        name, issued, heads, per = forecast(zone)
        issued_all.append(issued)
        Z=zone.upper()
        fc += [f'      <h3>NWS marine forecast — {html.escape(name)} ({Z})</h3>',
              f'      <p style="color:var(--muted);font-size:0.92rem;">Issued {html.escape(issued)}. Snapshot fetched {fetched} from NWS text product. <a href="https://marine.weather.gov/MapClick.php?zoneid={Z}&amp;TextType=1" rel="noopener">Official zone forecast</a> · <a href="https://tgftp.nws.noaa.gov/data/forecasts/marine/coastal/pk/{zone}.txt" rel="noopener">Raw text</a></p>']
        for h in heads: fc.append(f"<p><strong>...{html.escape(h)}...</strong></p>")
        fc.append('      <ul class="forecast-periods">')
        for p in per: fc.append(f"        <li>{html.escape(p)}</li>")
        fc.append("      </ul>")
    oks = []
    for buoy in buoys:
        m = re.search(rf'<h3>Nearby NDBC observation — (.*?{buoy}.*?)</h3>', s)
        label = m.group(1) if m else BUOY_NAMES.get(buoy, buoy)
        fc.append(f"      <h3>Nearby NDBC observation — {label}</h3>")
        o = obs(buoy)
        oks.append(bool(o))
        if o:
            fc.append(f"      <p><strong>{o[0]}</strong></p>")
            fc.append(f'      <p style="color:var(--muted);font-size:0.92rem;">Observation time {o[1].strftime("%Y-%m-%d %H:%M")} AKST (converted to AKST). Attribution: NOAA NDBC station <a href="https://www.ndbc.noaa.gov/station_page.php?station={buoy}" rel="noopener">{buoy}</a>. Snapshot fetched {fetched}.</p>')
        else:
            fc.append(f'      <p style="color:var(--muted);font-size:0.92rem;">Live values not cached on this page (realtime file unavailable at fetch {fetched}). Check the station page for current wind/seas: NOAA NDBC <a href="https://www.ndbc.noaa.gov/station_page.php?station={buoy}" rel="noopener">{buoy}</a>. Also <a href="https://www.ndbc.noaa.gov/" rel="noopener">NDBC home</a>.</p>')
        time.sleep(1)
    s, k = re.subn(r'[ \t]*<h3>NWS marine forecast.*?(?=[ \t]*<h3>Harbor webcams</h3>)', "\n".join(fc)+"\n", s, count=1, flags=re.S)
    assert k==1, slug
    open(path,"w").write(s)
    report.append((slug, n, issued_all, oks))
for r in report: print(r)
