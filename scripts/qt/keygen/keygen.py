'''
WARNING: This module must not be named random, os, sys, string, or uuid.
This module implements some uncommon randomization methods and usages.
This module currently implements three classes in the format rank - class - superclass:
	2 - RandomPool - object
	3 - NumberGenerator - object
	1 - KeyGen - object
All of them use the new-style classes and also superclass correctly.
All classes are well-documented and well-commented.
This also has some possible caveats:
	This code only runs on Python 2.
	RandomPool is not on a Windows, UNIX, Linux, or Mac OS X system and fails to function correctly, or it is running on a (micro) Python installation, without the Python standard library.
	NumberGenerator is seperated from RandomPool, or it is running on a (micro) Python installation, without the Python standard library.
	KeyGen is running on a (micro) Python installation, without the Python standard library.
'''
class RandomPool(object):
	'''
	A class that provides a random pool of data.
	When read from, it will provide either random data from /dev/urandom on UNIX/Linux/Mac OS X, or os.urandom(2500) on Windows.
	The data will vary.
	'''
	def __init__(self):
		super(RandomPool, self).__init__() # superclass python 3 style
		import sys
		if sys.platform == "win32": # are we on windows?
			import os
			self.generator = os.urandom
		else:
			self.generator = open("/dev/urandom", 'rb') # binary else escaped characters
	def read(byte): # couldn't use bytes 'cause it was reserved
		import sys
		if sys.platform == "win32":
			return self.generator(2500)[:byte]
		else:
			return self.generator.read(byte)


class KeyGen(object):
	'''
	A class that generates (fake) keys using one of 3 methods:
		1 - UUID manipulation
		2 - String randomization
		3 - System random numbers
	The identifiers for the methods are as follows:
		1 - uuid (default)
		2 - str
		3 - rand
	It generates 29-character long keys (with the dashes).
	It generates 25-character long keys (without the dashes).
	'''
	def __init__(self, method="uuid"):
		super(KeyGen, self).__init__() # superclass python 3 style
		# TODO: remove the random number method because it is less genuine-looking.
		if method == "uuid":
			import uuid
			self.generator = uuid.uuid4
		elif method == "str":
			import string
			self.chars = string.ascii_uppercase + string.digits
		elif method == "rand":
			import random
			self.generator = random.SystemRandom().randint
		self.method = method
	def get_key(self):
		'''
		The main method that implements the key generation function.
		TODO: remove the random number method because it is less genuine-looking.
		This function won't work properly unless it has the resources to complete a specific method, see change_method(3).
		'''
		if self.method == "uuid":
			key = str(self.generator()).upper().replace("-", "")[:5]
			while len(key) != 29:
				key += "-"
				key += str(self.generator()).upper().replace("-", "")[:5]
			return key
		elif self.method == "str":
			import random
			key = ''.join([random.choice(list(self.chars)) for i in range(5)])
			while len(key) != 29:
				key += "-"
				key += ''.join([random.choice(list(self.chars)) for i in range(5)])
			return key
		elif self.method == "rand":
			key = str(self.generator(0, 1000000000000))[:5]
			while len(key) != 29:
				key += "-"
				key += str(self.generator(0, 1000000000000))[:5]
			return key
	def change_method(self, method):
		'''
		Change from one key generation method to another.
		There could be several reasons why the user would like to change the method, i.e. for more 'genuine-ness' or better keys.
		The user could not simply set self.method to whatever they wanted, as that would result in the get_key function looking for resources that aren't created.
		This will not just change self.method, it will create/change the resources needed to use that particular method.
		Most of the time, the user will just change self.method, which means the resources for that particular method are not initialized.
		This is why this function exists, to clean up after the user's changes.
		'''
		self.method = method
		if self.method == "uuid":
			import uuid
			self.generator = uuid.uuid4
		elif self.method == "str":
			import string
			self.chars = string.ascii_uppercase + string.digits
		elif self.method == "rand":
			import random
			self.generator = random.SystemRandom().randint
