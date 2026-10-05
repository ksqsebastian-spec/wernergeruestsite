# J. Werner Gerüstbau

Eigener Website-Entwurf in `werner-geruest/`, unabhängig von der Mehlig-Seite im Repository-Stamm.

Live: https://wernergeruesttest.ksqsebastian.workers.dev/

- Original-MP4 als vollflächiger, viewporthoher Einstieg. Stumme Vorschau, Pause, Ton und Vollbild; kompletter Film in bildschirmfüllendem Player mit nativer Steuerung.
- Eigene Cloudflare-Assets für 38 Bilder und zwei unveränderte Filme. Byte-Range-Auslieferung unterstützt Vorspulen.
- Ruhiges weißes Framework, lokale Instrument-Serif-/Manrope-Schriften und Original-PNG-Logo.
- Sechs belegte Projektmaßnahmen mit elf zugeordneten Aufnahmen, animierte Bildwand, Suche, Filter, Bildgröße, Viewer und eigene Projektseiten. Berliner Tor und dessen Wetterschutzdach gehören zur selben Maßnahme.
- Vorher/mit-Gerüst-Vergleich Wincklerstraße, neun Kernleistungen und Baustellenservice, Zielgruppen und Ablauf.
- Sieben reale Ansprechpartner, bestehende Eignungsangaben und drei tatsächliche Stellenangebote aus der Quellwebsite.
- Telefon und E-Mail direkt. Anfrage, Rückruf und Bewerbung bereiten Nachrichten im E-Mail-Programm vor. Die Website sendet oder speichert keine Formulardaten. WhatsApp auf der Karriereseite verwendet die veröffentlichte Werner-Nummer.
- Kein Tracking, keine Drittanbieter-Player oder extern geladenen Schriften. Vorschau ist `noindex`.

## Lokal

```sh
cd werner-geruest
npm run build
npm run check
npm run dev
```

Öffnen: http://127.0.0.1:4177/

`npm run build` rendert die HTML-Seiten aus dem vorhandenen Katalog und erstellt `dist/worker.mjs` und `dist/photos/`. Der Build benötigt keine heruntergeladenen Rohseiten. Er braucht Node und Python; die Website selbst hat keine Build-Abhängigkeiten.

## Daten & Recherche

- `research/WEBSITE-INVENTAR.md`: vollständige sichtbare Texte aller elf erfassten Quellseiten, Unternehmensdaten und offene Punkte.
- `research/STRATEGIE-UND-VALUE-EQUATION.md`: Zielgruppenpriorität, Hamburger/internationale Vergleichsunternehmen, Hormozi-Modell und tatsächlich abgerufene Mobbin-Referenzen.
- `research/MEDIEN-INVENTAR.json`: Originaladressen und lokale Bildzuordnung.
- `public/data/projects.json`, `people.json`, `company.json`: redaktionell kuratierte Daten.
- `design/concept.png`, `DESIGN-UND-QA.md`: Gestaltungsentscheidung und Validierung.

`collect.py` kann die öffentliche Quelle erneut erfassen; `catalog.py` bereitet deren Daten auf. Dazu werden Python `requests`, `beautifulsoup4` und Pillow benötigt. Rohes Website-HTML und serialisierte interne Seitenkonfiguration bleiben außerhalb von Git.

## Cloudflare

Worker: `wernergeruesttest`. Account: `25346b53f111266024f71046763f6aee`.

Konfiguration: `wrangler.jsonc`. Veröffentlicht über die autorisierte Cloudflare-API-Verbindung, mit eigenem Assets-Binding. Upload-Sessions sind kurzlebig und werden nicht im Repository gespeichert. Für CLI-Deployments mit vorhandenem Cloudflare-Zugang:

```sh
npm run build
npx wrangler deploy
```

Das untergeordnete Projekt verändert keine Mehlig-Routen und keinen Werner-Bau-Worker.
