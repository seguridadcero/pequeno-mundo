#!/usr/bin/env python3
"""Auditoría reproducible: 9 procesos SECUENCIALES, resultados individuales, timeout por caso."""
from pathlib import Path
import subprocess,sys,json,re,tempfile,zipfile,time
R=Path(__file__).resolve().parent
CASES=[(g,w,h) for g in ('repartimos','clasificamos','comparamos') for w,h in ((360,740),(390,844),(1280,900))]
results={};start=time.time()
for g,w,h in CASES:
 key=f'{g}-{w}x{h}'
 try:
  p=subprocess.run([sys.executable,str(R/'prueba_juego.py'),g,str(w),str(h)],capture_output=True,text=True,timeout=30)
  results[key]={'status':'PASS' if p.returncode==0 else 'FAIL','detail':(p.stdout+p.stderr)[-2500:]}
 except subprocess.TimeoutExpired as e:
  results[key]={'status':'TIMEOUT','detail':str(e)}
 print(key,results[key]['status'],flush=True)
for name in ['index.html']+[f'juegos/{g}/index.html' for g,_,_ in CASES[::3]]:
 for i,js in enumerate(re.findall(r'<script(?:\s[^>]*)?>(.*?)</script>',(R/name).read_text(),re.S)):
  with tempfile.NamedTemporaryFile('w',suffix='.js') as f:
   f.write(js);f.flush();p=subprocess.run(['node','--check',f.name],capture_output=True,text=True)
   results[f'syntax-{name}-{i}']={'status':'PASS' if p.returncode==0 else 'FAIL','detail':p.stderr}
results['elapsed_seconds']=round(time.time()-start,2)
(R/'resultados_v11.json').write_text(json.dumps(results,ensure_ascii=False,indent=2))
print('RESULTADO', 'PASS' if all(v['status']=='PASS' for v in results.values() if isinstance(v,dict)) else 'FAIL')
sys.exit(0 if all(v['status']=='PASS' for v in results.values() if isinstance(v,dict)) else 1)
