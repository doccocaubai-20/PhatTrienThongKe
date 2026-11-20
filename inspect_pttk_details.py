import sqlite3

conn = sqlite3.connect(r'C:\Users\admin\Documents\VPProjects\pttk.vpp')
c = conn.cursor()

print("=== DIAGRAMS IN pttk.vpp ===")
c.execute("SELECT ID, DIAGRAM_TYPE, NAME FROM DIAGRAM")
diagrams = c.fetchall()
for d_id, d_type, d_name in diagrams:
    print(f"\nDiagram: [{d_type}] '{d_name}' (ID: {d_id})")
    # find elements in this diagram
    c.execute("""
        SELECT me.NAME, me.MODEL_TYPE 
        FROM DIAGRAM_ELEMENT de
        JOIN MODEL_ELEMENT me ON de.MODEL_ELEMENT_ID = me.ID
        WHERE de.DIAGRAM_ID = ? AND me.NAME IS NOT NULL AND me.NAME != ''
    """, (d_id,))
    elements = c.fetchall()
    print(f"  Total named elements: {len(elements)}")
    for name, mtype in elements[:20]:
        print(f"    - {mtype}: {name}")

print("\n=== ALL NAMED CLASSES IN pttk.vpp ===")
c.execute("SELECT NAME, MODEL_TYPE FROM MODEL_ELEMENT WHERE MODEL_TYPE IN ('Class', 'DBTable', 'Table', 'DBEntity') AND NAME IS NOT NULL AND NAME != ''")
for r in c.fetchall():
    print(f"  {r[1]}: {r[0]}")

print("\n=== ALL MODEL ELEMENT TYPES IN pttk.vpp ===")
c.execute("SELECT MODEL_TYPE, count(*) FROM MODEL_ELEMENT GROUP BY MODEL_TYPE")
for r in c.fetchall():
    print(f"  {r[0]}: {r[1]}")

conn.close()
