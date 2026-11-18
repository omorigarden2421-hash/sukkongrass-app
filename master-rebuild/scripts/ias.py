import openpyxl,re,json,glob,sys
wb=openpyxl.load_workbook('/tmp/claude-0/env/list_plants.xlsx',read_only=True)
L=[]
for sh in ('国外','国内'):
    for r in wb[sh].iter_rows(values_only=True):
        if r and isinstance(r[0],(int,float)) and r[8]:
            L.append({'sheet':sh,'cat':r[3],'tokutei':r[5],'ja':r[7],'sci':str(r[8]).replace('\n',' '),'area':r[9]})
def key(s):
    s=re.sub(r"[‘’‛'\"].*$","",s); p=s.replace('×',' ').split()
    p=[x for x in p if x not in ('x',)]
    return ' '.join(p[:2]).lower()
def check(sci):
    k=key(sci); g=k.split()[0] if k else ''
    hits=[x for x in L if key(x['sci'])==k]
    ghits=[x for x in L if key(x['sci']).split()[:1]==[g] and x not in hits]
    return hits,ghits
if __name__=='__main__':
    print(len(L),'entries')
    for p in sorted(glob.glob(sys.argv[1]+'/P*.json')):
        d=json.load(open(p)); h,g=check(d['学名'])
        print(d['id'],d['学名'],'| 該当:',[(x['ja'],x['cat'],x['tokutei']) for x in h],'| 同属:',[(x['ja'],x['sci'][:40]) for x in g][:3])
