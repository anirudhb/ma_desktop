class StringIOContextManager:
    def __init__(self, stringio):
        pass

	def __enter__(self, stringio):
		from cStringIO import StringIO as cstrio
		if not isinstance(stringio, cstrio): raise TypeError("Error: stringio must be a cStringIO object")
		return stringio
	
	def __exit__(self):
		try:
			stringio.close()
		except IOError:
			return True
		return False
