import os

for fld in ['xml_GaraMan-De26-MauXanh', 'xml_GaraMan-De26-BaiLam', 'xml_GaraMan-De26-HoanThien']:
    d = os.path.join(r"C:\Users\admin\Documents\PTTK", fld)
    print(f"\n=== {fld} ===")
    if os.path.exists(d):
        for f in sorted(os.listdir(d)):
            if f.endswith('.png'):
                p = os.path.join(d, f)
                print(f"  {f:45s}: {os.path.getsize(p):,} bytes")
