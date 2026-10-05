# Tischlerei Mehlig – Website-Entwurf

Live: https://mehligtest.ksqsebastian.workers.dev/

Eigenständiger Website-Entwurf für Tischlerei Mehlig GmbH im Repository `ksqsebastian-spec/wernergeruestsite`. Weißer, typografisch ruhiger Rahmen mit echten Projektfotos, animierter Galerie und persönlichen Kontaktwegen.

## Inhalt und Recherche

- [Due Diligence](MEHLIG-DUE-DILIGENCE.md): Unternehmensdaten, Leistungen, Ansprechpartner, Quellen, vollständige Projektübersicht und offene Fragen.
- [Zielgruppen und Value Equation](MEHLIG-ZIELGRUPPEN-VALUE-EQUATION.md): Positionierung, Hamburger und internationale Vergleichsfirmen, Hormozi-Modell und Mobbin-Referenzen.
- 48 echte Projekte, 381 Projektaufnahmen, fünf Ansprechpartner und zwei auf der bisherigen Website veröffentlichte Stellen.
- [Bildinventar](research/image-inventory.json): Herkunft und Maße der gesammelten Bilddateien.

Die ursprünglichen Bilder liegen als WebP in `public/assets/images`. Es werden keine generierten Projektfotos veröffentlicht. Unterschiedliche Aussagen der Quellen sind in der Recherche dokumentiert; ungesicherte Mitarbeiterzahlen, Projektjahre, Budgets und Zertifikate erscheinen nicht im Website-Text.

## Starten und bauen

Voraussetzungen: Node.js ab Version 20 und Python 3. Für normale Builds sind keine npm-Abhängigkeiten nötig.

```sh
npm run dev
npm run build
npm run check
```

Die lokale Vorschau läuft auf http://127.0.0.1:4176. `scripts/render.py` erzeugt Homepage, Karriere, rechtliche Seiten und alle Projektseiten aus den gespeicherten Katalogen. `scripts/build.mjs` erstellt den Worker sowie den tatsächlich verwendeten Foto-Bestand in `dist/photos`.

## Cloudflare

Worker: `mehligtest`; eigenes Deployment mit statischem Assets-Binding `ASSETS`. Unternehmensseiten, JavaScript, Schriften und Kataloge sind im Worker enthalten. 767 Bilddateien liegen in Cloudflare Workers Static Assets. Es gibt keine externe Bildabfrage im Browser und keinen KV-Speicher.

Mit einem für dieses Konto berechtigten Wrangler-Login bzw. API-Token:

```sh
npm run build
npm run check
npx wrangler@4 deploy
```

`wrangler.jsonc` enthält den Worker-Namen und die Asset-Konfiguration. Der erste Deploy wurde über die verbundene Cloudflare-API und einen kurzlebigen Asset-Upload-Token ausgeführt. Tokens werden nicht im Repository gespeichert. Für Direct Uploads stehen `scripts/asset-manifest.mjs` und `scripts/upload-assets.mjs` bereit; letzteres nimmt eine Upload-Session über stdin entgegen.

## Funktionen

- Galerie mit Kategorien, Suche, variablem Bildmaß, Bildwand/Raster und weiteren Projekten.
- Animierter Übergang in die Projektansicht, vollständige Fotoserie, Filmstreifen, Tastatursteuerung, Wischgeste, Zoom und Vollbild; reduzierte Bewegung wird berücksichtigt.
- Jede Referenz hat eine eigene, direkt aufrufbare Projektseite. Ohne JavaScript bleiben Projektlinks und direkte Kontaktwege nutzbar.
- Telefonnummer und E-Mail direkt sichtbar; Anfrage und Rückruf als E-Mail-Vorbereitung.
- Karriere mit zwei realen Stellen und einem einfachen Bewerbungsweg.
- Große echte Porträts mit Vergrößerung und individuellen Kontaktdaten.

Formulare speichern nichts auf dem Server. Die Nachricht wird durch den Besucher selbst im E-Mail-Programm versendet. Projektanfragen gehen an `info@mehlig-gmbh.de`, Bewerbungen an `b.koppe@mehlig-gmbh.de`. Ein automatischer Mailversand ist nicht angebunden.

## Prüfung und Grenzen

Alle lokalen Links, 48 Projektseiten, 381 Aufnahmen, 767 Live-Bilddateien und die Worker-Routen wurden geprüft. Browserprüfung auf 1487 × 1058, 390 × 844 und 320 × 740: Navigation, Filter, Suche/Leerzustand, Galerie, Kontakt/Rückruf und Stellenwahl/Bewerbung. Keine horizontalen Überläufe oder Konsolenfehler in den geprüften Ansichten. Es wurden keine E-Mails oder Bewerbungen versendet.

Dieser Deploy bleibt als Vorschau `noindex`. Vor dem endgültigen Unternehmensstart: Bildrechte/Credits je Aufnahme, Aktualität der Stellen und Ansprechpartner sowie Datenschutz-/Hostingverträge und Unternehmensprozesse bestätigen. Diese Punkte sind in der Due Diligence konkret aufgeführt.

Die Originalseite wird weder ersetzt noch verändert.

## Weitere eigenständige Website im Repository

[J. Werner Gerüstbau](werner-geruest/README.md): eigener Worker unter https://wernergeruesttest.ksqsebastian.workers.dev/, Originalfilm als vollflächiger Einstieg, Projektarchiv, Unternehmensdaten und Karriere. Lokal und Deployment aus dem Unterverzeichnis `werner-geruest/` starten.
