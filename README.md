# Jagerfly

Et top-down skydespil til mobil og browser, hvor du flyver et F-35 og skyder med maskingevær og missiler. Lavet, så en 6-årig kan spille det. v1.2.

**Spil:** åbn `index.html`, eller slå GitHub Pages til (Settings → Pages → Branch `main`, mappe `/root`). På mobilen kan siden føjes til hjemmeskærmen og kører så i fuld skærm som en app.

## ## Indhold
- 14 baner, som alle kan vælges fra start (klarede baner får en stjerne). Hver bane har sit eget terræn og sin egen boss:

| # | Bane | Terræn | Boss |
|---|---|---|---|
| 1 | Kysten | Hav, øer og land | Bombefly |
| 2 | Ørkenen | Sand, oaser og kaktus | Kæmpekampvogn |
| 3 | Sneen | Fyrreskov og frosne søer | Kæmpehelikopter |
| 4 | Natten | Storm og regn over havet | Slagskib |
| 5 | Junglen | Regnskov og floder | Kæmpehelikopter |
| 6 | Ishavet | Isflager | Hangarskib (sender jagerfly ud) |
| 7 | Kløften | Røde klipper | Kæmpekampvogn |
| 8 | Byen | Gader og høje huse | Fæstning |
| 9 | Solnedgang | Varmt hav og palmeøer | Bombefly |
| 10 | Efteråret | Marker og gule træer | Kæmpehelikopter |
| 11 | Vulkanen | Aske og lava | Fæstning |
| 12 | Sumpen | Mudder og siv | Kæmpekampvogn |
| 13 | Oceanet | Åbent hav | Hangarskib |
| 14 | Finalen | Byen om natten | Kæmpebombefly |

- Fjender: jagerfly i formation og zigzag, helikoptere, kanonbåde og kampvogne; banerne bliver lidt sværere for hver
- Maskingeværet skyder, så længe fingeren er på skærmen. Missiler er ekstra: den gule knap sender to målsøgende missiler af sted
- Missiler fyldes op med missilkasser, som fjender taber, og der kommer altid et hjerte og en missilkasse lige før bossen
- Sværhedsgrad: Let (5 hjerter, 8 missiler, langsomme kugler) eller Normal (3 hjerter, 6 missiler)
- Lyd kan slås fra

## Styring
| Mobil | Tastatur | Handling |
|---|---|---|
| Sæt en finger på skærmen og træk | Pile · WASD | Flyt flyet |
| Fingeren er nede | Mellemrum · J | Skyd med maskingevær |
| Den gule MISSIL-knap | M · Shift | Send to missiler af sted |
| Pauseknappen | P · Esc | Pause |
| | F | Fuld skærm |

Filer
- `index.html` – hele spillet i én fil
- `manifest.webmanifest`, `icon-*.png`, `apple-touch-icon.png` – app-ikon og fuld skærm på mobil

## Udvikling
Kilden ligger i `src/game.html`. `python3 build.py` bygger `index.html` (GitHub-versionen) og artifakt-versionen ud fra den.

## Versioner
Hver udgave gemmes også som `versions/jagerfly-vX.Y.html`, og versionen står i titlen og på startskærmen.
