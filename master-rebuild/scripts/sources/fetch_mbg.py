import json,sys,time,ssl,urllib.request,urllib.parse,os,glob,re,html
out,indir,ca=sys.argv[1:4]
ctx=ssl.create_default_context(cafile=ca)
UA={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36'}
def get(u):
    for i in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=45,context=ctx) as r: return r.read().decode('utf-8','replace')
        except Exception as e: err=e; time.sleep(3)
    return 'ERR '+str(err)
def search(q):
    t=get('https://plantfinder.mobot.org/PlantFinderProfileResults.aspx?basic='+urllib.parse.quote(q)); time.sleep(1.5)
    return [(m[0],html.unescape(re.sub(r'<[^>]+>','',m[1])).strip()) for m in re.findall(r'href="/PlantFinderDetails\.aspx\?taxonid=(\d+)[^"]*"[^>]*>(.*?)</a>',t,re.S) if re.sub(r'<[^>]+>','',m[1]).strip()]
def norm(s): return re.sub(r'[^a-z]','',s.lower())
for f in sorted(glob.glob(indir+'/P*.json')):
    d=json.load(open(f)); pid=os.path.basename(f)[:3]
    name=d['学名'].replace('‛',"'").replace('’',"'").replace('×','x').replace("Hosta'","Hosta '")
    m=re.match(r"^(.*?)\s*'(.+)'",name); sp=(m.group(1) if m else name).strip(); cv=m.group(2) if m else None
    genus=sp.split()[0]; sp2=' '.join([w for w in sp.split() if w!='x'][:2])
    log=[];pick=None;level=None
    if cv:
        r=search(genus+' '+cv); log.append((genus+' '+cv,r[:8]))
        for tid,nm in r:
            if norm(cv) in norm(nm) and norm(genus) in norm(nm): pick=(tid,nm);level='cultivar';break
    if not pick and len(sp.split())>1:
        r=search(sp2); log.append((sp2,r[:12]))
        for tid,nm in r:
            if cv and norm(cv) in norm(nm): pick=(tid,nm);level='cultivar';break
        if not pick:
            for tid,nm in r:
                if norm(nm)==norm(sp2): pick=(tid,nm);level='species';break
    res={'id':pid,'name':name,'log':log,'pick':pick,'level':level}
    if pick:
        u=f'https://www.missouribotanicalgarden.org/PlantFinder/PlantFinderDetails.aspx?taxonid={pick[0]}'
        t=get(u); time.sleep(1.5); res['url']=u
        open(f'{out}/{pid}.html','w').write(t)
        b=re.sub(r'<script.*?</script>|<style.*?</style>','',t,flags=re.S)
        i=b.find('MainContentPlaceHolder_'); 
        def sec(idp):
            mm=re.search(r'id="MainContentPlaceHolder_'+idp+r'"[^>]*>(.*?)</(?:span|p|div)>',b,re.S)
            return html.unescape(re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',mm.group(1)))).strip() if mm else None
        res['ids']=sorted(set(re.findall(r'id="MainContentPlaceHolder_([A-Za-z]+)"',b)))
        res['fields']={k:sec(k) for k in res['ids']}
    json.dump(res,open(f'{out}/{pid}.json','w'),ensure_ascii=False,indent=1)
    print(pid,name,'->',level,pick, [ (q,len(r)) for q,r in log])
