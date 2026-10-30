"""Build the Constitution version from the official parliament.gov.vu PDF text (pdftotext, non-layout)."""
import json,re,sys,hashlib
txt=open(sys.argv[1],encoding='utf8').read()
pdf_sha=sys.argv[2]
d=json.load(open('corpus.json',encoding='utf8'))
old=d['acts'][0]['versions'][0]['units']
titles={}
for k,u in old.items():
    m=re.match(r'# Article (\d+[A-Z]?)\. (.*)',u['text'])
    if m: titles[m.group(1)]=m.group(2).strip()
titles.update({'13':'Recognition of dual citizenship','29':'Malvatumauri Council of Chiefs','78':'Customary institutions to resolve land ownership and disputes','83':'Provincial Government Councils'})
lines=txt.split('\n')
i=next(n for n,l in enumerate(lines) if l.startswith('WE, the people'))
body=[]
for l in lines[i:]:
    l=l.strip()
    if not l or re.fullmatch(r'\d+',l) or l.startswith('LAWS OF THE REPUBLIC OF VANUATU') or l=='CONSTITUTION OF THE REPUBLIC OF VANUATU' or l=='\x0c': continue
    l=l.replace('\x0c','').replace('�','–').replace('­','')
    body.append(l)
# split preamble sentences: keep as one-line-per-clause like before
units={};cur=None;order=[]
def start(key,label,kind,head):
    global cur
    cur=key;units[key]={'label':label,'kind':kind,'lines':[head]}
start('preamble','Preamble','preamble','# Preamble')
expect=1
for l in body:
    m=re.match(r'(\d+[A-Z]?)\. (.*)$',l)
    if m and m.group(1)==str(expect) and cur!=None and (m.group(1) in titles) and not (cur and cur.startswith('sch')):
        n=m.group(1);rest=m.group(2);t=titles[n]
        if rest.startswith(t): rest=rest[len(t):].strip()
        elif not t.startswith(rest[:20]): print('title mismatch',n,t,'|',rest[:60])
        else: rest=''
        start('art-%03d'%int(n),'Art. '+n,'art','# Article %s. %s'%(n,t))
        if rest: units[cur]['lines'].append(rest)
        expect+=1;continue
    m=re.match(r'SCHEDULE (\d)$',l)
    if m:
        start('sch-%s'%m.group(1),'Schedule '+m.group(1),'schedule','# Schedule '+m.group(1));continue
    units[cur]['lines'].append(l)
print('articles',expect-1)
# re-wrap: join lines into paragraphs; a new paragraph starts at "(n)" / "(a)" / numbered line
out={}
for k,u in units.items():
    head=u['lines'][0];paras=[]
    for l in u['lines'][1:]:
        if paras and not re.match(r'\(\w+\) |CHAPTER |PART |Part |\d+\.$',l) and not re.match(r'^\d+\.$',paras[-1]) :
            paras[-1]+=' '+l
        else: paras.append(l)
    # split inline subclauses "(1) ... (2) ..." not done; keep
    out[k]={'label':u['label'],'kind':u['kind'],'text':head+'\n'+'\n'.join(paras)+'\n'}
a=d['acts'][0]
a['url']='https://parliament.gov.vu/images/constitution.pdf'
a['versions']=[{'from':'2020-04-29','source_url':'https://parliament.gov.vu/images/constitution.pdf','sha256':pdf_sha,'units':out,'credits':{},
 'note':'Laws of the Republic of Vanuatu, Consolidated Edition 2020 (Acts 10 of 1980, 15 of 1981, 20 of 1983, 24 of 2006, 27 of 2013), as published by the Parliament of Vanuatu; dated by its stated "Order commenced on 29th April 2020".'}]
a['earlier_laws']=['act-1980-10','act-1981-15','act-1983-20']
d['country']['publisher']={'name':'Parliament of the Republic of Vanuatu','email':'info@parliament.gov.vu'}
d['country']['licence_note']='Source: Parliament of the Republic of Vanuatu (parliament.gov.vu), Constitution, Laws of the Republic of Vanuatu Consolidated Edition 2020.'
d['sources']=[{'name':'Parliament of Vanuatu: Constitution (Consolidated Edition 2020)','url':'https://parliament.gov.vu/images/constitution.pdf','retrieved':'2026-10-30','requests':1,'licence':'Official text of the Constitution published by the Parliament; site states no reuse terms (robots.txt absent, Terms page missing).','notes':'Text layer read with pdftotext; page headers and numbers removed, broken dash glyphs normalised.'}]
json.dump(d,open('corpus.json','w',encoding='utf8',newline='\n'),ensure_ascii=False,indent=1)
print(len(out),[k for k in out if k.startswith('sch')])
