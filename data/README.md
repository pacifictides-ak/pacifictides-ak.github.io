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
