from pathlib import Path
from playwright.sync_api import sync_playwright
p=Path(__file__).parent
html=(p/'index.html').read_text()
with sync_playwright() as pw:
 browser=pw.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 for w,h in [(844,390),(390,844),(1280,800)]:
  page=browser.new_page(viewport={'width':w,'height':h},device_scale_factor=1)
  # local navigation is blocked in this environment: inject images as data URLs for screenshot validation
  import base64,re
  document=html
  for f in (p/'assets').iterdir():
   mime='image/jpeg' if f.suffix=='.jpg' else 'image/png'
   document=document.replace('assets/'+f.name,'data:'+mime+';base64,'+base64.b64encode(f.read_bytes()).decode())
  page.set_content(document,wait_until='load')
  page.screenshot(path=str(p/f'captura-{w}x{h}.png'),full_page=True)
  dims=page.evaluate('''() => ({scroll:document.documentElement.scrollHeight,client:innerHeight,width:document.documentElement.scrollWidth,clientW:innerWidth,children:[...document.querySelectorAll('.child')].map(x=>Math.round(x.getBoundingClientRect().height))})''')
  assert dims['width']<=dims['clientW']+2,dims
  assert dims['scroll']<=dims['client']+3,dims
  assert min(dims['children'])>=75,dims
  cups=page.locator('.cup');assert cups.count()==3
  cups.first.click();page.locator('[data-tray="1"]').click()
  assert page.locator('[data-tray="0"] .cup').count()==1
  assert page.locator('[data-tray="1"] .cup').count()==1
  page.locator('#check').click();assert 'Muy bien' in page.locator('#feedback').inner_text()
  page.locator('#reset').click();assert page.locator('[data-tray="0"] .cup').count()==2
  # drag via real pointer path
  source=page.locator('[data-tray="0"] .cup').first.bounding_box();target=page.locator('[data-tray="1"]').bounding_box()
  page.mouse.move(source['x']+source['width']/2,source['y']+source['height']/2)
  page.mouse.down();page.mouse.move(target['x']+target['width']/2,target['y']+target['height']/2,steps=12);page.mouse.up()
  assert page.locator('[data-tray="1"] .cup').count()==1
  print('PASS',w,h,dims)
  page.close()
 browser.close()