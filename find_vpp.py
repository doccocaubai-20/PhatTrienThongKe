import os
import glob

search_dirs = [
    r'c:\Users\admin\Documents\PTTK',
    r'c:\Users\admin\Documents',
    r'c:\Users\admin\Desktop',
    r'c:\Users\admin\AppData\Roaming\VisualParadigm',
    r'c:\Users\admin\AppData\Local\VisualParadigm',
    r'c:\Users\admin\.vpp',
    r'c:\Users\admin\.visualparadigm',
]

print("=== SEARCHING FOR .vpp and .vpp.bak FILES ===")
found = []
for sdir in search_dirs:
    if os.path.exists(sdir):
        print(f"Scanning: {sdir}")
        for root, dirs, files in os.walk(sdir):
            # don't go too deep into node_modules or .git
            if '.git' in root or 'node_modules' in root:
                continue
            for f in files:
                if f.endswith('.vpp') or f.endswith('.bak') or '.vpp' in f or 'autosave' in f.lower():
                    fpath = os.path.join(root, f)
                    try:
                        size = os.path.getsize(fpath)
                        mtime = os.path.getmtime(fpath)
                        import time
                        time_str = time.ctime(mtime)
                        found.append((fpath, size, time_str))
                        print(f"FOUND: {fpath} ({size} bytes, modified: {time_str})")
                    except Exception as e:
                        pass

print(f"\nTotal files found: {len(found)}")
