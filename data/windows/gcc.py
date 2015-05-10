#*--coding: utf-8--*
class gcc(object):
	def __init__(self, compilerpath, filec, cxfreeze=False, py2exe=False, py2app=False, mingw=False):
		super(gcc, self).__init__()
		self.c = compilerpath
		self.file = filec
		if cxfreeze == True:
			self.method = 'cxfreeze'
		elif py2exe == True:
			self.method = 'py2exe'
		elif py2app == True:
			self.method = 'py2app'
		else:
			self.method = 'shebang'
		if mingw == True:
			from os import system as cmd
			cmd('cd ./Lib/distutils')
			cmd('echo [build] >> distutils.cfg')
			cmd('echo compiler=mingw32 >> distutils.cfg')
		self.mingw = mingw
		
	def compile(self):
		from os import system as cmd
		if self.method == 'cxfreeze' or 'py2exe' or 'py2app':
			setup = open('setup.py', 'w')
		if self.method == 'cxfreeze':
			script = '''
from cx_Freeze import setup, Executable
import sys
if sys.platform == 'win32':
        base = 'win32gui'
setup(name='Autogen',version='0.1',executables=[Executable(%s)],base=base)
''' % self.file
		elif self.method == 'py2exe':
			script = '''
from distutils.core import setup
import py2exe

setup(console=[%s])
''' % self.file
		elif self.method == 'py2app':
			script = '''
from distutils.core import setup
import py2app

setup(console[%s])
''' % self.file
		if self.method != 'shebang':
			setup.write(script)
			setup.close()
			cmd('python setup.py build')
	def__del__(self):
		from os import system as cmd
		cmd('del setup.py')
            


