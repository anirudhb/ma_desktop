#Python Tutorial v3.5 (Version 35)

def ctc(x):
    '''
    (x) = x -> x

    Convert from Farenheit degrees to Celcius degrees.

    Examples:

    >>> ctc(32)
    0
    >>> ctc(212)
    100
    '''
    return (x - 32) * 5 // 9
def ctf(x):
    '''
    (x) = x -> int

    Convert from Celcius degrees to Farenheit degrees.

    Examples:

    >>> ctf(0)
    32
    >>> ctf(100)
    212
    '''
    return x * 9 // 5 + 32
import math
def sqrt(x):
    '''
    (float) float -> float

    Square root a number.

    Examples:

    >>> sqrt(9)
    3.0
    >>> sqrt(0)
    0.0
    '''
    return (math.sqrt(float(x)))
def sqrti():
    '''
    (float) float -> float

    Square root a number. (with input)

    '''
    
    num = float(input("Enter the number to square root:"))
    return (math.sqrt(num))
def pi():
    return (math.pi)

def ch_aeiou(mychar):
    ''' (str) -> bool
    Check if mychar is a vowel or not.
    Y is not treated as a vowel.
    
    >>> ch_aeiou('a')
    True
    >>> ch_aeiou('f')
    False
    '''
    if  mychar == 'a' or mychar == 'A' or mychar == 'e' or mychar == 'E' or mychar == 'i' or mychar == 'I' or mychar == 'o' or mychar == 'O' or mychar == 'u' or mychar == 'U':
        return True
    else:
        return False
    
def cv(s):
    '''
    (s) -> int

    Return the number of vowels in a letter.
    Y is not treated as a vowel.

    >>> cv('AEIOU')
    5
    >>> cv('xyz')
    0
    '''
    vowels = 0
    for char in s:
        if  ch_aeiou(char):
            vowels  = vowels + 1
    return vowels


def chv(str):
    '''
    (str) -> bool

    Return if str has vowels or not.
    Y is not treated as a vowel.

    >>> chv('afr')
    True
    >>> chv('dfr')
    False
    '''
    for char in str:
        if ch_aeiou(char):
            return True
        else:
            return False
def prv(string):
    '''
    (string) str -> str

    Print the letters in string that are vowels.
    Y is not treated as a vowel.

    >>> prv('namespace')
    a
    e
    a
    e
    >>> prv('xfr')
    '''
    for char in string:
        if ch_aeiou(char):
            print(char)
##class PallindromeType():
##    '''reversable str's'''
##    def __init__(self, string):
##        '''Initialize the object'''
##        import random
##        random.seed()
##        self.id = random.randint(0, 10000)
##        self.string = string
##    def ch1(self):
##        return reverse(self) == self
##pallindrome = PallindromeType
class str(str):
    def reverse(self):
        ''' (str) -> str
        Return a reversed version of the string.

        >>> "self".reverse()
        'fles'
        >>> "erf".reverse()
        'fre'
        '''
        rev = ''
        for char in self:
            rev = char + rev
        return rev
def ib(intn):
    ''' (int) -> int
    Return a integer binary representation of intn.

    >>> ib(3544)
    Binary string representation of 3544 is 0b110111011000
    And binary number representation of 3544 is 110111011000

        '''
    bin_str = bin(intn)
    bin_int = int(bin(intn)[2:])
    print('Binary string representation of',intn,'is',bin_str)
    print('And binary number representation of',intn,'is',bin_int)
    return None
def mksh(startdir='.',exitmode=0,wipemode=0):
    import os
    if exitmode == 1:
        import sys
        sys.exit([0])
    if wipemode == 1:
        reply = input('ALL FUNCTIONS WILL BE ERASED!\nDo you want to continue?(y/n)\n')
        if reply == 'y':
            os._exit(0)
        elif reply == 'n':
            rep = input('The shell will be launched.\nDo you want to continue?(y/n)\n')
            if rep == 'n':
                import sys
                sys.exit([0])
            elif rep == 'y':
                pass
    os.chdir(startdir)
    if os.system('start') == 0:
        print('Shell launched sucessfully!')
    else:
        print('Sorry, shell cannot launch sucessfully.')
    return None
import doctest
doctest.testmod()


    

    

    
