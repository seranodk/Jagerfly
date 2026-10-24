# Jagerfly

Et top-down skydespil til mobil og browser, hvor du flyver et F-35 og skyder med maskingevær eller missiler. Lavet, så en 6-årig kan spille det. v1.1.

**Spil:** åbn `index.html`, eller slå GitHub Pages til (Settings → Pages → Branch `main`, mappe `/root`). På mobilen kan siden føjes til hjemmeskærmen og kører så i fuld skærm som en app.

## Indhold
- 4 baner, som alle kan vælges fra start (klarede baner får en stjerne):
  1. **Kysten** – hav med øer og kanonbåde, så land med marker og kampvogne. Boss: bombefly
  2. **Ørkenen** – sand, klitter, oaser og kaktus. Boss: kæmpekampvogn med to tårne
  3. **Sneen** – fyrreskov, klipper og frosne søer. Boss: kæmpehelikopter med to rotorer
  4. **Natten** – storm og regn over havet. Boss: slagskib med tre kanontårne
- Fjender: jagerfly i formation, helikoptere, kanonbåde og kampvogne; banerne bliver lidt sværere for hver
- Efter en klaret bane kan man gå direkte videre til næste
- To våben: maskingevær (hurtigt) og missiler (finder selv målet)
- Hjerter i stedet for ét liv; fjender taber nogle gange et ekstra hjerte
- Sværhedsgrad: Let (5 hjerter, langsomme kugler) eller Normal (3 hjerter)
- Lyd kan slås fra

## Styring
| Mobil | Tastatur | Handling |
|---|---|---|
| Sæt en finger på skærmen og træk | Pile · WASD | Flyt flyet |
| Fingeren er nede | Mellemrum · J | Skyd |
| Knappen MASKINGEVÆR | 1 · Q | Vælg maskingevær |
| Knappen MISSIL | 2 · E | Vælg missil |
| Pauseknappen | P · Esc | Pause |
| | F | Fuld skærm |

## Filer
- `index.html` – hele spillet i én fil
- `manifest.webmanifest`, `icon-*.png`, `apple-touch-icon.png` – app-ikon og fuld skærm på mobil

## Udvikling
Kilden ligger i `src/game.html`. `python3 build.py` bygger `index.html` (GitHub-versionen) og artifakt-versionen ud fra den.

## Versioner
Hver udgave gemmes også som `versions/jagerfly-vX.Y.html`, og versionen står i titlen og på startskærmen.
