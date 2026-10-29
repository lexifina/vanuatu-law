import re,html,sys
t=open(sys.argv[1],encoding='utf-8',errors='replace').read()
t=re.sub(r'<script.*?</script>','',t,flags=re.S)
if len(sys.argv)>2 and sys.argv[2]=='links': print('\n'.join(re.findall(r'href="([^"]+)"',t))); sys.exit()
s=re.sub(r'<[^>]+>',' ',t); s=html.unescape(s); s=re.sub(r'[ \t]+',' ',s); s=re.sub(r'\n\s*\n+','\n',s)
print(s[:int(sys.argv[2]) if len(sys.argv)>2 else 4000])
