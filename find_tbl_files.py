import os
import glob
from datetime import datetime

search_str = b'tblThanhVien'

dirs_to_search = [
    r'C:\Users\admin\Documents\VPProjects',
    r'C:\Users\admin\Documents\flashcard\GaraMan-De26',
    r'C:\Users\admin\Documents\PTTK',
    r'C:\Users\admin\AppData\Roaming\VisualParadigm\ws',
    r'C:\Users\admin\Desktop',
    r'C:\Users\admin\Downloads'
]

found = []
for d in dirs_to_search:
    if not os.path.exists(d):
        continue
    for root, dirs, files in os.walk(d):
        for f in files:
            p = os.path.join(root, f)
            try:
                # only search files under 100MB
                if os.path.getsize(p) > 100 * 1024 * 1024:
                    continue
                with open(p, 'rb') as fp:
                    data = fp.read()
                    if search_str in data:
                        found.append((p, os.path.getsize(p), os.path.getmtime(p)))
            except:
                pass

print(f"Total found: {len(found)}")
for p, s, m in sorted(found, key=lambda x: x[2], reverse=True):
    dt = datetime.fromtimestamp(m).strftime('%Y-%m-%d %H:%M:%S')
    print(f"Found: {p} | Size: {s} | Modified: {dt}")
