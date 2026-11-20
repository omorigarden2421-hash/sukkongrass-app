import re,html,sys,os,subprocess,time
OUT=sys.argv[1]; os.makedirs(OUT,exist_ok=True)
def cl(x):
    x = re.sub(r"<button.*?</button>|<dialog.*?</dialog>|<svg.*?</svg>|<script.*?</script>", "", x, flags=re.S)
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", x))).strip()
for arg in sys.argv[2:]:
    k,ids=arg.split(':')
    for i in ids.split(','):
        f=f'{OUT}/{i}.html'
        if not os.path.exists(f) or os.path.getsize(f)<20000:
            subprocess.run(["curl","-sSL","-m","40","-A","Mozilla/5.0",f"https://www.rhs.org.uk/plants/{i}/x/details","-o",f]); time.sleep(1)
        t=open(f,encoding='utf-8',errors='replace').read()
        d={}
        for a,b in re.findall(r"<dt[^>]*>(.*?)</dt>\s*<dd[^>]*>(.*?)</dd>", t, re.S):
            kk=cl(a).split(" (function")[0].strip()
            if kk and kk not in d: d[kk]=cl(b)
        h1=re.search(r'<h1[^>]*>(.*?)</h1>',t,re.S); ti=re.search(r'<title>(.*?)</title>',t,re.S)
        common=html.unescape(ti.group(1)).split('|')[1].strip()[:40] if ti and ti.group(1).count('|')>1 else ''
        print(k,i,'|',cl(h1.group(1))[:62] if h1 else '','|',d.get('Name Status'),'|',d.get('Hardiness','')[:3],'|',len(d),'|',common)
