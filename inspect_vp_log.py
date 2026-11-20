import os
import re

log_path = r'C:\Users\admin\AppData\Roaming\VisualParadigm\vp.log'
if not os.path.exists(log_path):
    print("Log not found")
    exit()

print(f"Log size: {os.path.getsize(log_path)} bytes")

with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")
print("\n--- Last 50 lines ---")
for line in lines[-50:]:
    print(line.strip())

print("\n--- Recent lines mentioning .vpp or open project ---")
recent_lines = [l.strip() for l in lines if any(k in l.lower() for k in ['.vpp', 'open project', 'save project', 'diagram', 'erd'])]
for l in recent_lines[-30:]:
    print(l)
