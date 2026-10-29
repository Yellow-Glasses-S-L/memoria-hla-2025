# Genera mockup/assets/mapa-provincias.js: python3 scripts/generar-mapa-provincias.py spain-provinces.geojson > mockup/assets/mapa-provincias.js
# GeoJSON: https://raw.githubusercontent.com/codeforgermany/click_that_hood/main/public/data/spain-provinces.geojson
import json, math, sys
d=json.load(open(sys.argv[1]))
SKIP={'Las Palmas','Santa Cruz De Tenerife','Ceuta','Melilla'}
K=math.cos(math.radians(40))
def proj(p): return (p[0]*K, -p[1])
feats=[f for f in d['features'] if f['properties']['name'] not in SKIP]
pts=[proj(c) for f in feats for poly in (f['geometry']['coordinates'] if f['geometry']['type']=='MultiPolygon' else [f['geometry']['coordinates']]) for ring in poly for c in ring]
minx=min(p[0] for p in pts); maxx=max(p[0] for p in pts); miny=min(p[1] for p in pts); maxy=max(p[1] for p in pts)
W=600; S=W/(maxx-minx); H=round((maxy-miny)*S)
def T(p): x,y=proj(p); return ((x-minx)*S, (y-miny)*S)
def dp(pts,eps):
    if len(pts)<3: return pts
    a,b=pts[0],pts[-1]; dx,dy=b[0]-a[0],b[1]-a[1]; L=math.hypot(dx,dy) or 1e-9
    i,m=0,0
    for k in range(1,len(pts)-1):
        dd=abs(dy*pts[k][0]-dx*pts[k][1]+b[0]*a[1]-b[1]*a[0])/L
        if dd>m: i,m=k,dd
    if m>eps: return dp(pts[:i+1],eps)[:-1]+dp(pts[i:],eps)
    return [a,b]
def area(r): return abs(sum(r[i][0]*r[i-1][1]-r[i-1][0]*r[i][1] for i in range(len(r))))/2
out={}; cent={}
NAMES={'Alacant/Alicante':'Alicante','Araba/Álava':'Álava','Bizkaia/Vizcaya':'Vizcaya','Castelló/Castellón':'Castellón','Gipuzkoa/Guipúzcoa':'Guipúzcoa','València/Valencia':'Valencia','Illes Balears':'Baleares'}
for f in feats:
    n=NAMES.get(f['properties']['name'],f['properties']['name'])
    polys=f['geometry']['coordinates'] if f['geometry']['type']=='MultiPolygon' else [f['geometry']['coordinates']]
    parts=[]; big=None; ba=0
    for poly in polys:
        r=[T(c) for c in poly[0]]
        a=area(r)
        if a>ba: ba,big=a,r
        if a<12: continue
        h=len(r)//2
        s=dp(r[:h+1],0.9)[:-1]+dp(r[h:],0.9)
        if len(s)<4: continue
        parts.append('M'+'L'.join(f'{x:.1f} {y:.1f}' for x,y in s)+'Z')
    out[n]=''.join(parts)
    # centroid of largest ring
    A=cx=cy=0
    for i in range(len(big)):
        x0,y0=big[i-1]; x1,y1=big[i]; c=x0*y1-x1*y0; A+=c; cx+=(x0+x1)*c; cy+=(y0+y1)*c
    cent[n]=[round(cx/(3*A),1),round(cy/(3*A),1)]
print('/* Provincias de España (península + Baleares), simplificadas. Generado por scripts/generar-mapa-provincias.py\n   desde click_that_hood/spain-provinces.geojson (codeforgermany). No editar a mano. */')
print('const MAPA='+json.dumps({'w':W,'h':H,'minx':minx,'miny':miny,'s':S,'k':K})+';')
print('const PROV='+json.dumps(out,ensure_ascii=False,separators=(',',':'))+';')
print('const PROV_C='+json.dumps(cent,ensure_ascii=False,separators=(',',':'))+';')
