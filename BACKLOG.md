# Pacific Tides — phased nightly backlog

Ship **one** useful page per night. Prefer official sources; never invent data.
Master port inventory: [`data/ports.csv`](data/ports.csv) (generated 2026-11-05).
Station IDs verified against NOAA MDAPI `/stations.json?type=tidepredictions`
(U.S.) or CHS IWLS `/api/v1/stations` (BC). Re-verify before shipping if a
station looks stale. Rows marked `UNKNOWN` must be resolved before a tide page ships.

**Audiences (all phases):** recreational boaters & anglers · independent vessel owners
& operators · commercial fishermen · company vessels & fleet operators · coastal /
maritime businesses.

**Monetization keys:** `aff` = affiliate gear/services · `sponsor` = local harbor /
lodge / marine business · `fleet` = fleet planning / B2B services · `reg` = traffic
magnet via regs/safety (monetize via related pages).

**Build order:** high-demand hubs first (Dutch Harbor, Kodiak, Anchorage, Seattle,
SF/LA/SD, Astoria, Newport, Eureka…) → fill Alaska regions (SE → Southcentral →
**Kodiak Island** → **Aleutian Chain & Alaska Peninsula** → Bristol Bay → Arctic) →
WA/OR/CA remaining ports → BC (CHS). Interleave harbor/fleet directory pages once
traffic exists.

**Coverage:** 254 port communities — AK 91, BC 46, WA 46, OR 25, CA 46. Tide station gaps: 4.

---

## Phase 0 — Done

- [x] Petersburg, AK tides — NOAA `9451439` · aff/sponsor
- [x] Dutch Harbor / Amaknak, AK tides — NOAA `9462611` · fleet + sponsor + aff
- [x] Unalaska, AK tides — NOAA `9462620` · fleet + sponsor + aff
- [x] Kodiak, AK tides — NOAA `9457261` · fleet + sponsor + aff
- [x] Live-ports harbor, fuel dock, and haul-out directory — Petersburg, Dutch Harbor/Unalaska, Kodiak · [pages/alaska-harbor-fuel-haulout.html](pages/alaska-harbor-fuel-haulout.html) · shipped 2026-11-07 (Homer section added 2026-11-08)
- [x] Homer, AK tides — NOAA `9455558` (Coal Point, Kachemak Bay) · NWS PKZ741/PKZ742 · NDBC HMSA2/46108/FILA2 · harbor, seafood & shore directory · [pages/homer-tides.html](pages/homer-tides.html) · shipped 2026-11-08 · sponsor + aff

---

## Phase 1 — Priority hubs (search demand + revenue)

Ship these early; they unlock fleet/sponsor deals and organic search.

1. ~~**Dutch Harbor / Amaknak, AK tides** — NOAA `9462611`~~ *(shipped 2026-11-05)*
2. ~~**Unalaska, AK tides** — NOAA `9462620` (Unalaska, 0.7km) · current `UNI1015` (0.7km) · fleet + sponsor + aff~~ *(shipped 2026-11-05)*
3. ~~**Kodiak, AK tides** — NOAA `9457261` (Kodiak, Port of Kodiak, 1.4km) · current `KOD0903` (0.8km) · fleet + sponsor + aff~~ *(shipped 2026-11-06)*
4. **Anchorage (Port of Alaska), AK tides** — NOAA `9455920` (ANCHORAGE, Knik Arm, 0.7km) · current `PCT5146` (1.1km) · fleet + sponsor + aff
5. **Seattle (Elliott Bay), WA tides** — NOAA `9447130` (SEATTLE (Madison St.), Elliott Bay, 0.5km) · current `PUG1506` (2.0km) · fleet + sponsor + aff
6. **San Diego, CA tides** — NOAA `9410170` (SAN DIEGO (Broadway), 0.2km) · current `PCT0076` (0.3km) · fleet + sponsor + aff
7. **Los Angeles / San Pedro, CA tides** — NOAA `9410660` (LOS ANGELES (Outer Harbor), 2.2km) · current `lb0101` (8.0km) · fleet + sponsor + aff
8. **Long Beach, CA tides** — NOAA `9410678` (Long Beach Fire Boat Pier, 0.7km) · current `lb0101` (4.8km) · fleet + sponsor + aff
9. **San Francisco, CA tides** — NOAA `9414305` (San Francisco, North Point, Pier 41, 0.8km) · current `SFB1206` (0.7km) · fleet + sponsor + aff
10. **Vancouver, BC tides** — CHS `07735` (Vancouver, 0.9km) · fleet + sponsor + aff
11. ~~**Homer, AK tides** — NOAA `9455558` (Homer, Coal Point, Kachemak Bay, 9.0km) · current `COI0421` (9.5km) · sponsor + aff~~ *(shipped 2026-11-08)*
12. **Oakland, CA tides** — NOAA `9414764` (Oakland Inner Harbor, 0.2km) · current `SFB1214` (0.5km) · fleet + sponsor + aff
13. **Seward, AK tides** — NOAA `9455090` (Seward, Resurrection Bay, 1.9km) · sponsor + aff
14. **Astoria, OR tides** — NOAA `9439026` (Astoria (Youngs Bay), Oreg., 2.0km) · current `PCT1146` (3.2km) · sponsor + aff
15. **Newport, OR tides** — NOAA `9435385` (YAQUINA USCG STA, NEWPORT, 1.2km) · current `PCT1081` (1.6km) · sponsor + aff
16. **Tacoma (Commencement Bay), WA tides** — NOAA `9446484` (Tacoma, Commencement Bay, Sitcum Waterway, 0.5km) · current `PUG1521` (7.4km) · fleet + sponsor + aff
17. **Eureka / Humboldt Bay, CA tides** — NOAA `9418801` (Eureka, 0.5km) · current `PCT1026` (2.0km) · sponsor + aff
18. **Juneau, AK tides** — NOAA `9452210` (Juneau, 0.6km) · current `SEA0801` (0.7km) · sponsor + aff
19. **Ketchikan, AK tides** — NOAA `9450460` (Ketchikan, 1.7km) · current `PCT2786` (0.7km) · sponsor + aff
20. **Sitka, AK tides** — NOAA `9451600` (Sitka, 0.9km) · current `PCT4166` (0.4km) · sponsor + aff
21. **Valdez, AK tides** — NOAA `9454240` (VALDEZ, Port Valdez, 1.0km) · current `PWS0746` (1.4km) · fleet + sponsor + aff
22. **Prince Rupert, BC tides** — CHS `09354` (Prince Rupert, 0.3km) · fleet + sponsor + aff
23. **Victoria, BC tides** — CHS `07120` (Victoria Harbour, 0.3km) · sponsor + aff
24. **Coos Bay, OR tides** — NOAA `9432845` (Coos Bay, 1.6km) · current `PCT1061` (10.1km) · fleet + sponsor + aff

---

## Phase 2 — Southeast Alaska town tides

25. **Juneau, AK tides** — NOAA `9452210` (Juneau, 0.6km) · current `SEA0801` (0.7km) · sponsor + aff *(also Phase 1 hub)*
26. **Ketchikan, AK tides** — NOAA `9450460` (Ketchikan, 1.7km) · current `PCT2786` (0.7km) · sponsor + aff *(also Phase 1 hub)*
27. **Sitka, AK tides** — NOAA `9451600` (Sitka, 0.9km) · current `PCT4166` (0.4km) · sponsor + aff *(also Phase 1 hub)*
28. **Angoon, AK tides** — NOAA `9451895` (Killisnoo, 3.9km) · current `PCT4106` (0.4km) · sponsor + aff
29. **Auke Bay (Juneau), AK tides** — NOAA `9452263` (Auke Bay, 0.1km) · current `SEA0815` (3.5km) · sponsor + aff
30. **Baranof Warm Springs, AK tides** — NOAA `9451625` (Baranof, Warm Spring Bay, 0.5km) · current `PCT4081` (12.9km) · sponsor + aff
31. **Bartlett Cove (Glacier Bay), AK tides** — NOAA `9452534` (Bartlett Cove, Glacier Bay, 0.2km) · current `SEA0847` (8.7km) · sponsor + aff
32. **Coffman Cove, AK tides** — NOAA `9450906` (Beck Island, Clarence Strait, 4.2km) · current `PCT3036` (8.0km) · sponsor + aff
33. **Craig, AK tides** — NOAA `9450551` (Craig, Klawock Inlet, 1.4km) · current `PCT3356` (0.8km) · sponsor + aff
34. **Edna Bay, AK tides** — NOAA `9450859` (Edna Bay, 0.3km) · current `SEA0623` (9.6km) · sponsor + aff
35. **Elfin Cove, AK tides** — NOAA `9452634` (Elfin Cove, Port Althorp, 0.0km) · current `SEA0831` (1.2km) · sponsor + aff
36. **Gustavus, AK tides** — NOAA `9452534` (Bartlett Cove, Glacier Bay, 9.8km) · current `SEA1001` (11.5km) · sponsor + aff
37. **Haines, AK tides** — NOAA `9452435` (Haines Inlet, 0.9km) · current `SEA0825` (5.0km) · sponsor + aff
38. **Hollis, AK tides** — NOAA `9450544` (Hollis Anchorage, 0.5km) · current `SEA0709` (21.1km) · sponsor + aff
39. **Hoonah, AK tides** — NOAA `9452438` (Hoonah, Port Fredrick, 0.3km) · current `SEA0839` (10.8km) · sponsor + aff
40. **Hydaburg, AK tides** — NOAA `9450364` (HYDABURG, SUKKWAN STRAIT, 0.8km) · current `PCT3256` (1.1km) · sponsor + aff
41. **Hyder, AK tides** — NOAA `9450831` (Hyder, Portland Canal, 1.4km) · current `PCT2731` (3.9km) · sponsor + aff
42. **Kake, AK tides** — NOAA `9451528` (Kake Harbor, Keku Strait, 4.4km) · current `SEA0505` (1.2km) · sponsor + aff
43. **Kasaan, AK tides** — NOAA `9450581` (Kasaan, 0.8km) · current `SEA0709` (6.8km) · sponsor + aff
44. **Klawock, AK tides** — NOAA `9450618` (Shinaku Inlet, 5.5km) · current `SEA0901` (7.5km) · sponsor + aff
45. **Kupreanof, AK tides** — NOAA `9451439` (Petersburg, 1.6km) · current `PCT3796` (0.8km) · sponsor + aff
46. **Metlakatla, AK tides** — NOAA `9450314` (Metlakatla, Port Chester, 0.3km) · current `PCT2886` (0.6km) · sponsor + aff
47. **Naukati Bay, AK tides** — NOAA `9450817` (Tuxekan, 0.5 mile south of, 2.4km) · current `PCT3456` (2.4km) · sponsor + aff
48. **Pelican, AK tides** — NOAA `9452611` (Pelican Harbor, Lisianski Inlet, AK, 0.3km) · current `SEA0851` (8.9km) · sponsor + aff
49. **Point Baker, AK tides** — NOAA `9451095` (Port Protection, Prince of Wales Island., 5.1km) · current `SEA0606` (2.7km) · sponsor + aff
50. **Port Alexander, AK tides** — NOAA `9451054` (Port Alexander, Baranof Island, 0.4km) · current `PCT4061` (12.2km) · sponsor + aff
51. **Port Protection, AK tides** — NOAA `9451095` (Port Protection, Prince of Wales Island., 1.6km) · current `SEA0606` (2.3km) · sponsor + aff
52. **Saxman, AK tides** — NOAA `9450460` (Ketchikan, 2.5km) · current `PCT2781` (0.5km) · sponsor + aff
53. **Skagway, AK tides** — NOAA `9452400` (Skagway, Taiya Inlet, 1.2km) · current `SEA0824` (1.6km) · sponsor + aff
54. **Tenakee Springs, AK tides** — NOAA `9452386` (Tenakee Springs, Tenakee Inlet, 0.1km) · current `PCT4111` (22.9km) · sponsor + aff
55. **Thorne Bay, AK tides** — NOAA `9450625` (Lindeman Cove, 9.6km) · current `PCT3026` (12.5km) · sponsor + aff
56. **Whale Pass, AK tides** — NOAA `9450937` (El Capitan Passage, S. of Devilfish Bay, 11.4km) · current `PCT3496` (9.1km) · sponsor + aff
57. **Wrangell, AK tides** — NOAA `9451204` (Wrangell, Wrangell Island, 0.6km) · current `PCT3126` (1.5km) · sponsor + aff
58. **Yakutat, AK tides** — NOAA `9453220` (Yakutat, Yakutat Bay, 0.4km) · sponsor + aff

---

## Phase 3 — SE AK harbors, fuel, haul-out & safety (sponsor / reg)

59. **Petersburg harbor directory** — city/borough + harbor office links only · sponsor
60. **Juneau harbors directory (Aurora / Harris / Douglas / Statter)** — CBJ official · sponsor
61. **Ketchikan harbors directory** — city official · sponsor
62. **Sitka harbors directory** — city official · sponsor
63. **Wrangell harbor directory** — city official · sponsor
64. **SE Alaska fuel docks shortlist** — published operator/harbor pages only · sponsor + aff
65. **SE Alaska haul-out / shipyard shortlist** — published yards only · fleet + sponsor
66. **Cold-water & immersion safety hub** — USCG / Alaska Sea Grant cites · reg → aff
67. **Float plan & voyage checklist** — USCG NavCen / Safe Boating · reg → fleet
68. **NWS marine forecast zones for SE AK (PKZ…)** — zone deep links · reg
69. **ADF&G SE sport fishing regs landing** — ADF&G deep link · reg
70. **ADF&G emergency orders — how to check** — official EO pages · reg + commercial
71. **NOAA chart viewer shortcuts (Wrangell Narrows / Frederick Sound)** — official charts · fleet

---

## Phase 4 — Southcentral Alaska tides

72. **Anchorage (Port of Alaska), AK tides** — NOAA `9455920` (ANCHORAGE, Knik Arm, 0.7km) · current `PCT5146` (1.1km) · fleet + sponsor + aff *(also Phase 1 hub)*
73. **Homer, AK tides** — NOAA `9455558` (Homer, Coal Point, Kachemak Bay, 9.0km) · current `COI0421` (9.5km) · sponsor + aff *(also Phase 1 hub)*
74. **Seward, AK tides** — NOAA `9455090` (Seward, Resurrection Bay, 1.9km) · sponsor + aff *(also Phase 1 hub)*
75. **Valdez, AK tides** — NOAA `9454240` (VALDEZ, Port Valdez, 1.0km) · current `PWS0746` (1.4km) · fleet + sponsor + aff *(also Phase 1 hub)*
76. **Cordova, AK tides** — NOAA `9454050` (CORDOVA, 1.7km) · current `PWS0734` (3.3km) · sponsor + aff
77. **Whittier, AK tides** — NOAA `9454949` (Whittier, Passage Canal, 1.2km) · current `PWS0703` (18.0km) · sponsor + aff
78. **Anchor Point, AK tides** — NOAA `9455606` (Anchor Point, 2.1km) · current `COI1203` (11.9km) · sponsor + aff
79. **Chenega Bay, AK tides** — NOAA `9454764` (Sawmill Bay, Evans Island, 3.4km) · current `PWS0715` (2.1km) · sponsor + aff
80. **Halibut Cove, AK tides** — NOAA `9455556` (Halibut Cove, Kachemak Bay, 0.3km) · current `COI0422` (8.2km) · sponsor + aff
81. **Kenai / City Dock, AK tides** — NOAA `9455742` (Kenai City Pier, 2.4km) · current `PCT5016` (1.5km) · sponsor + aff
82. **Nikiski, AK tides** — NOAA `9455760` (NIKISKI, 0.1km) · current `COI0801` (0.4km) · sponsor + aff
83. **Ninilchik, AK tides** — NOAA `9455653` (Ninilchik, 1.0km) · current `PCT4976` (17.5km) · sponsor + aff
84. **Port MacKenzie, AK tides** — NOAA `9455934` (Port MacKenzie, 0.1km) · current `COI0211` (0.1km) · sponsor + aff
85. **Seldovia, AK tides** — NOAA `9455500` (SELDOVIA, Kachemak Bay, 0.5km) · current `COI0513` (5.5km) · sponsor + aff
86. **Tatitlek, AK tides** — NOAA `9454374` (Busby Island, 6.7km) · current `PWS0738` (6.6km) · sponsor + aff

---

## Phase 5 — Southcentral harbors & fleet hubs

87. **Anchorage / Ship Creek small-boat & Port of Alaska link hub** — official port pages · fleet + sponsor
88. **Seward harbor & boat harbor directory** — city/port official · sponsor
89. **Homer harbor directory** — city official · sponsor
90. **Whittier harbor / tunnel timing notes (links only)** — official · sponsor
91. **Valdez harbor & Port of Valdez hub** — official · fleet
92. **Cook Inlet commercial traffic / weather brief (links)** — NWS + NOAA · fleet
93. **Prince William Sound ports overview** — Valdez/Cordova/Whittier cross-links · fleet

---

## Phase 6 — Kodiak Island port communities

Own region per product plan. Includes city harbors and village ports (Port Lions, Ouzinkie, Old Harbor, Larsen Bay, Akhiok, Karluk, Alitak). Kodiak itself is also a Phase 1 hub.

94. **Kodiak, AK tides** — NOAA `9457261` (Kodiak, Port of Kodiak, 1.4km) · current `KOD0903` (0.8km) · fleet + sponsor + aff *(also Phase 1 hub)*
95. **Akhiok, AK tides** — NOAA `9457773` (Moser Bay (Trap Point), 6.4km) · current `KOD0918` (21.8km) · sponsor + aff
96. **Alitak / Lazy Bay, AK tides** — NOAA `9457804` (Alitak, Lazy Bay, 0.0km) · current `KOD0918` (16.6km) · sponsor + aff
97. **Karluk, AK tides** — NOAA `9457724` (Larsen Bay, 28.1km) · current `KOD0922` (25.3km) · sponsor + aff
98. **Larsen Bay, AK tides** — NOAA `9457724` (Larsen Bay, 1.0km) · current `KOD0924` (0.6km) · sponsor + aff
99. **Old Harbor, AK tides** — NOAA `9457527` (Old Harbor, 0.0km) · current `KOD0912` (3.0km) · sponsor + aff
100. **Ouzinkie, AK tides** — NOAA `9457287` (Ouzinkie, Spruce Island, 0.3km) · current `KOD0933` (1.9km) · sponsor + aff
101. **Port Lions, AK tides** — NOAA `9457391` (Port Lions, AK, 1.1km) · current `KOD0932` (7.7km) · sponsor + aff

---

## Phase 7 — Kodiak harbor & shipyard directory

102. **Kodiak harbor & shipyard directory** — official city/port links · fleet + sponsor
103. **Kodiak Island village harbors shortlist** — Port Lions / Ouzinkie / Old Harbor / Larsen Bay / Akhiok · sponsor + commercial

---

## Phase 8 — Aleutian Chain & Alaska Peninsula ports

Own region per product plan. Full chain coverage: Unalaska/Dutch Harbor, Akutan, King Cove, Cold Bay, Sand Point, Adak, Atka, Nikolski, False Pass, Chignik, Perryville, Port Heiden, Nelson Lagoon. Dutch Harbor & Unalaska are also Phase 1 hubs.

104. **Dutch Harbor / Amaknak, AK tides** — NOAA `9462611` (Dutch Harbor, Amaknak Island, 0.4km) · current `UNI1015` (1.6km) · fleet + sponsor + aff *(also Phase 1 hub)*
105. ~~**Unalaska, AK tides** — NOAA `9462620` (Unalaska, 0.7km) · current `UNI1015` (0.7km) · fleet + sponsor + aff~~ *(shipped 2026-11-05; also Phase 1 hub)*
106. **Sand Point, AK tides** — NOAA `9459450` (SAND POINT, POPOF ISLAND, 1.0km) · current `PCT5406` (1.4km) · sponsor + aff
107. **King Cove, AK tides** — NOAA `9459881` (King Cove, 1.0km) · sponsor + aff
108. **Adak, AK tides** — NOAA `9461380` (Sweeper Cove, Kuluk Bay, Adak Island, 2.9km) · current `PCT5646` (19.0km) · sponsor + aff
109. **Akutan, AK tides** — NOAA `9462694` (Akutan, Akutan Island, 0.4km) · current `UNI1008` (6.1km) · sponsor + aff
110. **Cold Bay, AK tides** — NOAA `9459949` (Cold Bay, 2.9km) · current `PCT5431` (26.2km) · sponsor + aff
111. **Chignik, AK tides** — NOAA `9458917` (Chignik, Anchorage Bay, 0.9km) · sponsor + aff
112. **Atka, AK tides** — NOAA `9461710` (Atka, Nazan Bay, 4.4km) · sponsor + aff
113. **False Pass, AK tides** — NOAA `9462955` (False Pass, Isanotski Strait, 0.5km) · current `UNI1901` (1.6km) · sponsor + aff
114. **Nelson Lagoon, AK tides** — NOAA `9463502` (Port Moller, 39.0km) · current `PCT5761` (29.2km) · sponsor + aff
115. **Nikolski, AK tides** — NOAA `9462450` (Nikolski, 0.4km) · sponsor + aff
116. **Perryville, AK tides** — NOAA `9459085` (Chiachi Island (east side), 8.2km) · sponsor + aff
117. **Port Heiden, AK tides** — NOAA `9464075` (Meshik, Port Heiden, 5.4km) · current `PCT5771` (15.7km) · sponsor + aff

---

## Phase 9 — Aleutian / Peninsula fleet hubs

118. **Dutch Harbor / Unalaska port & services hub** — official city/port links · fleet
119. **Aleutian chain transit ports shortlist** — Adak / Unalaska / Sand Point / King Cove / Cold Bay · fleet
120. **Bering Sea weather & ice notice deep links** — NWS/NIC official · fleet

---

## Phase 10 — Bristol Bay & Pribilof Islands

121. **Naknek / Port of Bristol Bay, AK tides** — NOAA `9465203` (Naknek, Naknek River, 1.8km) · current `PCT5781` (4.7km) · sponsor + aff
122. **St. Paul Island, AK tides** — NOAA `9464212` (Village Cove, St. Paul Island, 1.1km) · current `PCT5861` (11.4km) · sponsor + aff
123. **Aleknagik, AK tides** — NOAA `9465374` (Snag Point, 27.7km) · sponsor + aff
124. **Clarks Point, AK tides** — NOAA `9465261` (Nushagak Bay (Clarks Point), 0.1km) · current `PCT5811` (2.6km) · sponsor + aff
125. **Dillingham, AK tides** — NOAA `9465374` (Snag Point, 0.6km) · current `PCT5811` (24.1km) · sponsor + aff
126. **Egegik, AK tides** — NOAA `9464874` (Egegik, Egegik River, 0.1km) · sponsor + aff
127. **King Salmon, AK tides** — NOAA `9465149` (King Salmon Airport, 1.9km) · current `PCT5781` (16.5km) · sponsor + aff
128. **St. George Island, AK tides** — NOAA `9463888` (St. George, St. George Island, 0.4km) · sponsor + aff
129. **Togiak, AK tides** — NOAA `9465182` (Black Rock, Walrus Islands, 40.8km) · sponsor + aff
130. **St. Marys, AK tides** — tide station **UNKNOWN** — verify before shipping · sponsor + aff

---

## Phase 11 — Bristol Bay season planning

131. **Bristol Bay season planning hub (tides + ADF&G/NMFS links)** — no invented openers · fleet + commercial

---

## Phase 12 — Arctic & Western Alaska

132. **Nome, AK tides** — NOAA `9468756` (NOME, 1.7km) · sponsor + aff
133. **Bethel, AK tides** — NOAA `9466477` (Bethel, 0.9km) · sponsor + aff
134. **Kotzebue, AK tides** — NOAA `9490424` (Kotzebue, 0.7km) · sponsor + aff
135. **Point Hope, AK tides** — NOAA `9491873` (Point Hope, 3.4km) · sponsor + aff
136. **Prudhoe Bay / Deadhorse, AK tides** — NOAA `9497645` (PRUDHOE BAY, 9.6km) · sponsor + aff
137. **Red Dog / Delong Terminal, AK tides** — NOAA `9491094` (Red Dog Dock, 0.4km) · sponsor + aff
138. **Unalakleet, AK tides** — NOAA `9468333` (Unalakleet, 0.2km) · sponsor + aff
139. **Utqiagvik (Barrow), AK tides** — NOAA `9494935` (Barrow Offshore, 8.0km) · sponsor + aff
140. **Wainwright, AK tides** — NOAA `9494212` (Wainwright, Chukchi Sea, 1.3km) · sponsor + aff

---

## Phase 13 — Arctic maritime ops

141. **Arctic maritime ops link hub** — USCG District 17 / NWS Arctic · fleet

---

## Phase 14 — Washington ports

142. **Seattle (Elliott Bay), WA tides** — NOAA `9447130` (SEATTLE (Madison St.), Elliott Bay, 0.5km) · current `PUG1506` (2.0km) · fleet + sponsor + aff *(also Phase 1 hub)*
143. **Tacoma (Commencement Bay), WA tides** — NOAA `9446484` (Tacoma, Commencement Bay, Sitcum Waterway, 0.5km) · current `PUG1521` (7.4km) · fleet + sponsor + aff *(also Phase 1 hub)*
144. **Everett, WA tides** — NOAA `9447659` (Everett, 1.6km) · current `PUG1613` (2.7km) · sponsor + aff
145. **Westport, WA tides** — NOAA `9441102` (Westport, Point Chehalis, 1.6km) · current `PCT1316` (2.7km) · sponsor + aff
146. **Port Angeles, WA tides** — NOAA `9444090` (Port Angeles, 0.8km) · current `PCT1371` (1.7km) · sponsor + aff
147. **Port Townsend, WA tides** — NOAA `9444900` (PORT TOWNSEND, 0.6km) · current `PCT1501` (0.7km) · sponsor + aff
148. **Bellingham, WA tides** — NOAA `9449211` (Bellingham, 1.2km) · current `PCT2116` (12.8km) · sponsor + aff
149. **Friday Harbor, WA tides** — NOAA `9449880` (Friday Harbor, San Juan Island, 1.0km) · current `PUG1745` (2.5km) · sponsor + aff
150. **Allyn, WA tides** — NOAA `9446281` (Allyn, Case Inlet, 0.3km) · current `PUG1548` (8.7km) · sponsor + aff
151. **Anacortes, WA tides** — NOAA `9448794` (Anacortes, Guemes Channel, 0.9km) · current `PUG1735` (1.8km) · sponsor + aff
152. **Bremerton, WA tides** — NOAA `9445958` (Bremerton, Sinclair Inlet, Port Orchard, 1.1km) · current `PUG1510` (1.7km) · sponsor + aff
153. **Brownsville, WA tides** — NOAA `9445832` (Brownsville, Port Orchard, 0.1km) · current `PCT1646` (2.7km) · sponsor + aff
154. **Camas-Washougal, WA tides** — NOAA `9440047` (Washougal, 2.5km) · sponsor + aff
155. **Chinook, WA tides** — NOAA `9440573` (Chinook, Baker Bay, Wash., 0.2km) · current `PCT1126` (2.5km) · sponsor + aff
156. **Coupeville, WA tides** — NOAA `9447929` (Coupeville, Penn Cove, Whidbey Island, 0.5km) · current `PUG1625` (6.1km) · sponsor + aff
157. **Dewatto, WA tides** — NOAA `9445388` (Ayock Point, 6.5km) · current `PCT1596` (9.4km) · sponsor + aff
158. **Edmonds, WA tides** — NOAA `9447427` (Edmonds, 0.4km) · current `PUG1503` (4.6km) · sponsor + aff
159. **Grapeview, WA tides** — NOAA `9446366` (Vaughn, Case Inlet, 5.8km) · current `PUG1548` (2.7km) · sponsor + aff
160. **Grays Harbor / Aberdeen, WA tides** — NOAA `9441187` (ABERDEEN, 2.6km) · current `PCT1306` (20.5km) · sponsor + aff
161. **Hoodsport, WA tides** — NOAA `9445478` (Union, 6.1km) · current `PCT1596` (16.2km) · sponsor + aff
162. **Illahee, WA tides** — NOAA `9445958` (Bremerton, Sinclair Inlet, Port Orchard, 4.3km) · current `PUG1514` (2.6km) · sponsor + aff
163. **Ilwaco, WA tides** — NOAA `9440597` (Ilwaco, Baker Bay, Wash., 0.5km) · current `PCT1116` (6.0km) · sponsor + aff
164. **Indianola, WA tides** — NOAA `9445683` (Port Jefferson, 3.6km) · current `PCT1636` (3.7km) · sponsor + aff
165. **Kalama, WA tides** — NOAA `9440357` (Temco Kalama Terminal, 2.4km) · current `PCT1251` (21.5km) · sponsor + aff
166. **Keyport, WA tides** — NOAA `9445719` (Poulsbo, Liberty Bay, 2.8km) · current `PUG1508` (0.6km) · sponsor + aff
167. **Kingston, WA tides** — NOAA `9445639` (Kingston, Appletree Cove, 0.4km) · current `PUG1503` (4.1km) · sponsor + aff
168. **La Push, WA tides** — NOAA `9442396` (La Push, Quillayute River, 0.5km) · current `PCT1321` (1.0km) · sponsor + aff
169. **Longview, WA tides** — NOAA `9440422` (Longview, 0.0km) · current `PCT1251` (8.1km) · sponsor + aff
170. **Lopez Island, WA tides** — NOAA `9449911` (Upright Head, Lopez Island, 6.0km) · current `PUG1746` (3.3km) · sponsor + aff
171. **Manchester, WA tides** — NOAA `9445938` (Clam Bay, Rich Passage, 0.3km) · current `PCT1701` (1.2km) · sponsor + aff
172. **Neah Bay, WA tides** — NOAA `9443090` (NEAH BAY, 1.7km) · current `PUG1642` (9.6km) · sponsor + aff
173. **Olympia (Budd Inlet), WA tides** — NOAA `9446969` (Olympia, Budd Inlet, 1.7km) · current `PUG1540` (10.7km) · sponsor + aff
174. **Orcas Island, WA tides** — NOAA `9449798` (Orcas, Orcas Island, 0.7km) · current `PUG1722` (1.8km) · sponsor + aff
175. **Peninsula / Nahcotta, WA tides** — NOAA `9440747` (Nahcotta, 0.6km) · current `PCT1271` (25.3km) · sponsor + aff
176. **Poulsbo, WA tides** — NOAA `9445719` (Poulsbo, Liberty Bay, 1.1km) · current `PUG1508` (3.3km) · sponsor + aff
177. **Ridgefield, WA tides** — NOAA `9438125` (Multnomah Channel, 6.4km) · sponsor + aff
178. **Shelton (Oakland Bay), WA tides** — NOAA `9446628` (Shelton, Oakland Bay, 1.3km) · current `PCT1896` (4.7km) · fleet + sponsor + aff
179. **Silverdale, WA tides** — NOAA `9445901` (Tracyton, Dyes Inlet, 4.6km) · current `PUG1601` (7.3km) · sponsor + aff
180. **Skagit / La Conner, WA tides** — NOAA `9448558` (La Conner, Swinomish Channel, 0.1km) · current `PUG1628` (6.2km) · sponsor + aff
181. **South Whidbey / Langley, WA tides** — NOAA `9447856` (Sandy Point, Whidbey Island, 2.2km) · current `PUG1618` (1.5km) · sponsor + aff
182. **Tracyton, WA tides** — NOAA `9445901` (Tracyton, Dyes Inlet, 0.7km) · current `PUG1510` (3.7km) · sponsor + aff
183. **Vancouver WA, WA tides** — NOAA `9440083` (Vancouver, 1.2km) · fleet + sponsor + aff
184. **Wahkiakum No. 1 / Cathlamet, WA tides** — NOAA `9439099` (Wauna, 5.1km) · current `PCT1216` (1.7km) · sponsor + aff
185. **Wahkiakum No. 2 / Puget Island, WA tides** — NOAA `9439099` (Wauna, 2.9km) · current `PCT1216` (3.5km) · sponsor + aff
186. **Waterman, WA tides** — NOAA `9445832` (Brownsville, Port Orchard, 2.6km) · current `PCT1646` (2.0km) · sponsor + aff
187. **Willapa Harbor / Raymond, WA tides** — NOAA `9440875` (South Bend, Willapa River, 4.7km) · current `PCT1271` (4.4km) · sponsor + aff

---

## Phase 15 — WA harbors & Puget Sound fleet

188. **WA harbors & fuel docks shortlist** — official marina/port pages · sponsor + aff
189. **Puget Sound fleet planning hub** — multi-station tide index · fleet
190. **Columbia River (WA) ports overview** — Vancouver/Longview/Kalama cross-links · fleet

---

## Phase 16 — Oregon Coast ports

191. **Astoria, OR tides** — NOAA `9439026` (Astoria (Youngs Bay), Oreg., 2.0km) · current `PCT1146` (3.2km) · sponsor + aff *(also Phase 1 hub)*
192. **Newport, OR tides** — NOAA `9435385` (YAQUINA USCG STA, NEWPORT, 1.2km) · current `PCT1081` (1.6km) · sponsor + aff *(also Phase 1 hub)*
193. **Coos Bay, OR tides** — NOAA `9432845` (Coos Bay, 1.6km) · current `PCT1061` (10.1km) · fleet + sponsor + aff *(also Phase 1 hub)*
194. **Brookings-Harbor, OR tides** — NOAA `9430104` (Brookings, Chetco Cove, 1.6km) · sponsor + aff
195. **Garibaldi, OR tides** — NOAA `9437540` (Garibaldi, 0.9km) · current `PCT1096` (2.1km) · sponsor + aff
196. **Bandon, OR tides** — NOAA `9432373` (Bandon, Coquille River, 0.2km) · current `PCT1056` (0.5km) · sponsor + aff
197. **Charleston (Coos Bay), OR tides** — NOAA `9432780` (CHARLESTON, 0.9km) · current `PCT1061` (1.9km) · fleet + sponsor + aff
198. **Coquille River / Myrtle Point, OR tides** — NOAA `9432436` (Rink Creek Entrance, Coquille River, 10.9km) · current `PCT1056` (23.6km) · sponsor + aff
199. **Depoe Bay, OR tides** — NOAA `9435827` (Depoe Bay, 0.3km) · current `PCT1081` (20.8km) · sponsor + aff
200. **Florence / Siuslaw, OR tides** — NOAA `9434032` (Florence, Siuslaw River, 0.2km) · current `PCT1071` (18.6km) · sponsor + aff
201. **Gold Beach, OR tides** — NOAA `9431011` (Gold Beach, Rogue River, 0.2km) · sponsor + aff
202. **Nehalem, OR tides** — NOAA `9437908` (Nehalem, 0.6km) · current `PCT1096` (17.3km) · sponsor + aff
203. **Port Orford, OR tides** — NOAA `9431647` (Port Orford, 0.2km) · sponsor + aff
204. **Reedsport / Umpqua, OR tides** — NOAA `9433501` (Reedsport, 0.7km) · current `PCT1066` (8.2km) · sponsor + aff
205. **Tillamook Bay (POTB), OR tides** — NOAA `9437331` (Tillamook, Hoquarten Slough, 0.4km) · current `PCT1096` (13.3km) · sponsor + aff
206. **Toledo, OR tides** — NOAA `9435362` (TOLEDO, 0.5km) · current `PCT1091` (2.3km) · sponsor + aff
207. **Waldport / Alsea, OR tides** — NOAA `9434939` (Waldport, Alsea Bay, 1.1km) · current `PCT1086` (20.0km) · sponsor + aff

---

## Phase 17 — Oregon Columbia River ports

208. **Cascade Locks, OR tides** — NOAA `9440079` (Beacon Rock State Park, 11.8km) · sponsor + aff
209. **Columbia County / St. Helens, OR tides** — NOAA `9439201` (Saint Helens, 0.7km) · current `PCT1251` (36.0km) · sponsor + aff
210. **Hood River, OR tides** — NOAA `9440079` (Beacon Rock State Park, 40.3km) · sponsor + aff
211. **Portland, OR tides** — NOAA `9439221` (Portland Morrison Street Bridge, 4.9km) · sponsor + aff
212. **The Dalles, OR tides** — NOAA `9440079` (Beacon Rock State Park, 65.0km) · sponsor + aff
213. **Arlington, OR tides** — tide station **UNKNOWN** — verify before shipping · sponsor + aff
214. **Boardman / Morrow, OR tides** — tide station **UNKNOWN** — verify before shipping · sponsor + aff
215. **Umatilla, OR tides** — tide station **UNKNOWN** — verify before shipping · sponsor + aff

---

## Phase 18 — OR harbors shortlist

216. **OR coast harbors & fuel shortlist** — official · sponsor + aff

---

## Phase 19 — California North Coast

217. **Eureka / Humboldt Bay, CA tides** — NOAA `9418801` (Eureka, 0.5km) · current `PCT1026` (2.0km) · sponsor + aff *(also Phase 1 hub)*
218. **Crescent City, CA tides** — NOAA `9419750` (CRESCENT CITY, 0.6km) · sponsor + aff
219. **Shelter Cove, CA tides** — NOAA `9418024` (Shelter Cove, 1.3km) · sponsor + aff
220. **Trinidad, CA tides** — NOAA `9419059` (Trinidad Harbor, 0.4km) · current `PCT1026` (29.4km) · sponsor + aff

---

## Phase 20 — California Central Coast / Bay Area

221. **San Francisco, CA tides** — NOAA `9414305` (San Francisco, North Point, Pier 41, 0.8km) · current `SFB1206` (0.7km) · fleet + sponsor + aff *(also Phase 1 hub)*
222. **Oakland, CA tides** — NOAA `9414764` (Oakland Inner Harbor, 0.2km) · current `SFB1214` (0.5km) · fleet + sponsor + aff *(also Phase 1 hub)*
223. **Monterey, CA tides** — NOAA `9413450` (MONTEREY, MONTEREY BAY, 0.4km) · current `PCT0156` (6.2km) · sponsor + aff
224. **Moss Landing, CA tides** — NOAA `9413617` (General Fish Company Pier, 0.3km) · current `PCT0156` (24.0km) · sponsor + aff
225. **Bodega Bay, CA tides** — NOAA `9415625` (Bodega Harbor entrance, 2.8km) · sponsor + aff
226. **Alameda, CA tides** — NOAA `9414750` (Alameda, 0.2km) · current `SFB1214` (2.6km) · sponsor + aff
227. **Benicia, CA tides** — NOAA `9415111` (Benicia, 2.6km) · current `PCT0741` (1.1km) · sponsor + aff
228. **Berkeley, CA tides** — NOAA `9414816` (Berkeley, 0.9km) · current `SFB1218` (2.6km) · sponsor + aff
229. **Fort Bragg / Noyo Harbor, CA tides** — NOAA `9417426` (NOYO HARBOR, 0.2km) · sponsor + aff
230. **Half Moon Bay / Pillar Point, CA tides** — NOAA `9414131` (Pillar Point Harbor, Half Moon Bay, 0.3km) · current `PCT0171` (8.0km) · sponsor + aff
231. **Pittsburg / Antioch, CA tides** — NOAA `9415096` (Pittsburg, New York Slough, 0.4km) · current `PCT0886` (1.2km) · sponsor + aff
232. **Point Arena / Arena Cove, CA tides** — NOAA `9416841` (ARENA COVE, 0.1km) · sponsor + aff
233. **Port Chicago / Suisun Bay, CA tides** — NOAA `9415144` (PORT CHICAGO, SUISUN BAY, 0.8km) · current `SFB1323` (1.1km) · sponsor + aff
234. **Redwood City, CA tides** — NOAA `9414523` (Redwood City, Wharf 5, 0.3km) · current `SFB1304` (2.5km) · sponsor + aff
235. **Richmond CA, CA tides** — NOAA `9414863` (Chevron Oil Company Pier, Richmond, 2.0km) · current `PCT0661` (1.5km) · sponsor + aff
236. **Santa Cruz, CA tides** — NOAA `9413745` (Santa Cruz, Monterey Bay, 1.5km) · current `PCT0161` (5.4km) · sponsor + aff
237. **Sausalito, CA tides** — NOAA `9414819` (Sausalito, Corps of Engineers Dock, 1.0km) · current `PCT0546` (2.9km) · sponsor + aff
238. **Tomales Bay / Marshall, CA tides** — NOAA `9415339` (Marshall, Tomales Bay, 0.3km) · current `PCT0736` (35.2km) · sponsor + aff
239. **Vallejo, CA tides** — NOAA `9415165` (Vallejo, Mare Island Strait, 1.3km) · current `SFB1317` (3.3km) · sponsor + aff

---

## Phase 21 — California South Coast

240. **San Diego, CA tides** — NOAA `9410170` (SAN DIEGO (Broadway), 0.2km) · current `PCT0076` (0.3km) · fleet + sponsor + aff *(also Phase 1 hub)*
241. **Los Angeles / San Pedro, CA tides** — NOAA `9410660` (LOS ANGELES (Outer Harbor), 2.2km) · current `lb0101` (8.0km) · fleet + sponsor + aff *(also Phase 1 hub)*
242. **Long Beach, CA tides** — NOAA `9410678` (Long Beach Fire Boat Pier, 0.7km) · current `lb0101` (4.8km) · fleet + sponsor + aff *(also Phase 1 hub)*
243. **Marina del Rey, CA tides** — NOAA `9410840` (Santa Monica, Municipal Pier, 5.9km) · current `lb0101` (37.6km) · sponsor + aff
244. **Santa Barbara, CA tides** — NOAA `9411340` (Santa Barbara, 0.1km) · sponsor + aff
245. **Dana Point, CA tides** — NOAA `9410580` (Newport Bay Entrance, Corona del Mar, 23.3km) · sponsor + aff
246. **Ventura, CA tides** — NOAA `9411189` (Ventura, 2.8km) · sponsor + aff
247. **Morro Bay, CA tides** — NOAA `9412110` (PORT SAN LUIS, 24.2km) · sponsor + aff
248. **Alamitos Bay / Seal Beach, CA tides** — NOAA `9410686` (Long Beach, Inner Harbor, 9.3km) · current `lb0101` (7.4km) · sponsor + aff
249. **Avalon (Catalina), CA tides** — NOAA `9410079` (Avalon, Santa Catalina Island, 0.2km) · sponsor + aff
250. **Channel Islands Harbor, CA tides** — NOAA `9411065` (Port Hueneme, 2.5km) · sponsor + aff
251. **Chula Vista, CA tides** — NOAA `9410135` (South San Diego Bay, 1.2km) · current `PCT0116` (3.5km) · sponsor + aff
252. **Huntington Harbour, CA tides** — NOAA `9410678` (Long Beach Fire Boat Pier, 13.8km) · current `lb0101` (10.9km) · sponsor + aff
253. **Mission Bay (San Diego), CA tides** — NOAA `9410196` (Mission Bay, Campland, 3.0km) · current `PCT0056` (6.8km) · fleet + sponsor + aff
254. **National City, CA tides** — NOAA `9410152` (National City, San Diego Bay, 0.6km) · current `PCT0111` (1.0km) · sponsor + aff
255. **Newport Beach / Balboa, CA tides** — NOAA `9410583` (Balboa Pier, Newport Beach, 2.5km) · current `lb0101` (27.2km) · sponsor + aff
256. **Oceanside, CA tides** — NOAA `9410230` (La Jolla (Scripps Institution Wharf), 40.4km) · sponsor + aff
257. **Port Hueneme, CA tides** — NOAA `9411065` (Port Hueneme, 0.7km) · sponsor + aff
258. **Port San Luis / Avila, CA tides** — NOAA `9412110` (PORT SAN LUIS, 0.8km) · sponsor + aff
259. **Redondo Beach, CA tides** — NOAA `9410738` (King Harbor, Santa Monica Bay, 0.3km) · current `lb0101` (23.9km) · sponsor + aff
260. **Santa Monica, CA tides** — NOAA `9410840` (Santa Monica, Municipal Pier, 0.0km) · sponsor + aff
261. **Two Harbors (Catalina), CA tides** — NOAA `9410092` (Catalina Harbor, Santa Catalina Island, 1.0km) · sponsor + aff
262. **Wilmington CA, CA tides** — NOAA `9410680` (Long Beach, Terminal Island, 4.4km) · current `lb0101` (9.7km) · sponsor + aff

---

## Phase 22 — CA major ports fleet index

263. **CA major ports fleet index** — LA/LB/Oakland/SF/SD cross-links · fleet

---

## Phase 23 — British Columbia (CHS IWLS / tides.gc.ca)

Use CHS IWLS station codes (verified 2026-11-05 via `api-iwls.dfo-mpo.gc.ca`).
Do **not** use NOAA for these pages. Cite tides.gc.ca / DFO; build a BC generator later.

---

## Phase 23a — BC South Coast & Vancouver Island

264. **Vancouver, BC tides** — CHS `07735` (Vancouver, 0.9km) · fleet + sponsor + aff *(also Phase 1 hub)*
265. **Victoria, BC tides** — CHS `07120` (Victoria Harbour, 0.3km) · sponsor + aff *(also Phase 1 hub)*
266. **Nanaimo, BC tides** — CHS `07917` (Nanaimo Harbour, 1.2km) · sponsor + aff
267. **Tofino, BC tides** — CHS `08615` (Tofino, 0.5km) · sponsor + aff
268. **Campbell River, BC tides** — CHS `08074` (Campbell River, 1.0km) · sponsor + aff
269. **Bamfield, BC tides** — CHS `08545` (Bamfield, 0.0km) · sponsor + aff
270. **Chemainus, BC tides** — CHS `07455` (Chemainus, 0.4km) · sponsor + aff
271. **Comox, BC tides** — CHS `07965` (Comox, 0.3km) · sponsor + aff
272. **Courtenay, BC tides** — CHS `07965` (Comox, 5.2km) · sponsor + aff
273. **Cowichan Bay, BC tides** — CHS `07310` (Cowichan Bay, 0.1km) · sponsor + aff
274. **Crofton, BC tides** — CHS `07450` (Crofton, 0.5km) · sponsor + aff
275. **False Creek (Vancouver), BC tides** — CHS `07707` (Kitsilano, 0.7km) · fleet + sponsor + aff
276. **Fanny Bay, BC tides** — CHS `07955` (Denman Island, 4.9km) · sponsor + aff
277. **Fulford Harbour (Salt Spring), BC tides** — CHS `07330` (Fulford Harbour, 0.1km) · sponsor + aff
278. **Gibsons, BC tides** — CHS `07820` (Gibsons, 0.2km) · sponsor + aff
279. **Ladner / Delta, BC tides** — CHS `07609` (Deas Basin, 3.8km) · sponsor + aff
280. **Ladysmith, BC tides** — CHS `07460` (Ladysmith, 0.7km) · sponsor + aff
281. **Lund, BC tides** — CHS `07885` (Lund, 0.5km) · sponsor + aff
282. **Port Alberni, BC tides** — CHS `08575` (Port Alberni, 1.1km) · sponsor + aff
283. **Powell River, BC tides** — CHS `07880` (Powell River, 4.0km) · sponsor + aff
284. **Sechelt / Secret Cove, BC tides** — CHS `07830` (Halfmoon Bay, 4.4km) · sponsor + aff
285. **Sidney, BC tides** — CHS `07260` (Sidney, 0.5km) · sponsor + aff
286. **Sooke, BC tides** — CHS `07020` (Sooke, 0.7km) · sponsor + aff
287. **Squamish, BC tides** — CHS `07811` (Squamish Inner, 0.7km) · sponsor + aff
288. **Steveston / Richmond, BC tides** — CHS `07607` (Steveston, 0.5km) · sponsor + aff
289. **Tsehum / Shoal Harbour, BC tides** — CHS `07270` (Swartz Bay, 2.2km) · sponsor + aff
290. **Ucluelet, BC tides** — CHS `08595` (Ucluelet, 0.8km) · sponsor + aff
291. **Vesuvius Bay, BC tides** — CHS `07450` (Crofton, 5.1km) · sponsor + aff

---

## Phase 23b — BC Central Coast & North Island

292. **Port Hardy, BC tides** — CHS `08408` (Port Hardy, 0.6km) · sponsor + aff
293. **Alert Bay, BC tides** — CHS `08280` (Alert Bay, 0.0km) · sponsor + aff
294. **Bella Bella, BC tides** — CHS `08976` (Bella Bella, 0.1km) · sponsor + aff
295. **Bella Coola, BC tides** — CHS `08937` (Bella Coola, 2.5km) · sponsor + aff
296. **Klemtu, BC tides** — CHS `09035` (Klemtu, 0.1km) · sponsor + aff
297. **Port Alice, BC tides** — CHS `08751` (Port Alice South, 1.7km) · sponsor + aff
298. **Port McNeill, BC tides** — CHS `08290` (Port McNeill, 0.9km) · sponsor + aff

---

## Phase 23c — BC North Coast & Haida Gwaii

299. **Prince Rupert, BC tides** — CHS `09354` (Prince Rupert, 0.3km) · fleet + sponsor + aff *(also Phase 1 hub)*
300. **Kitimat, BC tides** — CHS `09140` (Kitimat, 1.3km) · fleet + sponsor + aff
301. **Stewart, BC tides** — CHS `09475` (Stewart, 2.7km) · sponsor + aff
302. **Masset, BC tides** — CHS `09910` (Masset, 0.6km) · sponsor + aff
303. **Daajing Giids (Queen Charlotte), BC tides** — CHS `09850` (Daajing Giids, 0.4km) · sponsor + aff
304. **Hartley Bay, BC tides** — CHS `09130` (Hartley Bay, 0.2km) · sponsor + aff
305. **Kitkatla, BC tides** — CHS `09242` (Kitkatla, 4.8km) · sponsor + aff
306. **Oona River, BC tides** — CHS `09250` (Seabreeze Point, 5.6km) · sponsor + aff
307. **Port Edward, BC tides** — CHS `09342` (Port Edward, 0.4km) · sponsor + aff
308. **Sandspit, BC tides** — CHS `09808` (Shingle Bay, 0.5km) · sponsor + aff
309. **Skidegate, BC tides** — CHS `09850` (Daajing Giids, 5.5km) · sponsor + aff

---

## Phase 24 — BC harbors & Inside Passage

310. **BC Inside Passage fleet planning hub** — multi-station CHS index · fleet
311. **BC harbors & fuel docks shortlist** — published port authority / DFO SCH pages · sponsor + fleet

---

## Phase 25 — Cross-coast commercial / fleet products (revenue scale)

312. **West Coast company-vessel port checklist template** — links to customs/port pages · fleet
313. **Multi-port tide week planner (AK→CA→BC)** — static table from ports.csv stations · fleet
314. **Affiliate gear hub — foul weather, PFDs, electronics** — Amazon/West Marine style · aff
315. **Marine insurance / surveyor directory (links only)** — published listings · fleet + sponsor
316. **Ship chandler & provisioning shortlist by region** — published · fleet + sponsor

---

## Notes for nightly ship

- Prefer Phase 1 hub tide pages early (Dutch Harbor, Kodiak, Anchorage, Seattle,
  major CA/OR). Then fill regional phases; interleave harbor/fleet pages (Phases
  3/5/7/9/…) once traffic exists.
- Never invent heights, openers, bag limits, harbor fees, or station IDs — link
  official pages. If `ports.csv` says `UNKNOWN`, research before shipping.
- Monetization: soft affiliate on gear/safety pages; local sponsor blocks only after
  the page is live and pitches are user-approved; fleet hubs are B2B lead pages.
- BC pages need a separate CHS fetch path; do not force NOAA station ids onto BC.
- Source lists used for `ports.csv`: Alaska DOT&PF Harbors (May 2018); Washington
  Public Ports Association; Oregon Public Ports Association / Blue Book; California
  coastal public harbors (Coast Pilot / harbor districts / CAHBMPC); DFO Small Craft
  Harbours & major BC port authorities. Matched to NOAA CO-OPS / CHS IWLS by
  haversine nearest station (tide ≤80 km, current ≤40 km).


- 2026-11-06 nightly: no new port shipped — Seward draft (/workspace/se-alaska-tides-drafts/seward/) still awaiting Jason OK via Mogul. Refreshed live pages instead: 8-day NOAA tide tables from Nov 7, latest NWS zone forecasts (PKZ034/738/771), NDBC obs (CDEA2, DPXA2; KDAA2 realtime file 404). Script: tools/refresh_live_pages.py.
- 2026-11-07 nightly: no new tide-port shipped — Seward draft still awaiting Jason OK via Mogul (Anchorage and seafood-processor pack remain draft/hold). Added live-ports harbor/fuel/haul-out directory; deepened Kodiak/Petersburg/Dutch Harbor/Unalaska ashore listings (hospital, grocery, pharmacy, USPS, airports) from official sources; added Petersburg FAA PAPG webcam; added published harbormaster emails; refreshed NOAA tide tables and NWS/NDBC weather on all four live port pages.
- 2026-11-08 nightly: shipped Homer, AK tides (NOAA 9455558, Coal Point / Kachemak Bay) at pages/homer-tides.html — NWS PKZ741 Kachemak Bay + PKZ742 Cook Inlet Kalgin Island to Point Bede, NDBC HMSA2/46108/FILA2, three free webcam links, five news links, 45 verified directory rows (incl. 4 seafood processors/buyers), Historic+Current photo strip (USFWS 1964 PD + CC BY 2.0 2011) and three original Homer SVGs. Homer added to harbor/fuel/haul-out directory and cross-port links. refresh_live_pages.py now supports multi-zone/multi-buoy ports and includes Homer; Kodiak gained KGXA2 (Gull Island) obs since KDAA2 has no met data. Seward, Anchorage, and seafood-processor pack remain draft/hold (not pushed).
- Next up (near-term order): Seward (draft awaiting Jason OK) → Whittier/Valdez → Anchorage (draft awaiting Jason OK). Without approvals, next fresh build candidate is Valdez (NOAA 9454240) or Whittier.
