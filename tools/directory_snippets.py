"""Shared HTML snippets for port pages (signup, sponsor, directory, affiliates)."""
from __future__ import annotations
import csv
from html import escape
from pathlib import Path

SITE_ROOT = Path(__file__).resolve().parent.parent
BUTTONDOWN_SUBSCRIBE = "https://buttondown.com/api/emails/embed-subscribe/pacifictides"
MAIL = "pacifictides.ak@gmail.com"

CATEGORY_LABELS = {
    "seafood_processors": "Seafood processors & buyers",
    "shipyards_haulouts": "Shipyards & haul-outs",
    "boat_repair_mechanics": "Boat repair & mechanics",
    "fuel_docks": "Fuel docks",
    "marine_suppliers_chandleries": "Marine suppliers & chandleries",
    "electronics_sales_installation": "Electronics sales & installation",
    "welding_fabrication": "Welding & fabrication",
    "canvas_upholstery": "Canvas & upholstery",
    "surveyors": "Surveyors",
    "towing_salvage": "Towing & salvage",
    "moorage_marinas": "Moorage & marinas",
    "ice_bait": "Ice & bait",
    "fishing_charters": "Fishing charters",
    "groceries_provisioning": "Groceries & provisioning",
    "hardware": "Hardware",
    "liquor_stores": "Liquor stores",
    "laundromats": "Laundromats",
    "showers": "Showers",
    "lodging": "Lodging",
    "restaurants": "Restaurants",
    "medical_clinics": "Medical clinics",
    "pharmacies": "Pharmacies",
    "post_office_shipping": "Post office & shipping",
    "airport_floatplane": "Airport & floatplane",
    "propane": "Propane",
    "auto_truck_rental": "Auto & truck rental",
}
MARINE_ORDER = list(CATEGORY_LABELS)[:12]
# explicit orders
MARINE_ORDER = [
    "moorage_marinas","seafood_processors","fuel_docks","shipyards_haulouts","boat_repair_mechanics",
    "marine_suppliers_chandleries","electronics_sales_installation","welding_fabrication",
    "canvas_upholstery","surveyors","towing_salvage","ice_bait","fishing_charters",
]
ASHORE_ORDER = [
    "groceries_provisioning","hardware","liquor_stores","laundromats","showers","lodging",
    "restaurants","medical_clinics","pharmacies","post_office_shipping","airport_floatplane",
    "propane","auto_truck_rental",
]

def nav_html(prefix: str = "../") -> str:
    return f"""  <header class="site-header">
    <a class="brand" href="{prefix}index.html">Pacific Tides</a>
    <nav>
      <a href="{prefix}index.html">Directory</a>
      <a href="{prefix}advertise.html">Advertise</a>
      <a href="{prefix}about.html">About</a>
      <a href="{prefix}privacy.html">Privacy</a>
    </nav>
  </header>"""

def footer_html(prefix: str = "../") -> str:
    return f"""  <footer class="site-footer">
    <p>Pacific Tides — Alaska &amp; West Coast marine directory. Data © NOAA CO-OPS. Not for navigation.
    <a href="{prefix}privacy.html">Privacy</a> · <a href="{prefix}advertise.html">Advertise</a></p>
    <p class="amazon-disclosure"><em>As an Amazon Associate I earn from qualifying purchases.</em></p>
  </footer>"""

def signup_html(port_name: str, prefix: str = "../", port_slug: str = "") -> str:
    tag_line = ""
    if port_slug:
        tag_line = f'        <input type="hidden" name="tag" value="{escape(port_slug)}">\n'
    return f"""    <section class="signup" id="email-signup">
      <h2>Free weekly tides &amp; marine weather</h2>
      <p>Get a short email for your port. We do not sell your email. <a href="{prefix}privacy.html">Privacy</a>.</p>
      <form class="signup-form" action="{BUTTONDOWN_SUBSCRIBE}" method="post" target="popupwindow"
            onsubmit="window.open('https://buttondown.com/pacifictides', 'popupwindow')">
{tag_line}        <label for="bd-email">Email
          <input id="bd-email" name="email" type="email" required placeholder="you@example.com" autocomplete="email">
        </label>
        <label class="consent"><input type="checkbox" name="consent" value="yes" required> I agree to receive the free weekly tides &amp; marine weather email and accept the <a href="{prefix}privacy.html">privacy policy</a>.</label>
        <button type="submit">Subscribe free</button>
      </form>
      <p style="margin:0.75rem 0 0;font-size:0.85rem;color:var(--muted);">Mailing list powered by <a href="https://buttondown.com" rel="noopener">Buttondown</a>.</p>
    </section>"""

def sponsor_html(port_name: str, prefix: str = "../") -> str:
    return f"""    <section class="sponsor-slot" id="port-sponsor">
      <h2>Port Sponsor — {escape(port_name)}</h2>
      <p>Top placement for fuel docks, marinas, yards, and marine businesses.</p>
      <p class="price">$25–$50 / month</p>
      <p><a class="btn" href="{prefix}advertise.html#port-sponsor">Become Port Sponsor</a>
      <a class="btn btn-ghost" href="{prefix}advertise.html#local">Local listing $10/mo or $100/yr</a></p>
    </section>"""

def affiliate_html() -> str:
    return """    <section class="affiliate-box" id="gear-insurance">
      <h2>Boating gear on Amazon</h2>
      <p class="amazon-disclosure"><em>As an Amazon Associate I earn from qualifying purchases.</em></p>
      <p>Helpful search links for common gear. Prices and availability are on Amazon.</p>
      <div class="affiliate-grid">
        <div class="affiliate-card"><strong>Marine VHF radios</strong><div><a href="https://www.amazon.com/s?k=marine+VHF+radio&tag=pacifictides-20" rel="noopener sponsored nofollow">Shop on Amazon</a></div><span class="tag">tag=pacifictides-20</span></div>
        <div class="affiliate-card"><strong>Life jackets / PFDs</strong><div><a href="https://www.amazon.com/s?k=life+jacket+PFD+marine&tag=pacifictides-20" rel="noopener sponsored nofollow">Shop on Amazon</a></div><span class="tag">tag=pacifictides-20</span></div>
        <div class="affiliate-card"><strong>Tide clocks</strong><div><a href="https://www.amazon.com/s?k=tide+clock&tag=pacifictides-20" rel="noopener sponsored nofollow">Shop on Amazon</a></div><span class="tag">tag=pacifictides-20</span></div>
        <div class="affiliate-card"><strong>Fishing gear</strong><div><a href="https://www.amazon.com/s?k=saltwater+fishing+gear&tag=pacifictides-20" rel="noopener sponsored nofollow">Shop on Amazon</a></div><span class="tag">tag=pacifictides-20</span></div>
        <div class="affiliate-card"><strong>Anchors</strong><div><a href="https://www.amazon.com/s?k=boat+anchor&tag=pacifictides-20" rel="noopener sponsored nofollow">Shop on Amazon</a></div><span class="tag">tag=pacifictides-20</span></div>
        <div class="affiliate-card"><strong>Bilge pumps</strong><div><a href="https://www.amazon.com/s?k=bilge+pump&tag=pacifictides-20" rel="noopener sponsored nofollow">Shop on Amazon</a></div><span class="tag">tag=pacifictides-20</span></div>
        <div class="affiliate-card"><strong>Marine electronics</strong><div><a href="https://www.amazon.com/s?k=marine+electronics+fish+finder+GPS&tag=pacifictides-20" rel="noopener sponsored nofollow">Shop on Amazon</a></div><span class="tag">tag=pacifictides-20</span></div>
        <div class="affiliate-card"><strong>Boat insurance quotes</strong><div><a href="https://www.progressive.com/boat/" rel="noopener">Progressive Boat</a> · <a href="https://www.boatus.com/insurance" rel="noopener">BoatUS</a></div><span class="tag">Non-Amazon</span></div>
      </div>
    </section>
"""


def ads_placeholder_html() -> str:
    return """    <aside class="ad-placeholder" id="display-ads">
      Display ads placeholder — AdSense later. No ad code yet.
    </aside>"""


def local_news_html(port_slug: str, port_name: str = "") -> str:
    """Render Local news links for a port from data/local_news.csv with UTM tags."""
    path = SITE_ROOT / "data" / "local_news.csv"
    rows = []
    if path.exists():
        with path.open() as f:
            rows = [r for r in csv.DictReader(f) if r.get("port_slug") == port_slug]
    title = escape(port_name) if port_name else escape(port_slug.replace("-", " ").title())
    campaign = f"{port_slug}-news"

    def with_utm(url: str) -> str:
        from urllib.parse import urlparse, parse_qsl, urlencode, urlunparse
        parts = urlparse(url.strip())
        q = dict(parse_qsl(parts.query, keep_blank_values=True))
        q["utm_source"] = "pacifictides"
        q["utm_medium"] = "referral"
        q["utm_campaign"] = campaign
        return urlunparse(parts._replace(query=urlencode(q)))

    if not rows:
        return f"""    <section class="local-news" id="local-news">
      <h2>Local news — {title}</h2>
      <p class="dir-empty">No verified local news links yet for this port.</p>
    </section>"""
    items = []
    for r in rows:
        name = escape(r["name"])
        url = escape(with_utm(r["url"]))
        items.append(f'        <li><a href="{url}" rel="noopener">{name}</a></li>')
    lis = "\n".join(items)
    return f"""    <section class="local-news" id="local-news">
      <h2>Local news — {title}</h2>
      <p style="color:var(--muted);font-size:0.92rem;">Plain links to local outlets. Always check the source for the latest. <a href="../advertise.html#news-partner">Local news partners</a> welcome.</p>
      <ul class="news-list">
{lis}
      </ul>
    </section>"""


def directory_html(port_slug: str, prefix: str = "../") -> str:
    path = SITE_ROOT / "data" / "businesses.csv"
    rows = []
    if path.exists():
        with path.open() as f:
            rows = [r for r in csv.DictReader(f) if r["port_slug"] == port_slug]
    by_cat: dict[str, list] = {}
    for r in rows:
        by_cat.setdefault(r["category"], []).append(r)

    def block(title: str, order: list[str]) -> str:
        out = [f'      <h3 class="dir-cat">{escape(title)}</h3>']
        for cat in order:
            label = CATEGORY_LABELS.get(cat, cat)
            out.append(f'      <h4 class="dir-cat" style="font-size:0.95rem;margin-top:0.7rem;">{escape(label)}</h4>')
            items = by_cat.get(cat, [])
            if not items:
                out.append(f'      <p class="dir-empty">No verified listing yet — <a href="{prefix}advertise.html#list-free">list your business free</a>.</p>')
                continue
            items = sorted(items, key=lambda x: (0 if x.get("featured") == "yes" else 1, x["name"].lower()))
            for it in items:
                cls = "listing featured" if it.get("featured") == "yes" else "listing"
                meta = []
                if it.get("phone"):
                    meta.append(f'<a href="tel:{escape(it["phone"].replace("-",""))}">{escape(it["phone"])}</a>')
                if it.get("email"):
                    meta.append(f'<a href="mailto:{escape(it["email"])}">{escape(it["email"])}</a>')
                if it.get("website"):
                    meta.append(f'<a href="{escape(it["website"])}" rel="noopener">Website</a>')
                if it.get("address"):
                    meta.append(escape(it["address"]))
                desc = f'<div class="desc">{escape(it["description"])}</div>' if it.get("featured") == "yes" and it.get("description") else ""
                out.append(f'      <div class="{cls}"><div class="name">{escape(it["name"])}</div><div class="meta">{" · ".join(meta)}</div>{desc}</div>')
        return "\n".join(out)

    return f"""    <section class="directory" id="local-directory">
      <h2>Local marine &amp; shore directory</h2>
      <p style="color:var(--muted);font-size:0.92rem;">Verified public listings only. <a href="{prefix}advertise.html#list-free">List free</a> · <a href="{prefix}advertise.html#local">Get featured</a></p>
{block("Marine services", MARINE_ORDER)}
{block("Ashore for boaters", ASHORE_ORDER)}
    </section>"""
