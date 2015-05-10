import sys



def encrypt(text, charpass):
    """
    :param text: str
    :param charpass: str
    :return: str
    """
    s = ''
    for l in text:
        s += str(ord(l) + ord(charpass))
    return s


def decrypt(num, charpass):
    """
    :param num: int or str
    :param charpass: str
    :return: str
    """
    if type(num) != str:
        num = str(num)
    l = split_by_len(num, 3)
    text = ''
    for n in l:
        l[l.index(n)] = str(int(n) - ord(charpass))
    return text.join([chr(int(n)) for n in l])


def split_by_len(text, lentosplit):
    tmp = ''
    l = []
    if len(text) < lentosplit:
        return [text]
    for letter in text:
        tmp += letter
        if len(tmp) > lentosplit:
            l.append(tmp)
            tmp = ''
    if tmp:
        l.append(tmp)
    return l


class Cipher(object):
    def __init__(self, password, name, buf=''):
        """
        :param secretchr: str
        :param buf: str
        :param name: str
        :return: None
        """
        super(Cipher, self).__init__()
        self.buf = buf
        self.passwd = password
        self.name = name

    def append_bigdata(self, s):
        """
        :param s: str
        :return: None
        """
        if len(s) > 64 * 1024:
            for w in split_by_len(s, 64 * 1024):
                self.buf += w

    def append(self, s):
        """
        :param s: str
        :return: None
        """
        self.buf += s

    def update(self, s):
        """
        :param s: str
        :return: None
        """
        self.buf = s

    def clear(self):
        """
        :return: None
        """
        self.buf = ''

    def encrypt(self):
        """
        :return: str
        """
        return hex(int(encrypt(self.buf, self.passwd)))[2:]

    def decrypt(self):
        """
        :return: str
        """
        return decrypt(int(self.buf, 16), self.passwd)

    def randompass(self, length=8):
        """
        :return: str
        """
        import random
        random.seed()
        ch = [random.randint(97, 122) for i in range(length)]
        return ''.join([chr(c) for c in ch])

    def __eq__(self, other):
        assert isinstance(other, Cipher)
        return self.buf == other.buf and self.chr == other.chr

    def __hash__(self):
        return hash(hash(self.buf) + hash(self.chr))

    def __hex__(self):
        import binascii
        s = binascii.hexlify(self.buf)
        return hex(ord(self.chr)) + s

    def __int__(self):
        return int(hex(self), 16)

    def __gt__(self, other):
        assert isinstance(other, Cipher)
        return ord(self.chr) > ord(other.chr)

    def __lt__(self, other):
        assert isinstance(other, Cipher)
        return ord(self.chr) < ord(other.chr)

    def __delslice__(self, i, j):
        s = list(self.buf)
        del s[i:j]
        self.buf = str(s)

    def __getslice__(self, i, j):
        return self.buf[i:j]

    def __getitem__(self, i):
        return self.buf[i]

    def __delitem__(self, i):
        s = list(self.buf)
        del s[i]
        self.buf = str(s)

    def __str__(self):
        return "Cipher object %s: buf=%s, chr=%s" % (self.name, self.buf, self.chr)
    
    def __repr__(self):
        return "<Cipher object %s (built-in)>" % self.name

if __name__ == "__main__":
    print encrypt("anirudh", "a")
