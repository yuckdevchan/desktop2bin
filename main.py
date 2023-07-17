# desktop2bin
# licensed under the GPL v2 only
import subprocess

subprocess.run("./xdg_test.sh", shell=True)

if xdg_desktop_exists:
  print("XDG Desktop Folder Exists.")
else:
  print("XDG Desktop Folder does not exist.")
