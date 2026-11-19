import re,html,json,glob,os,sys
d=sys.argv[1]
def clean(s): return html.unescape(re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',s))).strip()
for f in sorted(glob.glob(d+'/P*.html')):
    pid=os.path.basename(f)[:3]; t=open(f,encoding='utf-8').read()
    t=re.sub(r'<script.*?</script>|<style.*?</style>','',t,flags=re.S)
    fl={}
    for m in re.finditer(r'id="ctl00_MainContentPlaceHolder_(\w+?)Row"[^>]*>(.*?)(?=<div id="ctl00_MainContentPlaceHolder_\w+Row"|<div class="clear-float">|$)',t,re.S):
        v=clean(m.group(2))
        if v: fl[m.group(1)]=v
    for m in re.finditer(r'id="ctl00_MainContentPlaceHolder_(\w+)"[^>]*>(.*?)</(?:span|a|h1|h2)>',t,re.S):
        v=clean(m.group(2))
        if v and len(v)<300 and m.group(1) not in fl: fl[m.group(1)]=v
    j=json.load(open(f'{d}/{pid}.json')); j['fields']=fl; j.pop('ids',None)
    json.dump(j,open(f'{d}/{pid}.json','w'),ensure_ascii=False,indent=1)
    print(pid,j['level'],j['pick'][1] if j['pick'] else None,'|',list(fl.keys()))
