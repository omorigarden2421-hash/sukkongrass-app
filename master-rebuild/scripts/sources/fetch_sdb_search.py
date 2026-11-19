import json,sys,time,urllib.request,urllib.parse,os,glob,re
out=sys.argv[1]; indir=sys.argv[2]
UA={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36','Accept':'application/json'}
def get(params):
    u='https://www.stauden.de/staudendatenbank/api.php?'+urllib.parse.urlencode(params)
    for i in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=40) as r: return json.load(r)
        except Exception as e: err=e; time.sleep(3)
    return {'error':str(err)}
for f in sorted(glob.glob(indir+'/P*.json')):
    d=json.load(open(f)); pid=os.path.basename(f)[:3]; name=d['学名']
    name=name.replace('‛',"'").replace('’',"'").replace('×','x')
    m=re.match(r"^(.*?)\s*'(.+)'",name)
    qs=[]
    if m: qs.append(m.group(1).strip()+' '+m.group(2)); qs.append(m.group(2))
    sp=(m.group(1) if m else name).strip()
    qs.append(sp); qs.append(' '.join(sp.split()[:2]))
    res={'name':name,'tries':[]}
    for q in dict.fromkeys(qs):
        s=get({'action':'search','q':q}); time.sleep(1.5)
        items=[i for i in s.get('items',[]) if i.get('type')=='plant']
        res['tries'].append({'q':q,'n':len(items),'names':[(i['relid'],i['bona_1']) for i in items[:40]]})
        if items: break
    json.dump(res,open(f'{out}/{pid}_search.json','w'),ensure_ascii=False,indent=1)
    print(pid,name,'|',[(t['q'],t['n']) for t in res['tries']],res['tries'][-1]['names'][:6])
