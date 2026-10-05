from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import json,re,html
b=Path(__file__).resolve().parents[1];pages=json.loads((b/'research/pages.json').read_text());assets={a['url']:a for a in json.loads((b/'research/images.json').read_text())}
labels={'private':'Privat','hotels':'Hotels','gastro':'Gastronomie','work':'Arbeitswelten'}
categories={}
for prefix,cat in [('54/','gastro'),('59/','hotels'),('56/','work'),('55/','private')]:
 for p in pages:
  if urlparse(p['url']).path.lstrip('/').startswith(prefix):
   for link in p['links']:categories[link]=cat
covers={'p87':'7fa0fc3cd2b0','p96':'01c541826b36','p89':'d2f6f18cc646','p74':'086a31df935a','p30':'ae4956b053f6','p90':'7e2787d46ad7','p34':'a5ccdf080b4','p29':'168ab82e1dc1','p48':'d990d17076c5','p86':'946d70176bae','p78':'c2d9eb948fce','p37':'ca6863b6be99'}
priority=['p87','p96','p89','p74','p30','p90','p34','p29','p48','p86','p78','p37','p33','p36','p80','p91','p35','p50']
projects=[]
for p in pages:
 if not p['gallery']:continue
 number=urlparse(p['url']).path.strip('/').split('/')[0];pid='p'+number;fields={}
 for line in p['text'].splitlines():
  for key in ['Aufgabe','Planung','Bauherr']:
   if line.startswith(key+':'):fields[key]=line.split(':',1)[1].strip()
 images=[assets[u] for u in p['gallery']];cat=categories.get(p['url'],'private');title=p['headings'][0].replace(' - ',' – ')
 if pid=='p96':title='Privater Innenausbau · Lüneburg'
 if pid=='p87':title='Wiener Café · Hamburg'
 cover=next((a for a in images if covers.get(pid) in a['path']),images[0]) if covers.get(pid) else images[0]
 task=fields.get('Aufgabe','Ladeneinrichtung' if pid=='p93' else 'Inneneinrichtung')
 if pid=='p31':task='Einrichtung der Hotellobby'
 planner='' if pid=='p31' else fields.get('Planung','')
 projects.append({'id':pid,'title':title,'category':cat,'categoryLabel':labels[cat],'task':task,'planning':planner,'source':p['url'],'cover':cover,'images':images})
projects.sort(key=lambda p:priority.index(p['id']) if p['id'] in priority else 100)
people=[];s=BeautifulSoup((b/'research/source/39_team.html').read_text(),'html.parser')
for card in s.select('.card:has(h4)'):
 name=card.h4.get_text(' ',strip=True);img=card.find('img');ps=card.select('.card-text p');role=ps[0].get_text(' ',strip=True);a=card.select_one('a[href^="mailto:"]');phone=ps[1].get_text('\n',strip=True).splitlines()[0]
 people.append({'name':name,'role':role,'email':a.get_text(strip=True),'phone':phone,'image':assets['https://www.mehlig-gmbh.de/'+img['src']]['path']})
(b/'public/data').mkdir(exist_ok=True);(b/'public/data/projects.json').write_text(json.dumps(projects,ensure_ascii=False,separators=(',',':')));(b/'public/data/people.json').write_text(json.dumps(people,ensure_ascii=False,separators=(',',':')))
summary=f'''# Tischlerei Mehlig – Due Diligence

Stand: 5. Oktober 2026. Öffentliche Unternehmensquellen wurden live abgerufen. {len(pages)} Seiten, {len(projects)} Projektseiten mit {sum(len(p['images']) for p in projects)} Projektfotos sowie {len(assets)} eindeutige Bilddateien erfasst. Dies ist eine Bestandsaufnahme der veröffentlichten Angaben, keine Bestätigung interner Prozesse oder aktueller Verfügbarkeiten.

## Unternehmen und Kontakt

- Tischlerei Mehlig GmbH, Beesenweide 14, 25436 Moorrege. Die alte Website verwendet zusätzlich „Moorrege/Hamburg“.
- Telefon: 04122 85 94 3; Telefax: 04122 85 94 51; E-Mail: info@mehlig-gmbh.de.
- Geschäftsführer laut Impressum: Axel Seehafer.
- Handelsregister: Amtsgericht Elmshorn, HRB 1951. USt-ID: DE 812 901 145.
- Zuständige Kammer: Handwerkskammer Lübeck, Breite Straße 10/12, 23552 Lübeck.
- Zugehörigkeit zu GRUPPENWERK wird auf der bestehenden Website genannt.
- Originalquellen: [Kontakt](https://www.mehlig-gmbh.de/2/kontakt/), [Impressum](https://www.mehlig-gmbh.de/25/impressum/), [Team](https://www.mehlig-gmbh.de/39/team/).

## Leistungen und Arbeitsweise

Innenausbau, Objekteinrichtung und individueller Möbelbau, für private Immobilien, Büros, Hotels und Gastronomie. Die Kompetenzen-Seite nennt Inneneinrichtung, Ladenbau, Objekteinrichtung, Hotel/Gastronomie, Küchen, Türen und Einzelmöbel. Türen umfassen historische Stiltüren, moderne Elemente und Funktionstüren für Brand- und Schallschutz. Es werden Holz und Holzwerkstoffe, Stein, Metall, Leder, Mineralwerkstoffe, Stoffe und Kunststoffe verarbeitet. Die Website beschreibt Zusammenarbeit mit Auftraggebern, Architekten, Interior-Designern und einem festen Partnernetzwerk sowie die Möglichkeit, die Werkstatt zu besuchen. Diskretion und individuelle Abstimmung gehören zum veröffentlichten Selbstverständnis.

Quellen: [Startseite](https://www.mehlig-gmbh.de/), [Kompetenzen](https://www.mehlig-gmbh.de/28/kompetenzen/), [Referenzen](https://www.mehlig-gmbh.de/44/referenzen/).

## Ansprechpartner

| Name | Funktion | Telefon | E-Mail |
|---|---|---|---|
'''
for p in people:summary+=f"| {p['name']} | {p['role']} | {p['phone']} | {p['email']} |\n"
summary+='''
Zusätzliche veröffentlichte Mobilnummern: Ole Wiedenbeck 0174 18 24 767; Ole Bostelmann 0173 66 77 060. Die neue Website priorisiert die beruflichen Festnetz- und Mailkontakte.

## Karriere

Zwei auf der Website veröffentlichte Aufgaben, nicht erfunden:

1. **Projektleitung (m/w/d):** Kunden- und Architektenbetreuung, individuelle Lösungen, Kalkulation, Angebot, Termin-/Einsatzplanung, Kosten- und Qualitätssteuerung, Abrechnung und Prozessverbesserung/Digitalisierung. Meister-/Holztechniker- oder ähnliche Qualifikation, Erfahrung mit Innen-/Laden-/Objekt- oder Gastronomieeinrichtungen, Personalführung, Detailgenauigkeit und verbindliche Kommunikation. Die Anzeige nennt moderne Arbeitsmittel, eigenverantwortliches Arbeiten, Entwicklungsmöglichkeiten und ein kollegiales Team.
2. **Arbeitsvorbereitung und Auftragsabwicklung (m/w/d):** Kalkulation, Werkplanung, Fertigungs- und Montagekoordination. Meister-/Holztechnikerqualifikation, Berufserfahrung, Führerschein Klasse B, CNC- und EDV-Kenntnisse (AutoCAD, WoodWop, OSD, Outlook), Erfahrung mit Oberflächen und strukturierte Arbeitsweise. Die Anzeige nennt langfristige Beschäftigung und tarifliche Vergütung mit leistungsbezogenen Zulagen.

Bewerbung laut Quelle an **Bärbel Koppe, b.koppe@mehlig-gmbh.de**, mit Lebenslauf, Gehaltsvorstellung und frühestmöglichem Eintritt. Es gibt keine erkennbaren Ausschreibungsdaten; die tatsächliche Aktualität muss intern bestätigt werden.

Quellen: [Projektleitung](https://www.mehlig-gmbh.de/3/karriere/detail/65/wir-suchen-projektleiter-mwd.html), [Arbeitsvorbereitung](https://www.mehlig-gmbh.de/3/karriere/detail/353/mitarbeiter-mwd--fuer-die-arbeitsvorbereitung-und-auftragsabwicklung.html).

## Referenzen – vollständiges Inventar

Projektjahre, Budgets und messbare Ergebnisse sind in den ausgewerteten Projektseiten nicht angegeben. Die Tabelle gibt den veröffentlichten Leistungsumfang und die Planung wieder. Bauherr-Angaben werden wegen einzelner Widersprüche nicht für die neue Website übernommen.

| Projekt / Quelle | Bereich | veröffentlichte Aufgabe | Planung | Fotos |
|---|---|---|---|---:|
'''
for p in projects:summary+=f"| [{p['title']}]({p['source']}) | {p['categoryLabel']} | {p['task']} | {p['planning'] or 'nicht eindeutig belegt'} | {len(p['images'])} |\n"
summary+='''
## Bildquellen und Nachweise

Originalfotos wurden von der bestehenden Mehlig-Website übernommen, als WebP in hoher Auflösung erhalten und zusätzlich für Vorschaubilder optimiert. Keine generierten Projektbilder werden veröffentlicht. Bildquelle, Projektzuordnung und ursprüngliche Abmessungen stehen in `public/data/projects.json`. Das vollständige Bildquelleninventar steht in `research/image-inventory.json`.

Das bestehende Impressum nennt DuPont™ Corian® (Copyright DuPont), simon eymann | photography und simon eymann | kopterwork, zusätzlich gegebenenfalls direkt angegebene Quellen. Diese Angaben werden im neuen Impressum erhalten. Die Quelle belegt die Veröffentlichung, nicht pauschal weitergehende Nutzungsrechte.

[Referenzbroschüre, 9 Seiten](https://www.mehlig-gmbh.de/pic/upload/Referenzen_205x290.pdf): Grande Beach, Eggers, Sylc, Gut Kaden, Strandleben, The George, Apartment040, Gastwerkhotel, Balducci. Keine zusätzlichen Zertifizierungen oder verifizierten Qualitäts-Siegel wurden daraus abgeleitet.

## Offene Punkte und Widersprüche

- Teamseite: 35 Mitarbeitende; Karriereanzeigen: über 20. Kein Personalstand wird ungeprüft prominent beworben.
- Riverside Rechtsanwälte nennt auf der Projektseite „Sylc Appartmenthotel“ als Bauherr. Auffälliger möglicher Übertragungsfehler; nicht übernommen.
- Sylc: Broschüre nennt Lobby, Sicon GmbH und Windels Architekten; Website nennt Gesamteinrichtung, Sylc und Britta Müller-Kirchenbauer. Neue Website verwendet konservativ „Einrichtung der Hotellobby“ und lässt widersprüchliche Beteiligtenangaben weg.
- Gut Kaden: Bauherr in Broschüre und Projektseite unterschiedlich. Beteiligtenangaben intern prüfen.
- Datenschutz der alten Website beschreibt unter anderem externe Google-Schriften. Die neue Vorschau nutzt lokal gespeicherte Schriften, keine Analyse- oder Marketing-Cookies, keine externen Einbettungen und keinen automatischen Formularversand. Dafür ist eine eigene, zutreffende technische Beschreibung erforderlich.
- Alte Rechtsverweise (TMG) werden nicht ungeprüft als aktuelle Rechtsgrundlage wiederholt. Die Unternehmensstammdaten bleiben erhalten.
- Keine belegten Reaktionszeiten, Festpreise, garantierten Liefertermine, Projektjahre oder aktuellen Mitarbeiterzahlen erfinden.

## Abgerufene Seiten

'''
for p in pages:summary+=f"- [{p['title']}]({p['url']})\n"
(b/'MEHLIG-DUE-DILIGENCE.md').write_text(summary)
(b/'research/image-inventory.json').write_text(json.dumps(list(assets.values()),ensure_ascii=False,indent=2))
print('Catalog',len(projects),'projects',sum(len(p['images']) for p in projects),'photos',len(people),'people')
