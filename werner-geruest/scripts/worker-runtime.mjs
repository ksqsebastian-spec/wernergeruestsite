const SECURITY={'X-Content-Type-Options':'nosniff','Referrer-Policy':'strict-origin-when-cross-origin','Permissions-Policy':'camera=(), microphone=(), geolocation=()','X-Robots-Tag':'noindex, nofollow','Content-Security-Policy':"default-src 'self'; img-src 'self'; media-src 'self'; style-src 'self'; script-src 'self'; font-src 'self'; connect-src 'self'; object-src 'none'; base-uri 'self'; frame-ancestors 'none'; form-action 'none'"};
export default{async fetch(request,env){
 if(!['GET','HEAD'].includes(request.method))return new Response('Method not allowed',{status:405,headers:{...SECURITY,Allow:'GET, HEAD'}});
 const url=new URL(request.url);let path;try{path=decodeURIComponent(url.pathname);}catch{return new Response('Ungültige Adresse',{status:400,headers:SECURITY});}
 if(/^\/assets\/(?:images\/[a-f0-9]{12}(?:-thumb)?\.webp|video\/(?:hero|film)\.mp4)$/.test(path)){
  const response=await env.ASSETS.fetch(new Request(url.origin+path,{method:request.method,headers:request.headers}));const headers=new Headers(response.headers);for(const [key,value]of Object.entries(SECURITY))headers.set(key,value);
  if(path.endsWith('.mp4')){
   headers.set('Accept-Ranges','bytes');headers.set('Cache-Control','public, max-age=86400');
   const range=request.headers.get('Range'),validator=request.headers.get('If-Range');
   // The assets binding can return a full 200 body for a byte-range request.
   // Both films are bounded below 13 MB; slice that cached body only when needed.
   if(request.method==='GET'&&range&&response.status===200&&(!validator||validator===headers.get('ETag'))){
    const bytes=new Uint8Array(await response.arrayBuffer()),size=bytes.byteLength,m=/^bytes=(\d*)-(\d*)$/.exec(range);let start,end;
    if(m&&(m[1]||m[2])){if(m[1]){start=Number(m[1]);end=m[2]?Math.min(Number(m[2]),size-1):size-1;}else{start=Math.max(0,size-Number(m[2]));end=size-1;}}
    if(!Number.isSafeInteger(start)||!Number.isSafeInteger(end)||start<0||start>=size||end<start){headers.set('Content-Range','bytes */'+size);headers.delete('Content-Length');return new Response(null,{status:416,headers});}
    headers.set('Content-Range',`bytes ${start}-${end}/${size}`);headers.set('Content-Length',String(end-start+1));return new Response(bytes.subarray(start,end+1),{status:206,headers});
   }
  }
  return new Response(request.method==='HEAD'?null:response.body,{status:response.status,headers});
 }
 if(path==='/')path='/index.html';else if(!/\.[^/]+$/.test(path))path=path.replace(/\/$/,'')+'.html';const asset=STATIC[path];
 if(!asset)return new Response('Seite nicht gefunden',{status:404,headers:{...SECURITY,'Content-Type':'text/plain; charset=utf-8'}});
 const bytes=Uint8Array.from(atob(asset[1]),c=>c.charCodeAt(0));return new Response(request.method==='HEAD'?null:bytes,{headers:{...SECURITY,'Content-Type':asset[0],'Cache-Control':path.startsWith('/assets/')?'public, max-age=86400':'public, max-age=0, must-revalidate'}});
}};
