from pathlib import Path
from urllib.parse import urljoin,urlparse
import requests,json,re,hashlib,concurrent.futures
from bs4 import BeautifulSoup
from PIL import Image,ImageOps
from io import BytesIO
B=Path(__file__).resolve().parents[1];R=B/'research';ROOT='https://www.j-werner-geruestbau.de/'
paths=['','privat','gewerbe','leistungen','referenzen','ueber-uns','kontakt','karriere','anfrage','impressum','datenschutz']
def get(path):
 u=urljoin(ROOT,path);r=requests.get(u,timeout=45);r.raise_for_status();r.encoding='utf-8';(R/'source'/((path or 'home')+'.html')).write_text(r.text);s=BeautifulSoup(r.text,'html.parser');states=[]
 for script in s.select('script'):
  t=script.string or script.get_text()
  try:d=json.loads(t)
  except:continue
  if isinstance(d,dict) and 'siteId' in d:states.append(d)
 images=[]
 for img in s.select('img[src]'):
  u=img['src'];m=re.search('/media/([^/]+)/(?:full|preview)',u)
  if m:u='https://onecdn.io/media/'+m[1]+'/full'
  images.append({'url':u,'alt':img.get('alt','')})
 for x in s.select('script,style,noscript,nav,header,footer'):x.decompose()
 return {'url':urljoin(ROOT,path),'path':path or 'home','text':s.get_text('\n',strip=True),'state':states,'images':images}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:pages=list(pool.map(get,paths))
(R/'pages.json').write_text(json.dumps(pages,ensure_ascii=False,indent=2));urls=list(dict.fromkeys(i['url'] for p in pages for i in p['images']));folder=B/'public/assets/images'
def download(u):
 try:
  r=requests.get(u,timeout=50);r.raise_for_status();im=ImageOps.exif_transpose(Image.open(BytesIO(r.content))).convert('RGB');w,h=im.size;key=hashlib.sha1(u.encode()).hexdigest()[:12];im.thumbnail((2400,2400));im.save(folder/(key+'.webp'),'WEBP',quality=90);im.thumbnail((800,1000));im.save(folder/(key+'-thumb.webp'),'WEBP',quality=85);return {'url':u,'path':'/assets/images/'+key+'.webp','thumb':'/assets/images/'+key+'-thumb.webp','width':w,'height':h}
 except Exception as err:return {'url':u,'error':str(err)}
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:images=list(pool.map(download,urls))
(R/'images.json').write_text(json.dumps(images,ensure_ascii=False,indent=2));print(json.dumps({'pages':len(pages),'images':len(images),'errors':[i for i in images if 'error'in i]}))
