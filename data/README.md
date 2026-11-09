# Pacific Tides — port inventory

`ports.csv` is the master list of port cities/towns with harbors or commercial/recreational ports across Alaska, British Columbia, Washington, Oregon, and California.

## Columns

- `tide_agency` / `tide_station_id` — NOAA CO-OPS id or CHS IWLS code; `UNKNOWN` if no station within 80 km
- `tide_station_distance_km` — haversine from community lat/lon to station
- `current_station_id` — nearest NOAA current-prediction station within 40 km (U.S. only)
- `priority_score` — shipping order hint (search demand + revenue); higher first
- `sources` — authoritative list(s) the community was drawn from

## Sources (2026-11-05)

- Alaska: DOT&PF *Public Ports & Harbors in Alaska* (May 2018) locator index
- Washington: Washington Public Ports Association member ports (marine/coastal subset; inland dry ports omitted)
- Oregon: Oregon Public Ports Association / Oregon Blue Book port districts
- California: coastal public harbors & port districts (Coast Pilot / harbor districts / CAHBMPC)
- British Columbia: DFO Small Craft Harbours + major port authorities; tide stations from CHS IWLS
- Stations: NOAA MDAPI `stations.json?type=tidepredictions` / `currentpredictions`; CHS `api-iwls.dfo-mpo.gc.ca/api/v1/stations`

Do not invent station IDs. Re-verify before shipping a page.


## businesses.csv

Yellow-pages style marine + ashore directory for each port.

### Columns

- `port_slug` — matches the tide page slug (e.g. `petersburg`)
- `name`, `category`, `phone`, `website`, `address`
- `featured` — `yes` for paid featured listings ($10/mo or $100/yr); `no` for free basic
- `description`, `logo_url` — used only when `featured=yes`
- `source_url`, `verified_date` — public source used to verify; never invent businesses
- `email` — public business email shown on the listing (optional; added 2026-11-08)
- `notes` — internal

### Categories (marine)

seafood_processors, shipyards_haulouts, boat_repair_mechanics, fuel_docks, marine_suppliers_chandleries, electronics_sales_installation, welding_fabrication, canvas_upholstery, surveyors, towing_salvage, moorage_marinas, ice_bait, fishing_charters

### Categories (ashore)

groceries_provisioning, hardware, liquor_stores, laundromats, showers, lodging, restaurants, medical_clinics, pharmacies, post_office_shipping, airport_floatplane, propane, auto_truck_rental

Free basic listings: name, category, phone, website. Featured: top placement, highlight, logo, description.


## local_news.csv

Plain links to real local news outlets per port. Columns: `port_slug`, `name`, `url`, `notes`.
Only verified working URLs. Do not invent outlets.

Rendered links append `?utm_source=pacifictides&utm_medium=referral&utm_campaign=<port_slug>-news`.
