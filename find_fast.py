import os
import glob
import sqlite3

files = glob.glob(r'C:\Users\admin\Documents\flashcard\GaraMan-De26\*.vpp*') + \
        glob.glob(r'C:\Users\admin\Documents\VPProjects\*.vpp*')

print(f"Total files to check: {len(files)}")
for fpath in files:
    fname = os.path.basename(fpath)
    try:
        conn = sqlite3.connect(fpath)
        c = conn.cursor()
        c.execute("SELECT count(*) FROM MODEL_ELEMENT WHERE NAME LIKE '%tbl%' OR MODEL_TYPE IN ('DBTable', 'Table')")
        cnt = c.fetchone()[0]
        if cnt > 0:
            print(f"FOUND IN {fname}: {cnt} table elements!")
            c.execute("SELECT NAME, MODEL_TYPE FROM MODEL_ELEMENT WHERE NAME LIKE '%tbl%' OR MODEL_TYPE IN ('DBTable', 'Table') LIMIT 10")
            for r in c.fetchall():
                print(f"   {r[1]}: {r[0]}")
        conn.close()
    except Exception as e:
        # not sqlite or error
        pass
