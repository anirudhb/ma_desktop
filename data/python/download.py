import sys
from os import system as cmd
cmd('wget -E -H -k -p -r --convert-links '+sys.argv[1])
