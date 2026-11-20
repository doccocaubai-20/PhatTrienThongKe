import subprocess
import os

vp_scripts_dir = r"C:\Program Files\Visual Paradigm 18.0\scripts"
export_bat = os.path.join(vp_scripts_dir, "ExportXML.bat")

for name in ['GaraMan-De26-MauXanh.vpp', 'GaraMan-De26-BaiLam.vpp', 'GaraMan-De26-HoanThien.vpp']:
    target_vpp = rf"C:\Users\admin\Documents\flashcard\GaraMan-De26\{name}"
    out_dir = rf"C:\Users\admin\Documents\PTTK\xml_{name[:-4]}"
    os.makedirs(out_dir, exist_ok=True)
    cmd = [export_bat, "-project", target_vpp, "-out", out_dir]
    res = subprocess.run(cmd, cwd=vp_scripts_dir, capture_output=True, text=True)
    print(f"{name}: rc={res.returncode}")
