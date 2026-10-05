import {readFile,writeFile,readdir,mkdir,copyFile} from 'node:fs/promises';
import {extname} from 'node:path';
import {execFileSync} from 'node:child_process';
execFileSync('python3',['scripts/render.py']);
const types={'.html':'text/html; charset=utf-8','.css':'text/css; charset=utf-8','.js':'text/javascript; charset=utf-8','.json':'application/json; charset=utf-8','.svg':'image/svg+xml','.woff2':'font/woff2','.txt':'text/plain; charset=utf-8'};
const assets={};async function walk(dir){for(const f of await readdir(dir,{withFileTypes:true})){const file=dir+'/'+f.name;if(f.isDirectory()){if(file!=='public/assets/images')await walk(file);}else{const path=file.slice(6);assets[path]=[types[extname(file)]||'application/octet-stream',(await readFile(file)).toString('base64')];}}}await walk('public');
const runtime=await readFile('scripts/worker-runtime.mjs','utf8');await mkdir('dist',{recursive:true});await writeFile('dist/worker.mjs','const STATIC='+JSON.stringify(assets)+';\n'+runtime);
const projects=JSON.parse(await readFile('public/data/projects.json')),people=JSON.parse(await readFile('public/data/people.json'));const keys=new Set();for(const p of projects)for(const a of p.images){keys.add(a.path);keys.add(a.thumb);}for(const p of people)keys.add(p.image);
await mkdir('dist/photos/assets/images',{recursive:true});for(const key of keys)await copyFile('public'+key,'dist/photos'+key);await writeFile('dist/asset-keys.json',JSON.stringify([...keys].sort()));console.log(JSON.stringify({staticFiles:Object.keys(assets).length,workerBytes:(await readFile('dist/worker.mjs')).length,imageFiles:keys.size}));
