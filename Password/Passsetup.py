import cx_Freeze
import os
os.environ['TCL_LIBRARY'] = r'C:\Program Files\Python35-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Program Files\Python35-32\tcl\tk8.6'
cx_Freeze.setup(
    name="Password Generator",
    version='0.1',
    author="KaiXtr",
    options={"build_exe": {"packages": ["kivy", "time", "re", "random", "pyperclip", "getpass"]}},
    description="Password Generator v0.1 EN",
    executables=[cx_Freeze.Executable('Password Generator.py')])