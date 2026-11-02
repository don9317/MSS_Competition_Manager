"""Non-destructive release smoke checks. Run: python verify_release.py"""
from pathlib import Path
from html.parser import HTMLParser
import re, subprocess
root=Path(__file__).parent
html=(root/'index.html').read_text(encoding='utf-8')
class IDs(HTMLParser):
 def __init__(self): super().__init__();self.ids=[]
 def handle_starttag(self,tag,attrs):
  d=dict(attrs)
  if 'id' in d:self.ids.append(d['id'])
parser=IDs();parser.feed(html)
checks={
 'version title and header':html.count('MSS League Scheduler v11.11.87.2')>=2,
 'unique build identifier':"MSS-87.2-20261101-A" in html,
 'read-only build information panel':all(x in html for x in ['buildInfoDialog','buildInfoButton','buildSourceText','getMssBuildDetails']),
 'sticky parking lot remains': 'id="parkingLotDirectorBanner" style="position:sticky' in html,
 'core scheduling functions retained':all(re.search(r'function\s+'+n+r'\s*\(',html) for n in ['generateSchedule','optimizeSchedule','renderAll','openDatabase','readStateFromDB','writeStateToDB']),
 'no duplicate element ids':len(parser.ids)==len(set(parser.ids)),
 'existing IndexedDB name retained':"const DB_NAME='MSSLeagueSchedulerDB'" in html,
 'existing record key retained':"const RECORD_KEY='current'" in html,
 'no external runtime dependency added':not bool(re.search(r'<script[^>]+src=',html)),
}
js=html.split('<script>',1)[1].rsplit('</script>',1)[0]
(root/'_syntax_check.js').write_text(js)
result=subprocess.run(['node','--check',str(root/'_syntax_check.js')],capture_output=True,text=True)
(root/'_syntax_check.js').unlink()
checks['JavaScript parses']=result.returncode==0
for name,ok in checks.items():print(('PASS' if ok else 'FAIL')+'  '+name)
if result.returncode:print(result.stderr)
if not all(checks.values()):raise SystemExit(1)
print('All non-destructive static smoke checks passed. Browser interaction and scheduling regressions remain untested.')
