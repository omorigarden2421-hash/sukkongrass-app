import csv,json,re,sys,glob,os
csv.field_size_limit(10**9)
rows={};byname={}
with open('/tmp/claude-0/kew/wcvp_names.csv',encoding='utf-8') as f:
    for r in csv.DictReader(f,delimiter='|'):
        if r['taxon_rank'] not in ('Species','Variety','Subspecies','Genus','Form'): continue
        rows[r['plant_name_id']]=r
        byname.setdefault(r['taxon_name'],[]).append(r['plant_name_id'])
def clean(s):
    s=re.sub(r"[‘’‛'\"].*$","",s)          # drop cultivar
    s=s.replace('×','× ').replace(' x ',' × ')
    s=re.sub(r'\s+',' ',s).strip()
    s=re.sub(r'var\.(\S)',r'var. \1',s); s=re.sub(r'subsp\.(\S)',r'subsp. \1',s)
    s=re.sub(r'\b(sp|f)\.?$','',s).strip()
    return s
def lookup(sci):
    q=clean(sci); cands=[q]
    parts=q.split()
    if len(parts)>2: cands.append(' '.join(parts[:2]))
    if parts and parts[0]=='×': pass
    for c in cands:
        c2=c.replace('× ','×')
        for key in (c,c2):
            order={'Accepted':0,'Synonym':1,'Artificial Hybrid':2}
            for pid in sorted(byname.get(key,[]),key=lambda p:order.get(rows[p]['taxon_status'],9)):
                r=rows[pid]
                acc=rows.get(r['accepted_plant_name_id'],r)
                return {'query':sci,'matched':key,'status':r['taxon_status'],'accepted':acc['taxon_name']+' '+acc['taxon_authors'],
                        'family':acc['family'],'native':acc['geographic_area'],'lifeform':acc['lifeform_description'],'climate':acc['climate_description'],'partial':c!=q}
    return {'query':sci,'matched':None}
if __name__=='__main__':
    for p in sorted(glob.glob(sys.argv[1]+'/P*.json')):
        d=json.load(open(p)); r=lookup(d['学名'])
        print(d['id'],'|',d['学名'],'→',r.get('matched'),'|',r.get('status'),'|',r.get('accepted'),'|',r.get('family'),'|',r.get('native'),'|',r.get('lifeform'))
