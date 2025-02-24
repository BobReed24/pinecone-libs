ver = "V1.0.0"
import subprocess
import os
pre_process = "sudo apt-get -y install acpi"
process = subprocess.run(pre_process, shell=True, capture_output=True, text=True)
os.system("acpi")
