import cx_Freeze
import os
os.environ['TCL_LIBRARY'] = r'C:\Program Files\Python35-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Program Files\Python35-32\tcl\tk8.6'
cx_Freeze.setup(
    name="Ideapad",
    version='0.1',
    author="KaiXtr",
    options={"build_exe": {"packages": ["kivy", "os", "webbrowser", "getpass", "platform"]}},
    description="Ideapad",
    executables=[cx_Freeze.Executable('Ideapad.py')])