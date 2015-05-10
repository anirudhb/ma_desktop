import sys
from encrypt import decrypt
print decrypt(open(sys.argv[1]).read(), sys.argv[2])
