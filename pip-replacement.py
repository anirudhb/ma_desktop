import tarfile
import gzip
import os
import shutil
import urllib
import sys
from bs4 import BeautifulSoup as BS
from bs4 import NavigableString as NS

packages = sys.argv[1:]

for package in packages:
	url = urllib.urlopen("https://pypi.python.org/pypi/%s" % package)
	soup = BS(url)
	global version
	version = str(list(soup.descendants)[266])[len(package)+1:] # easiest way
	# worst non-working way
	#for div in soup.body:
	#	if not isinstance(div, NS) and div.name == "div" and 'id' in div.attrs and div['id'] == "content-body":
	#		for div1 in div.children:
	#			if not isinstance(div1, NS) and div1.name == "div" and 'id' in div1.attrs and div1['id'] == "body-main":
	#				for div2 in div1.children:
	#					if not isinstance(div2, NS) and div2.name == "div" and 'id' in div2.attrs and div2['id'] == "content":
	#						for div3 in div2.children:
	#							if not isinstance(div3, NS) and div3.name == "div" and 'class' in div3.attrs and div3['class'] == "section":
	#								version = str(div3.h1.string.split(" ")[1])
	#								print unicode(div3.contents[0].contents[0]).split(" ")[1]
	#								break
	url.close()
	del url, soup
	try:
		os.mkdir("/tmp/pipr-build-tmp")
	except:
		pass
	os.chdir("/tmp/pipr-build-tmp")
	urllib.urlretrieve("https://pypi.python.org/packages/source/%s/%s/%s-%s.tar.gz" % (package[0], package, package, version), "%s-%s.tar.gz" % (package, version))
	#print tarfile.is_tarfile("%s-%s.tar.gz" % (package, version))
	gz = gzip.open("%s-%s.tar.gz" % (package, version))
	tar0 = open("%s-%s.tar" % (package, version), 'w')
	tar0.write(gz.read())
	tar0.close()
	gz.close()
	del gz, tar0
	tar = tarfile.open("%s-%s.tar" % (package, version))
	tar.extractall()
	os.chdir("%s-%s" % (package, version))
	os.system("python setup.py install --user")
