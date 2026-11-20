import sqlite3
import os

files_to_check = [
    r'c:\Users\admin\Documents\VPProjects\pttk.vpp',
    r'c:\Users\admin\Documents\VPProjects\untitled.vpp',
    r'c:\Users\admin\Documents\VPProjects\untitled.vpp.bak',
    r'c:\Users\admin\Documents\VPProjects\untitled.vpp.bak2',
    r'c:\Users\admin\Documents\VPProjects\untitled.vpp.bak3',
    r'c:\Users\admin\Documents\VPProjects\pttk.vpp.bak_000f',
]

for fpath in files_to_check:
    if not os.path.exists(fpath):
        continue
    fname = os.path.basename(fpath)
    print(f"\n==========================================")
    print(f"FILE: {fname} (Size: {os.path.getsize(fpath)} bytes)")
    try:
        conn = sqlite3.connect(fpath)
        cursor = conn.cursor()
        
        # Get list of tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = [t[0] for t in cursor.fetchall()]
        print("Tables in SQLite DB:", tables)
        
        # Look for diagram tables
        for t in tables:
            if 'diagram' in t.lower() or 'model' in t.lower() or 'element' in t.lower() or 'view' in t.lower():
                try:
                    cursor.execute(f"SELECT COUNT(*) FROM {t};")
                    cnt = cursor.fetchone()[0]
                    print(f"  Table {t}: {cnt} rows")
                except Exception as e:
                    pass
        
        # Let's search for diagram names
        # Check if there is a Diagram table or similar
        for t in tables:
            # check columns of table t
            cursor.execute(f"PRAGMA table_info({t});")
            cols = [col[1] for col in cursor.fetchall()]
            if any('name' in c.lower() or 'type' in c.lower() for c in cols):
                try:
                    query = f"SELECT {', '.join([c for c in cols if 'id' in c.lower() or 'name' in c.lower() or 'type' in c.lower()][:4])} FROM {t} LIMIT 20;"
                    cursor.execute(query)
                    rows = cursor.fetchall()
                    if rows:
                        print(f"  Sample from {t}:")
                        for r in rows[:10]:
                            print(f"    {r}")
                except:
                    pass
        conn.close()
    except Exception as e:
        print("Error:", e)
