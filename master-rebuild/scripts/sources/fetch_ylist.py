import json,sys,time,urllib.request,urllib.parse,os,glob,re,html
out,indir=sys.argv[1:3]
UA={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36'}
def search(q):
    u='http://ylist.info/ylist_simple_search.php?'+urllib.parse.urlencode({'any_field':q,'capital':'0','family_order':'2','family_disp_type':'1','family_header':'0','spec_order':'0','list_type':'0','search':'検索'})
    t=urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=40).read().decode('utf-8','replace'); time.sleep(1.5)
    n=re.search(r'ヒット数:\s*(\d+)',re.sub(r'<[^>]+>','',t))
    rows=[]
    for m in re.finditer(r"<span class = 'list_all'>.*?pass=(\d+)'><span class = 'gakumei'>(.*?)</span>(.*?)</(?:span|a)>",t,re.S):
        rest=html.unescape(m.group(3)).replace('\u3000',' ').split()
        rows.append({'pass':m.group(1),'sci':re.sub(r'\s+',' ',html.unescape(m.group(2))).strip(),'ja':rest[0] if rest else '','status':rest[1] if len(rest)>1 else ''})
    return u,(int(n.group(1)) if n else None),rows
for f in sorted(glob.glob(indir+'/P*.json')):
    d=json.load(open(f)); pid=os.path.basename(f)[:3]
    name=d['学名'].replace('×','x').replace("Hosta'","Hosta '")
    sp=re.split(r"\s*['‛]",name)[0].strip(); ws=[w for w in sp.split() if w not in('x','sp.')]
    q=' '.join(ws[:2]); res={'id':pid,'q':q}
    if len(ws)>=2:
        res['url'],res['n'],res['rows']=search(q)
    json.dump(res,open(f'{out}/{pid}.json','w'),ensure_ascii=False,indent=1)
    print(pid,q,res.get('n'),res.get('rows',[])[:6])
