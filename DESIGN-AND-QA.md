# Gestaltung und Prüfung

Stand: 5. Oktober 2026.

## Gestaltungsregeln

Weiß `#ffffff`, Schrift `#232923`, zurückhaltende Nebeninformationen `#73776f`, feine Linien `#dedfd9`. Instrument Serif für große Überschriften, Manrope für Navigation und Bedienung; beide lokal eingebunden. Breite 1280 px, große freie Flächen, unverzierte Links, keine dekorativen Emojis. Originales Mehlig-Logo und ausschließlich vorhandene Unternehmens-/Projektfotografie.

Mobbin wurde tatsächlich durchsucht und visuell ausgewertet:
- [Cosmos](https://mobbin.com/screens/88989e22-126c-49fc-aef2-f1012718995b): Bildwand und diskrete Bildverwaltung als Inspiration.
- [Savee](https://mobbin.com/screens/7354055f-058c-4122-a735-38f71a4b9053): Fotos als Hauptinhalt, leise Bedienung.

Moderne Interaktion konzentriert sich auf die Galerie. FLIP-Übergänge für Umordnung; Foto-Übergang in die Detailansicht, Filmstreifen, Zoom/Vollbild und mobile Wischgeste. Der Unternehmensrahmen bleibt ruhig. `prefers-reduced-motion` deaktiviert Bewegung.

## Konzeptvergleich

Drei ImageGen-Konzeptansichten wurden vor der Umsetzung erzeugt und visuell geprüft: Hero, Galerie sowie Leistungen/Unternehmen/Kontakt. Sie dienen als Layoutreferenz; keine daraus generierten Bilder erscheinen im Produkt. Hero-Konzept und Browserrender wurden im nativen Konzeptformat 1487 × 1058 verglichen. Die übrigen Konzepte sind Abschnittsansichten; der tatsächliche Inhalt kann aufgrund des vollständigen Portfolios und echten Teams höher ausfallen.

| Punkt | Umsetzung / bewusste Abweichung |
|---|---|
| Weißraum und Rahmen | Echter weißer Hintergrund, breiter Seitenrand und offene Struktur wie im Konzept. |
| Überschrift | Große Serifenschrift „Räume, nach Maß.“ links, sachlicher Introtext rechts. |
| Navigation | Kleine Textlinks rechts; originales Mehlig-Logo ergänzt die konzeptionelle Wortmarke. |
| Einstiegsfoto | Dasselbe echte Wiener-Café-Motiv, großzügig und ohne Textüberlagerung. Bildausschnitt aus dem Original statt generierter Rekonstruktion. |
| Kontakt | Telefon, Anfrage und E-Mail nebeneinander; mobil übersichtlich umgebrochen. |
| Galerie | Bildwand mit unterschiedlichen Proportionen und ruhiger Textbedienung. Projektbeschriftungen ergänzen das Konzept für nachvollziehbare Referenzen. |
| Unternehmen | Fünf genuine Porträts ersetzen Konzeptplatzhalter. Größer und mit echten Ansprechpartnern, Funktionen und Kontaktdaten. |
| Mobile | Eigener kompakter Header, native Kategorieauswahl, zweispaltige Galerie und vertikale Projektansicht; keine verkleinerte Desktop-Oberfläche. |

## Funktionale Prüfung

- 48 Projekte und 381 Projektbilder im Katalog; 767 verwendete Original-/Vorschaudateien und Porträts live mit HTTP 200 und `image/webp` geprüft.
- Große Einstiegsfotos 1400 px; Porträts 550 × 550 px aus der Quelle, keine künstliche Hochskalierung.
- Desktopfilter Hotels: acht Projekte. Unpassende Suche zeigt verständlichen Leerzustand; Zurücksetzen stellt Übersicht wieder her.
- Raster/Bildwand, variable Größe, weitere Projekte und Bildnavigation geprüft. Wiener Café hat sieben navigierbare Aufnahmen.
- Mobile Menünavigation klappt nach Auswahl zu; Seiten bei 390 und 320 px ohne horizontalen Überlauf.
- Kontakt- und Rückrufformular erzeugen korrekte `mailto:`-Nachrichten an `info@mehlig-gmbh.de`.
- Stellenwahl wird in die Bewerbung übernommen. Empfänger `b.koppe@mehlig-gmbh.de`; kein Versand ausgelöst.
- Worker: HTML-Routen, eigene Projektseiten, 404, HEAD, 405 für POST und Sicherheitsheader geprüft.
- Alle lokalen HTML-Verweise und JavaScript-Syntax geprüft; Browserkonsole ohne Fehler in den geprüften Abläufen.

## Offene Punkte für den Unternehmensstart

Aktualität der Stellen und Teamdaten, projektspezifische Fotorechte/Credits sowie endgültige Hosting-/Datenschutzangaben und Löschfristen. Automatischer Formularversand bleibt ein gesonderter Integrationsschritt. Die Website kennzeichnet die technischen Kontaktwege transparent.

## Größere Fotoansicht

Die Galerie startet mit drei Spalten auf großen Displays, zwei auf Tablets und einer auf Smartphones. Die großen Originaldateien werden direkt geladen. Das Einstiegsfoto ist auf Desktop bis zu 760 px und auf Mobilgeräten 380–440 px hoch. Die Bildgröße bleibt über den vorhandenen Regler anpassbar.
