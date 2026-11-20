import os
import subprocess

vp_scripts_dir = r"C:\Program Files\Visual Paradigm 18.0\scripts"
export_bat = os.path.join(vp_scripts_dir, "ExportXML.bat")
vpp_dir = r"C:\Users\admin\Documents\flashcard\GaraMan-De26"

vpp_files = [f for f in os.listdir(vpp_dir) if f.endswith('.vpp')]
print("All VPP files:", vpp_files)
