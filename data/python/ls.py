def ls(dir):
	from os import system as cmd
	import os
	cmd('cd ' + dir + ';ls>temp')
	os.chdir(dir)
	with open('temp') as table:
		lines = table.readlines()
		for line in lines:
			if line != 'temp' and line != '\n' and line != '':
				print line
			pass
	cmd('rm temp')

