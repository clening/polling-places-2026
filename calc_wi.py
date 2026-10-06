# Wisconsin EAVS rows are municipalities without county FIPS; match county from the jurisdiction name.
import csv,re,collections
rows=[x for x in csv.DictReader(open('2024_EAVS_for_Public_Release_nolabel_V2.csv',encoding='latin-1')) if x['State_Abbr']=='WI']
def num(v):
    try:
        n=float(v); return n if n>=0 else 0
    except: return 0
c=collections.Counter()
for x in rows:
    m=re.search(r'- ([A-Z .]+) COUNTY',x['Jurisdiction_Name'])
    c[m.group(1) if m else 'UNK']+=num(x['D3a'])
w1={'KENOSHA':1,'RACINE':1,'WALWORTH':1,'ROCK':.8,'MILWAUKEE':.08,'WAUKESHA':.05}
w3={k:1 for k in 'ADAMS,BUFFALO,CRAWFORD,DUNN,EAU CLAIRE,GRANT,JACKSON,JUNEAU,LA CROSSE,MONROE,PEPIN,PIERCE,PORTAGE,RICHLAND,TREMPEALEAU,VERNON'.split(',')}
w3.update({'CHIPPEWA':.5,'SAUK':.5,'WOOD':.5})
print('UNK',c['UNK'],'total',sum(c.values()))
for n,w in(('WI-1',w1),('WI-3',w3)):
    print(n,round(sum(c[k]*v for k,v in w.items())),[k for k in w if k not in c])
