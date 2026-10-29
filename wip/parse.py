"""Read the cache only; write corpus.json. Phase 1 stub: Constitution, 2006 consolidated edition (oldest available)."""
import hashlib, json, os, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import fetch, rtf
S = json.loads((HERE / 'sources.json').read_text(encoding='utf-8'))

def norm(t):
    t = t.replace('\u00a0', ' ').replace('\t', ' ')
    t = re.sub(r'[\u2018\u2019]', "'", t); t = re.sub(r'[\u201c\u201d]', '"', t)
    return '\n'.join(re.sub(r' +', ' ', l).strip() for l in t.split('\n'))

def constitution():
    raw = fetch.raw(S['con-2006'])
    lines = [l for l in norm(rtf.to_text(raw)).split('\n') if l]
    start = [i for i, l in enumerate(lines) if l == 'CONSTITUTION OF THE REPUBLIC OF VANUATU'][1]
    units, key, cur, art = {}, 'preamble', ['# Preamble'], 0
    for l in lines[start + 1:]:
        m = re.match(r'^(\d+)([A-Z]?)\. (.+)$', l)
        if l.startswith('SCHEDULE'):
            break
        if m and int(m.group(1)) == art + 1 or (m and m.group(2) and int(m.group(1)) == art):
            units[key] = '\n'.join(cur) + '\n'
            art = int(m.group(1)); key = f'art-{art:03d}' + (f'-{m.group(2).lower()}' if m.group(2) else '')
            cur = [f'# Article {art}{m.group(2)}. {m.group(3)}']
            continue
        cur.append(l)
    units[key] = '\n'.join(cur) + '\n'
    units = {k: {'label': ('Preamble' if k == 'preamble' else 'Art. ' + k[4:].lstrip('0').replace('-', '').upper()),
                 'kind': 'art' if k != 'preamble' else 'preamble', 'text': v} for k, v in units.items()}
    src = S['con-2006']
    return {'slug': 'constitution', 'short': 'Constitution', 'title': 'Constitution of the Republic of Vanuatu',
            'url': 'http://www.paclii.org/vu/legis/consol_act/cotrov406/', 'first_law': None,
            'earlier_laws': ['act-1980-10', 'act-1981-15', 'act-1983-20'],
            'versions': [{'from': '2006-08-31', 'source_url': fetch.wb_url(src),
                          'sha256': hashlib.sha256(raw).hexdigest(), 'units': units, 'credits': {},
                          'note': 'Laws of the Republic of Vanuatu, Consolidated Edition 2006 (Acts 10 of 1980, 15 of 1981, 20 of 1983), as published by PacLII; dated by its earliest Internet Archive capture, 31 August 2006.'}]}

laws = {k: {'label': l, 'title': t, 'kind': 'law', 'enacted': None, 'published': None, 'url': None,
            'temporary_until': None, 'restores': None, 'note': None} for k, l, t in [
    ('act-1980-10', 'Act 10 of 1980', 'Constitution First Amendment Act 1980'),
    ('act-1981-15', 'Act 15 of 1981', 'Constitution Second Amendment Act 1981'),
    ('act-1983-20', 'Act 20 of 1983', 'Constitution Third Amendment Act 1983')]}
corpus = {
 'country': {'code': 'VU', 'name': 'Vanuatu', 'slug': 'vanuatu', 'lang': 'en', 'tz': 'Pacific/Efate', 'future_branch': 'future',
   'publisher': {'name': 'Pacific Islands Legal Information Institute (PacLII)', 'email': 'paclii@paclii.invalid'},
   'default_in_force_rule': {'text': 'Interpretation Act [Cap 132]: an Act commences on publication in the Gazette unless it provides otherwise (to verify)', 'source': 'http://www.paclii.org/vu/legis/consol_act/ia138/'},
   'licence_note': 'Source: PacLII (www.paclii.org), Laws of the Republic of Vanuatu Consolidated Edition 2006, read from Internet Archive captures.'},
 'sources': [{'name': 'PacLII Vanuatu Consolidated Legislation 2006, via Internet Archive', 'url': 'http://www.paclii.org/vu/legis/consol_act/', 'retrieved': '2026-10-29', 'requests': 1, 'licence': 'PacLII free access; legislation text is public law', 'notes': 'Read only through web.archive.org id_ captures, pinned by timestamp.'}],
 'laws': laws, 'acts': [constitution()], 'applies': [],
 'decisions': ['English text built; French and Bislama official texts exist.',
   'Phase 1 stub: the Constitution as in the Consolidated Edition 2006 is the oldest version available, credited to the publisher; it is dated 2006-08-31, the earliest Internet Archive capture of that edition on PacLII, because the edition carries no day of its own.',
   'Not yet applied: Constitution (Fifth Amendment) Act 2006 (Act 24 of 2006), Constitution (Sixth)(Amendment) Act 2013 (Act 27 of 2013), and the Constitution (Eighth)(Amendment) Act No. 21 of 2023 approved at the 29 May 2024 referendum.'],
 'ai_use': ['none: parsing is deterministic code; no model wrote or edited legal text.']}
tmp = HERE / 'corpus.json.tmp'
tmp.write_text(json.dumps(corpus, ensure_ascii=False, indent=1) + '\n', encoding='utf-8', newline='\n')
os.replace(tmp, HERE / 'corpus.json')
a = corpus['acts'][0]['versions'][0]['units']
print(len(a), list(a)[:5], list(a)[-3:])
