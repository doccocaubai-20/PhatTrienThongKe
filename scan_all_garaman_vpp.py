import sqlite3
import os
import glob

base_dir = r'C:\Users\admin\Documents\flashcard\GaraMan-De26'
vpp_files = glob.glob(os.path.join(base_dir, '*.vpp*'))

for fpath in sorted(vpp_files):
    fname = os.path.basename(fpath)
    try:
        conn = sqlite3.connect(fpath)
        c = conn.cursor()
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = [t[0] for t in c.fetchall()]
        if 'DIAGRAM' in tables:
            c.execute("SELECT ID, DIAGRAM_TYPE, NAME FROM DIAGRAM")
            diagrams = c.fetchall()
            erd_or_class = [d for d in diagrams if 'erd' in d[1].lower() or 'erd' in d[2].lower() or 'database' in d[1].lower() or 'data' in d[1].lower() or 'entity' in d[1].lower() or 'chi tiet' in d[2].lower() or 'thiet ke' in d[2].lower()]
            print(f"=== {fname} ({len(diagrams)} diagrams) ===")
            for d in diagrams:
                is_special = d in erd_or_class
                mark = " ***" if is_special else ""
                print(f"    [{d[1]:<25}] '{d[2]}'{mark}")
        conn.close()
    except Exception as e:
        print(f"=== {fname}: {e} ===")
