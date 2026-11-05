"""Shared HTML snippets for port pages (signup, sponsor, directory, affiliates)."""
from __future__ import annotations
import csv
from html import escape
from pathlib import Path

SITE_ROOT = Path(__file__).resolve().parent.parent
GOPIGEON = "https://api.gopigeon.dev/f/f_53bjw6t5dcxahfdy"
MAIL = "jlmiller99833@gmail.com"

CATEGORY_LABELS = {
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
    "moorage_marinas","fuel_docks","shipyards_haulouts","boat_repair_mechanics",
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
  </footer>"""

def signup_html(port_name: str, prefix: str = "../") -> str:
    return f"""    <section class="signup" id="email-signup">
      <h2>Free weekly tides &amp; marine weather</h2>
      <p>Get a short email for your port. We do not sell your email. <a href="{prefix}privacy.html">Privacy</a>.</p>
      <form class="signup-form" action="{GOPIGEON}" method="POST">
        <input type="hidden" name="_subject" value="Pacific Tides email signup">
        <div class="hp-field" aria-hidden="true"><label>Leave blank<input type="text" name="_gotcha" tabindex="-1" autocomplete="off"></label></div>
        <label for="email">Email<input id="email" name="email" type="email" required autocomplete="email"></label>
        <label for="port">Port<input id="port" name="port" type="text" value="{escape(port_name)}" readonly></label>
        <label class="consent"><input type="checkbox" name="consent" value="yes" required> I agree to receive the free weekly email and accept the privacy policy.</label>
        <button type="submit">Subscribe free</button>
      </form>
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
      <h2>Gear &amp; insurance (affiliate-ready)</h2>
      <p>Plain links for now; affiliate IDs go in marked slots after program approval.</p>
      <div class="affiliate-grid">
        <div class="affiliate-card"><strong>Marine electronics</strong><a href="https://www.garmin.com/en-US/c/marine/" rel="noopener sponsored">Browse</a><span class="tag">Affiliate slot: <!-- AFFILIATE_ID_ELECTRONICS --></span></div>
        <div class="affiliate-card"><strong>Safety gear</strong><a href="https://www.westmarine.com/" rel="noopener sponsored">Browse</a><span class="tag">Affiliate slot: <!-- AFFILIATE_ID_SAFETY --></span></div>
        <div class="affiliate-card"><strong>Fishing gear</strong><a href="https://www.basspro.com/" rel="noopener sponsored">Browse</a><span class="tag">Affiliate slot: <!-- AFFILIATE_ID_FISHING --></span></div>
        <div class="affiliate-card"><strong>Boat insurance quotes</strong><a href="https://www.progressive.com/boat/" rel="noopener sponsored">Browse</a><span class="tag">Affiliate slot: <!-- AFFILIATE_ID_INSURANCE --></span></div>
      </div>
    </section>"""

def ads_placeholder_html() -> str:
    return """    <aside class="ad-placeholder" id="display-ads">
      Display ads placeholder — AdSense later. No ad code yet.
    </aside>"""

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
