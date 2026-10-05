(()=>{
const video=document.querySelector('#hero-video'),hero=document.querySelector('.film-hero'),toggle=document.querySelector('#hero-pause'),sound=document.querySelector('#hero-sound'),dialog=document.querySelector('#film-dialog'),film=document.querySelector('#full-film');if(!video)return;
const reduced=matchMedia('(prefers-reduced-motion: reduce)'),preview='/assets/video/hero.mp4';let userPaused=reduced.matches,resumeAfterFilm=false;
const playIcon='<path d="m9 6 9 6-9 6Z"/>',pauseIcon='<path d="M8 5v14m8-14v14"/>';
function state(){const paused=video.paused;toggle.querySelector('span').textContent=paused?'Abspielen':'Pause';toggle.setAttribute('aria-label',paused?'Video abspielen':'Video pausieren');toggle.querySelector('svg').innerHTML=paused?playIcon:pauseIcon;sound.querySelector('span').textContent=video.muted?'Ton aus':'Ton an';sound.setAttribute('aria-pressed',String(!video.muted));sound.querySelector('svg').innerHTML='<path d="M4 9h4l5-4v14l-5-4H4Z"/><path d="'+(video.muted?'M17 9l5 6m0-6-5 6':'M17 8q5 4 0 8m3-11q8 7 0 14')+'"/>';}
function prepare(){if(!video.getAttribute('src')){video.src=preview;video.load();}}
async function play(){prepare();try{await video.play();document.querySelector('#video-error').hidden=true;}catch{state();}}
video.addEventListener('timeupdate',()=>{hero.dataset.outro=String(Number.isFinite(video.duration)&&video.currentTime>=10);});
video.addEventListener('play',state);video.addEventListener('pause',state);video.addEventListener('volumechange',state);video.addEventListener('error',()=>{document.querySelector('#video-error').hidden=false;});
toggle.addEventListener('click',()=>{if(video.paused){userPaused=false;play();}else{userPaused=true;video.pause();}});
sound.addEventListener('click',()=>{video.muted=!video.muted;state();});
async function fullscreen(element,media){try{if(document.fullscreenElement)await document.exitFullscreen();else if(element.requestFullscreen)await element.requestFullscreen();else if(media.webkitEnterFullscreen)media.webkitEnterFullscreen();}catch{/* The film remains available at full viewport size. */}}
document.querySelector('#hero-fullscreen').addEventListener('click',()=>fullscreen(hero,video));
document.querySelector('#film-fullscreen').addEventListener('click',()=>fullscreen(dialog,film));
document.querySelector('#film-open').addEventListener('click',()=>{resumeAfterFilm=!video.paused;video.pause();if(!film.getAttribute('src'))film.src='/assets/video/film.mp4';dialog.showModal();film.play().catch(()=>{});});
dialog.querySelector('.film-close').addEventListener('click',()=>dialog.close());dialog.addEventListener('close',()=>{film.pause();if(document.fullscreenElement===dialog)document.exitFullscreen().catch(()=>{});if(resumeAfterFilm&&!userPaused&&!document.hidden)play();});film.addEventListener('error',()=>{document.querySelector('#full-film-error').hidden=false;});
new IntersectionObserver(entries=>{if(!entries[0].isIntersecting)video.pause();else if(!userPaused&&!document.hidden&&!dialog.open)play();},{threshold:.1}).observe(hero);
document.addEventListener('visibilitychange',()=>{if(document.hidden){video.pause();film.pause();}else if(!userPaused&&!dialog.open&&hero.getBoundingClientRect().bottom>0)play();});reduced.addEventListener('change',()=>{if(reduced.matches){userPaused=true;video.pause();}});
if(!reduced.matches)play();else state();
const comparison=document.querySelector('#comparison'),range=document.querySelector('#comparison-range');range?.addEventListener('input',()=>comparison.style.setProperty('--split',range.value+'%'));
})();
