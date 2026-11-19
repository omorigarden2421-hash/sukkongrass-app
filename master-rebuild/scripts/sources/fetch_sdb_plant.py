import json,sys,time,urllib.request,urllib.parse
out=sys.argv[1]
UA={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36','Accept':'application/json'}
def get(params):
    u='https://www.stauden.de/staudendatenbank/api.php?'+urllib.parse.urlencode(params)
    for i in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=40) as r: return json.load(r)
        except Exception as e: err=e; time.sleep(3)
    return {'error':str(err)}
for q in ['Armeria maritima','Sedum spurium','Phedimus spurius','Anemone sylvestris','Lonicera periclymenum','Cornus alba','Hydrangea','Prostanthera','Drachenblut']:
    s=get({'action':'search','q':q}); time.sleep(1.5)
    print(q,[(i['relid'],i['bona_1']) for i in s.get('items',[]) if i.get('type')=='plant'][:16])
picks={'P01':565,'P02':504,'P03':310,'P04':5640,'P05':25877,'P06':30610,'P07':9289,'P08':1108,'P09':11022,'P10':2811,'P11':2718,'P12':2063,'P13':25326,'P16':28621,'P17':3622,'P18':3583,'P19':29498,'P20':6369,'P21':43483,'P22':31292,'P24':43136}
for pid,r in picks.items():
    d=get({'action':'plant','relid':r}); time.sleep(1.5)
    json.dump(d,open(f'{out}/{pid}_plant_{r}.json','w'),ensure_ascii=False)
    print(pid,r,d.get('master',{}).get('bona_lang'),len(json.dumps(d)))
