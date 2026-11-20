import sqlite3
import os
import glob

base_dir = r'C:\Users\admin\Documents\flashcard\GaraMan-De26'
vpp_files = glob.glob(os.path.join(base_dir, '*.vpp*'))

print("=== CHECKING FOR ERD IN ALL FILES ===")
for fpath in sorted(vpp_files):
    fname = os.path.basename(fpath)
    try:
        conn = sqlite3.connect(fpath)
        c = conn.cursor()
        c.execute("SELECT ID, DIAGRAM_TYPE, NAME FROM DIAGRAM")
        diagrams = c.fetchall()
        for d in diagrams:
            dtype = d[1].lower()
            dname = d[2].lower()
            if 'erd' in dtype or 'erd' in dname or 'entity' in dtype or 'relat' in dtype or 'data' in dtype or 'table' in dname:
                print(f"Found in {fname}: Type={d[1]}, Name='{d[2]}'")
        conn.close()
    except:
        pass

print("\n=== CHECKING DIAGRAMS IN GaraMan-De26-Activity-Sequence.vpp.bak ===")
bak_file = os.path.join(base_dir, 'GaraMan-De26-Activity-Sequence.vpp.bak')
conn = sqlite3.connect(bak_file)
c = conn.cursor()
c.execute("SELECT ID, DIAGRAM_TYPE, NAME FROM DIAGRAM")
for d_id, d_type, d_name in c.fetchall():
    print(f"\n[{d_type}] '{d_name}' (ID: {d_id})")
    c.execute("""
        SELECT me.NAME, me.MODEL_TYPE 
        FROM DIAGRAM_ELEMENT de
        JOIN MODEL_ELEMENT me ON de.MODEL_ELEMENT_ID = me.ID
        WHERE de.DIAGRAM_ID = ? AND me.NAME IS NOT NULL AND me.NAME != ''
    """, (d_id,))
    elements = c.fetchall()
    print(f"  Count: {len(elements)} elements")
    for name, mtype in elements[:10]:
        print(f"    - {mtype}: {name}")
conn.close()
