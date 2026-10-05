# Gestaltung und Prüfung — Werner Gerüstbau

Stand: 5. Oktober 2026.

## Richtung und Konzept

Das bestehende weiße Framework mit Instrument Serif, Manrope, unterstrichenen Kontakten und offenen Abschnitten wird fortgeführt. Der neue starke Kontrast ist der vollflächige Film. Konzept in `design/concept.png`: drei zusammenhängende Ansichten für Film, Editorial-Einstieg und Fotoarchiv. Produktionsbilder, Film und Logo stammen aus der bestehenden Unternehmenswebsite. Das Konzept wird nicht als UI-Grafik ausgeliefert.

Tatsächliche Mobbin-Suche und Referenzen sind in `research/STRATEGIE-UND-VALUE-EQUATION.md` dokumentiert.

## Vergleich mit dem Konzept

Konzept und Browseraufnahme wurden im selben Prüfpass mit `view_image` betrachtet. Das Konzept ist ein langer Überblick mit 945 Pixel Breite; die Umsetzung wurde abschnittsweise bei 1440×810 geprüft. Ein vorheriger Viewport von 1440×1000 lieferte in der IAB-Aufnahme nur 810 Pixel Höhe; deshalb erfolgte die visuelle Prüfung im nativen 810-Pixel-Fenster und die geometrische Prüfung zusätzlich bei 1000 Pixel Höhe.

| Vergleichspunkt | Konzept | Umsetzung / Entscheidung |
|---|---|---|
| Videofläche | Ohne Rahmen, über volle Breite | 1440 Pixel breit; 710 Pixel plus 100-Pixel-Header füllen die erste 810-Pixel-Ansicht. Bei 1000 Pixel Höhe: 900-Pixel-Video. Auf Mobil: 390 Pixel breit, 728 Pixel plus 82-Pixel-Header. |
| Überschrift | Große weiße Serifenschrift links unten | Instrument Serif, 122 Pixel bei 1440 Pixel Breite; mobile zweizeilige Fortsetzung. Position und Hierarchie übernommen. |
| Videolesbarkeit | Dunkler Verlauf nur am unteren Rand | Untere Kante abgedunkelt, unveränderte Originaldatei. Bei der im Originalfilm enthaltenen Logo-Einblendung blendet die zusätzliche Überschrift kurz aus, damit beide Markenflächen nicht konkurrieren. |
| Header und Logo | Weiß, kleines Gold-Schwarz-Signet | Original-PNG unverändert, einschließlich seiner grauen Wortmarke; kein neu gezeichnetes Logo. Navigation und Bewerbung als schlichte Textlinks. |
| Weiße Einführung | Große Typografie, offene Fläche, drei Kontaktlinks | Reines Weiß #fff, Instrument/Manrope und sichtbare Telefonnummer, Anfrage und E-Mail. Keine neuen Statistik- oder Bewertungskarten. |
| Fotoarchiv | Große Aufnahmen in drei Spalten | Animierte Bildwand, drei Spalten auf Desktop, standardmäßig eine auf Mobil. Originalaufnahmen im Vordergrund; kleine Thumbnails ausschließlich im Viewer-Filmstreifen. |
| Projekttitel | Konzept enthält generierte Ortsbeispiele | Bewusste Korrektur: ausschließlich zugeordnete Namen aus der Quellwebsite. Kein generierter Projektname wird veröffentlicht. |
| Interface | Ruhige kleine Bedienelemente | Einheitliche Textsteuerung und dünne SVG-Symbole für Video. Keine Emojis, Merkliste oder Download-Button-Leiste. |

## Funktionsprüfung

- Lokaler Build und `npm run check` bestanden: Datenbestand, lokale Links, Syntax aller sechs Browser-Skripte, Worker-Routing und CSP.
- Desktop-Layout bei 1440×810 und geometrisch 1440×1000 geprüft; mobile Ansichten bei 390×810 und 320×740 ohne horizontales Überlaufen.
- Mobilmenü öffnet, navigiert zu Projekten und schließt. 320-Pixel-Ansicht zeigt große 280-Pixel-Porträts in einer Spalte.
- Industrie-Filter ergibt ein Projekt; Projektviewer enthält Eurogate mit zwei bzw. Berliner Tor mit vier Aufnahmen. Bildwechsel und Projektbezug zur Kontaktanfrage geprüft.
- Ein sehr schneller automatisierter Klick während Filter- und Scrollanimation traf ein darunter liegendes Leistungsdetail. Nach erneuter visueller Zustandsprüfung öffnete derselbe Projektlink korrekt. Kein wiederholter Blindklick; UI-Zustände werden bei der Prüfung abgewartet.
- Kontaktvorbereitung erzeugt `mailto:info@j-werner-geruestbau.de`, inklusive Projektname, mit sichtbarer Vorschau. Es wurde keine Nachricht gesendet.
- Drei tatsächliche Stellen und die veröffentlichte WhatsApp-Nummer auf der Karriereseite geprüft. Kein erfundener Stellenbestand.
- Originalvorschau: 1440×810, 17,2172 Sekunden. Vollständiger Film: 1152×648, 121,8 Sekunden. Videos bleiben unverändert; keine erfundene 4K-Datei.
- Lokale Videozeit bewegt sich bei Wiedergabe, Hero pausiert während des vollständigen Films; vollständiger Film spielt mit Ton und nativen Controls. Vollbildsteuerung nutzt Browser-/iOS-API; der IAB bildet den systemweiten Vollbildzustand nicht verlässlich als prüfbares DOM-Signal ab. Der Player selbst füllt auch dort den ganzen Viewport.
- Live: HTML, Karriere, Projektseiten, Logo, Fotos und beide MP4-Dateien mit 200 geprüft. Native Assets gaben zunächst ganze Dateien statt Teilbereichen zurück; der Worker ergänzt nun eine begrenzte Range-Auslieferung.
- Live-Range-Prüfung für beide Filme: Startbereich und Bereich ab Byte 1.000.000 liefern 206 und genau 1024 Byte; Bereiche hinter dem Dateiende liefern 416. Auch Suffixbereiche und `If-Range` sind lokal geprüft.

## Bewusste Grenzen

Keine unbelegten Google-Bewertungen, Jahreskennzahlen oder PQ-Nummer. Eignungsangaben stammen aus der Unternehmensquelle, aktuelle Dokumente werden angefordert. Mailversand läuft über das E-Mail-Programm des Besuchers; es gibt keinen simulierten Erfolg eines Backend-Versands. Vertrags-, Rechte- und Datenschutzangaben sind für den endgültigen Unternehmensstart abzustimmen, im Entwurf entsprechend eingeordnet.

Live-Schlussprüfung: Dach/Wetterschutz-Filter liefert zwei Maßnahmen; Karriereseite und Bewerbungsvorschau an die korrekte Werner-Adresse geprüft. Live-Konsole ohne Fehler oder Warnungen. Ton an/aus und Pause geprüft. Finaler Cloudflare-Deploy: `1fe5f1caf0c54dad9980276b8ddb278e`.
