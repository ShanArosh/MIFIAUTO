import sys
import subprocess
import pkg_resources


required = {'selenium', 'pywinauto','colorama'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing])
print("\n")
print("Mifiauto Infrastructure is Provisioned")
input()
