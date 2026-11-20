import sqlite3
import os
import glob
from datetime import datetime

base_dir = r'C:\Users\admin\Documents\flashcard\GaraMan-De26'
target_file = os.path.join(base_dir, 'GaraMan-De26-Activity-Sequence.vpp')

print(f"Inspecting: {target_file}")
mtime = datetime.fromtimestamp(os.path.getmtime(target_file)).strftime('%Y-%m-%d %H:%M:%S')
print(f"Size: {os.path.getsize(target_file)} bytes | Modified: {mtime}")

conn = sqlite3.connect(target_file)
c = conn.cursor()

c.execute("SELECT ID, DIAGRAM_TYPE, NAME FROM DIAGRAM")
diagrams = c.fetchall()
print(f"\nTotal Diagrams in GaraMan-De26-Activity-Sequence.vpp: {len(diagrams)}")
for d in diagrams:
    print(f"  - [{d[1]:<25}] '{d[2]}' (ID: {d[0]})")

print("\n--- Model Elements Count ---")
c.execute("SELECT MODEL_TYPE, count(*) FROM MODEL_ELEMENT GROUP BY MODEL_TYPE ORDER BY count(*) DESC LIMIT 15")
for r in c.fetchall():
    print(f"  {r[0]}: {r[1]}")

print("\n--- Checking for ERD or Tables or Design Classes ---")
c.execute("SELECT NAME, MODEL_TYPE FROM MODEL_ELEMENT WHERE MODEL_TYPE IN ('DBTable', 'Table', 'DBEntity', 'Entity', 'Class') AND NAME IS NOT NULL AND NAME != ''")
classes = c.fetchall()
print(f"Total Class/Table elements: {len(classes)}")
for cl in classes[:35]:
    print(f"  [{cl[1]}] {cl[0]}")

conn.close()
