from pathlib import Path
import sys,re,subprocess,tempfile,json,zipfile
from playwright.sync_api import sync_playwright
R=Path(__file__).resolve().parent
G=['repartimos','clasificamos','comparamos']
if len(sys.argv)!=4:
 print('Uso: prueba_juego.py JUEGO ANCHO ALTO');sys.exit(2)
game=sys.argv[1];w=int(sys.argv[2]);h=int(sys.argv[3]);errors=[]
with sync_playwright() as pw:
 browser=pw.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'])
 page=browser.new_page(viewport={'width':w,'height':h},reduced_motion='reduce')
 page.set_default_timeout(2500)
 page.on('pageerror',lambda e:errors.append(str(e)))
 page.set_content((R/'juegos'/game/'index.html').read_text())
 if game=='repartimos':
  page.click('#startGame')
  for st in range(5):
   page.evaluate('locked=false')
   page.evaluate('''() => {for(let i=0;i<items.length;i++){if(items[i].at!==i)place(i,i)}}''')
   if st==2 and page.locator('#continue').is_hidden():page.evaluate('place(1,1)')
   assert page.locator('#continue').is_visible(),st
   page.click('#continue')
  assert page.locator('#end.active').count()==1
 elif game=='clasificamos':
  page.click('#start')
  for st in range(5):
   page.evaluate('''() => {const l=levels[level];for(const o of [...objects]){const d=l.mode==='match'?(o.color==='red'?0:null):(o.color==='red'?0:1);if(d!==null&&o.at!==d)moveObject(o.id,d)}}''')
   assert page.locator('#next').is_visible(),st
   page.click('#next')
  assert page.locator('#end.active').count()==1
 else:
  page.click('#start')
  for st in range(5):
   for j in range(page.evaluate('tasks[stage].length')):
    correct=page.evaluate('expected(current())')
    if st==1 and j==0:
     wrong='left' if correct!='left' else 'right';page.click('#'+wrong)
     assert page.locator('#next').is_hidden()
    if st==1 and j==1:
     page.click('#help');page.click('#help')
     assert page.locator('#pairing svg line').count()==2
    if st>=3:assert page.locator('#equal').is_visible()
    page.click('#'+correct)
    assert page.locator('#next').is_visible(),(st,j)
    page.click('#next')
  assert page.locator('#intro').is_visible()
  rec=page.evaluate('records');assert len(rec)==10
  assert rec[0]['independent']==False and rec[1]['independent']==False
  assert rec[2]['assisted']==True
  assert rec[7]['kind']=='equal' and rec[7]['independent']==True
 dims=page.evaluate('''() => ({sw:document.documentElement.scrollWidth,iw:innerWidth,sh:document.documentElement.scrollHeight,ih:innerHeight})''')
 assert dims['sw']<=dims['iw'],dims
 assert not errors,errors
 print('PASS',game,w,h,dims)
 browser.close()