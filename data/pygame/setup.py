from cx_Freeze import setup, Executable

execs = [Executable("game.py")]

setup(name="Eat The Apples",
version="0.1",
options={"build_exe": {"packages": ["pygame"]}},
executables=execs
)
