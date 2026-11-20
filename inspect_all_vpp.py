import sqlite3
import os
import glob
from datetime import datetime

vp_dir = r'C:\Users\admin\Documents\VPProjects'
files = glob.glob(os.path.join(vp_dir, '*.vpp*'))

print(f"Scanning directory: {vp_dir}")

for fpath in sorted(files):
    fname = os.path.basename(fpath)
    mtime = datetime.fromtimestamp(os.path.getmtime(fpath)).strftime('%Y-%m-%d %H:%M:%S')
    size = os.path.getsize(fpath)
    print(f"\n=======================================================")
    print(f"FILE: {fname} | Size: {size} bytes | Modified: {mtime}")
    try:
        conn = sqlite3.connect(fpath)
        c = conn.cursor()
        
        # Check tables
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = [t[0] for t in c.fetchall()]
        
        if 'DIAGRAM' in tables:
            c.execute("SELECT ID, DIAGRAM_TYPE, NAME FROM DIAGRAM")
            diagrams = c.fetchall()
            print(f"  DIAGRAMS ({len(diagrams)}):")
            for d in diagrams:
                print(f"    - Type: {d[1]:<25} | Name: '{d[2]}' | ID: {d[0]}")
        
        if 'LAST_DIAGRAM' in tables:
            c.execute("SELECT ID, DIAGRAM_TYPE, NAME FROM LAST_DIAGRAM")
            ldiagrams = c.fetchall()
            print(f"  LAST_DIAGRAMS ({len(ldiagrams)}):")
            for d in ldiagrams:
                print(f"    - Type: {d[1]:<25} | Name: '{d[2]}' | ID: {d[0]}")
                
        # Count elements by type
        if 'MODEL_ELEMENT' in tables:
            c.execute("SELECT MODEL_TYPE, count(*) FROM MODEL_ELEMENT GROUP BY MODEL_TYPE ORDER BY count(*) DESC LIMIT 10")
            print("  Top Model Elements:")
            for row in c.fetchall():
                print(f"    - {row[0]}: {row[1]}")
                
            # Check for Class or DB Table names
            c.execute("SELECT NAME, MODEL_TYPE FROM MODEL_ELEMENT WHERE NAME IS NOT NULL AND NAME != '' AND MODEL_TYPE IN ('Class', 'DBTable', 'Table', 'DBEntity', 'Entity', 'Actor', 'UseCase') LIMIT 25")
            sample_elements = c.fetchall()
            if sample_elements:
                print(f"  Sample Named Elements ({len(sample_elements)}):")
                for se in sample_elements[:15]:
                    print(f"    - [{se[1]}] {se[0]}")
                    
        conn.close()
    except Exception as e:
        print(f"  Error reading {fname}: {e}")
