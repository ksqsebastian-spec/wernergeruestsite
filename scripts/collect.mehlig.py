from pathlib import Path
from urllib.parse import urljoin,urlparse,urldefrag
import requests,re,json,hashlib,concurrent.futures
from bs4 import BeautifulSoup
from PIL import Image,ImageOps
from io import BytesIO
ROOT='https://www.mehlig-gmbh.de/'
BASE=Path(__file__).resolve().parents[1]
RAW=BASE/'research/source';RAW.mkdir(parents=True,exist_ok=True)
def canon(h):
 u=urldefrag(urljoin(ROOT,h.strip()))[0];p=urlparse(u)
 if p.hostname not in ('mehlig-gmbh.de','www.mehlig-gmbh.de'):return None
 if p.path=='/' or re.match(r'^/(?:de/)?\d+/',p.path):return ROOT+p.path.lstrip('/').removeprefix('de/')
def read(u):
 r=requests.get(u,timeout=35);r.raise_for_status();s=BeautifulSoup(r.text,'html.parser')
 links=list(dict.fromkeys(v for a in s.select('a[href]') if (v:=canon(a['href']))))
 imgs=list(dict.fromkeys(urljoin(ROOT,i['src'].strip()) for i in s.select('img[src]')))
 gallery=list(dict.fromkeys(urljoin(ROOT,i['src'].strip()) for i in s.select('[id^=galerie] img[src]')))
 heading=[x.get_text(' ',strip=True) for x in s.select('h1,h2,h3,h4')]
 for x in s.select('script,style,.navbar,.cookie-banner'):x.decompose()
 text=s.get_text('\n',strip=True)
 key=urlparse(u).path.strip('/').replace('/','_') or 'home';(RAW/(key+'.html')).write_text(r.text)
 return {'url':u,'title':s.title.get_text(strip=True) if s.title else '', 'headings':heading,'text':text,'links':links,'images':imgs,'gallery':gallery}
pages={};queue=[ROOT]
while queue and len(pages)<100:
 batch=queue[:8];queue=queue[8:]
 with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
  for result in ex.map(read,batch):
   pages[result['url']]=result
   for link in result['links']:
    if link not in pages and link not in queue and link not in batch:queue.append(link)
print('Pages',len(pages))
(BASE/'research/pages.json').write_text(json.dumps(list(pages.values()),ensure_ascii=False,indent=2))
assets=list(dict.fromkeys(x for p in pages.values() for x in p['images']))
folder=BASE/'public/assets/images';folder.mkdir(parents=True,exist_ok=True)
def image(u):
 name=hashlib.sha1(u.encode()).hexdigest()[:12];r=requests.get(u,timeout=35);r.raise_for_status()
 if urlparse(u).path.endswith('.svg'):
  path=BASE/'public/assets'/('logo.svg' if 'mehlig_logo' in u else name+'.svg');path.write_bytes(r.content);return {'url':u,'path':'/'+str(path.relative_to(BASE/'public')),'width':0,'height':0}
 im=ImageOps.exif_transpose(Image.open(BytesIO(r.content))).convert('RGB');w,h=im.size
 im.thumbnail((1800,1800));path=folder/(name+'.webp');im.save(path,'WEBP',quality=88,method=5)
 thumb=im.copy();thumb.thumbnail((700,900));thumb.save(folder/(name+'-thumb.webp'),'WEBP',quality=83,method=5)
 return {'url':u,'path':'/assets/images/'+name+'.webp','thumb':'/assets/images/'+name+'-thumb.webp','width':w,'height':h,'bytes':path.stat().st_size}
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:manifest=list(ex.map(image,assets))
(BASE/'research/images.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
print('Assets',len(manifest),'project pages',sum(bool(p['gallery']) for p in pages.values()),'image bytes',sum(i.get('bytes',0) for i in manifest))
for p in pages.values():print(p['url'],p['headings'][:2],len(p['gallery']))
