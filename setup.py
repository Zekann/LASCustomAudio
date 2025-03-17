import sys

from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os"], "excludes": ["tkinter", "customtinker"], "include_files": ["encodings", "PySide6"], "include_files": ["tools"], "optimize": 2}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

build_icon = "icon.ico"

setup(
    name = "Custom Sound for LAS",
    version = "0.1",
    description = "Tools for make random sound for LAS",
    options = {"build_exe": build_exe_options},
    executables = [Executable("custom_audio.py", base=base, icon=build_icon)]
)
