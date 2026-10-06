import csv,collections
rows=list(csv.DictReader(open('2024_EAVS_for_Public_Release_nolabel_V2.csv',encoding='latin-1')))
def num(v):
    try:
        n=float(v); return n if n>=0 else 0
    except: return 0
pres={x['county_fips']:(x['county_name'],float(x['per_point_diff']),x['state_name']) for x in csv.DictReader(open('pres24.csv'))}
SEN=['TX','OH','FL','MI','NC','GA','SC','IA','KS','AK','NH']
bands=[10,20,30]
print('SENATE  state total | <=10 <=20 <=30 | unmatched')
tot=collections.Counter()
for s in SEN:
    t=0;b=collections.Counter();un=0
    for x in rows:
        if x['State_Abbr']!=s: continue
        n=num(x['D3a']); t+=n
        f=x['FIPSCode'][:5]
        if s=='AK': m=-13.1  # statewide, single jurisdiction
        elif f in pres: m=pres[f][1]*100
        else: un+=n; continue
        for k in bands:
            if abs(m)<=k: b[k]+=n
    print(f'{s} {t:6.0f} | {b[10]:6.0f} {b[20]:6.0f} {b[30]:6.0f} | {un:.0f}')
    tot['t']+=t
    for k in bands: tot[k]+=b[k]
print('SUM',tot)
# margins of some big counties
for s,names in [('Texas',['Travis','Harris','Dallas','Bexar','Tarrant','Collin','Hidalgo','El Paso','Fort Bend'])]:
    for f,(n,m,st) in pres.items():
        if st==s and any(n.startswith(z+' ') for z in names): print(n,round(m*100,1))
# House-only districts
H={
'AL-2':('AL',{'Montgomery':1,'Macon':1,'Bullock':1,'Russell':1,'Barbour':1,'Pike':1,'Crenshaw':1,'Butler':1,'Conecuh':1,'Monroe':1,'Washington':1,'Clarke':.5,'Mobile':.45}),
'KY-6':('KY',{'Fayette':1,'Scott':1,'Woodford':1,'Jessamine':1,'Madison':1,'Clark':1,'Bourbon':1,'Montgomery':1,'Powell':1,'Estill':1,'Nicholas':1,'Fleming':1,'Mercer':1,'Garrard':1,'Anderson':.5,'Bath':.5}),
'ME-2':('ME',{'Androscoggin':1,'Aroostook':1,'Franklin':1,'Hancock':1,'Oxford':1,'Penobscot':1,'Piscataquis':1,'Somerset':1,'Waldo':1,'Washington':1,'Kennebec':.5}),
'MT-1':('MT',{'Lincoln':1,'Flathead':1,'Glacier':1,'Sanders':1,'Lake':1,'Mineral':1,'Missoula':1,'Powell':1,'Granite':1,'Ravalli':1,'Deer Lodge':1,'Silver Bow':1,'Beaverhead':1,'Madison':1,'Gallatin':1,'Pondera':.3}),
'NE-2':('NE',{'Douglas':1,'Saunders':1,'Sarpy':.5}),
'NJ-7':('NJ',{'Hunterdon':1,'Warren':1,'Somerset':.6,'Morris':.25,'Sussex':.35,'Union':.25}),
'NY-17':('NY',{'Rockland':1,'Putnam':1,'Westchester':.4,'Dutchess':.1}),
'PA-1':('PA',{'Bucks':1,'Montgomery':.07}),
'PA-7':('PA',{'Lehigh':1,'Northampton':1,'Carbon':1,'Monroe':.05}),
'PA-8':('PA',{'Lackawanna':1,'Wayne':1,'Pike':1,'Luzerne':.65,'Monroe':.95}),
'PA-10':('PA',{'Dauphin':1,'Cumberland':.65,'York':.45}),
'VA-1':('VA',{'Essex':1,'Gloucester':1,'King and Queen':1,'King William':1,'Lancaster':1,'Mathews':1,'Middlesex':1,'Northumberland':1,'Richmond County':1,'Westmoreland':1,'New Kent':1,'James City':1,'York':1,'Poquoson':1,'Williamsburg':1,'Hanover':.8,'Henrico':.35,'Chesterfield':.35}),
'VA-2':('VA',{'Virginia Beach':1,'Accomack':1,'Northampton':1,'Isle of Wight':1,'Suffolk':1,'Franklin city':1,'Chesapeake':.35,'Southampton':.5}),
'WI-1':('WI',{'Kenosha':1,'Racine':1,'Walworth':1,'Rock':.8,'Milwaukee':.08,'Waukesha':.05}),
'WI-3':('WI',{'Adams':1,'Buffalo':1,'Crawford':1,'Dunn':1,'Eau Claire':1,'Grant':1,'Jackson':1,'Juneau':1,'La Crosse':1,'Monroe':1,'Pepin':1,'Pierce':1,'Portage':1,'Richland':1,'Trempealeau':1,'Vernon':1,'Chippewa':.5,'Sauk':.5,'Wood':.5}),
}
full={'Alabama':'AL','Kentucky':'KY','Maine':'ME','Montana':'MT','Nebraska':'NE','New Jersey':'NJ','New York':'NY','Pennsylvania':'PA','Virginia':'VA','Wisconsin':'WI'}
bycounty=collections.Counter()
for x in rows: bycounty[x['FIPSCode'][:5]]+=num(x['D3a'])
ht=0
for d,(s,cs) in H.items():
    t=0;miss=[]
    for c,w in cs.items():
        hit=[f for f,(n,m,st) in pres.items() if full.get(st)==s and (n==c or n==c+' County' or n==c+' city' or (c=='Richmond County' and n=='Richmond County'))]
        if c in('Franklin city',): hit=[f for f,(n,m,st) in pres.items() if st=='Virginia' and n=='Franklin city']
        if c=='Richmond County': hit=[f for f,(n,m,st) in pres.items() if st=='Virginia' and n=='Richmond County']
        if not hit: miss.append(c); continue
        t+=sum(bycounty[f] for f in hit)*w
    print(d,round(t),'MISSING',miss if miss else '')
    ht+=t
print('house subtotal (excl LA-6, TN-9)',round(ht))
