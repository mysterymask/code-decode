#!/usr/bin/python
#-*-:coding:utf-8:-*-
import sys

DICT={'A':'aaaaa','B':'aaaab','C':'aaaba','D':'aaabb','E':'aabaa','F':'aabab','G':'aabba','H':'aabbb','I':'abaaa','J':'abaab','K':'ababa','L':'ababb','M':'abbaa',\
            'N':'abbab','O':'abbba','P':'abbbb','Q':'baaaa','R':'baaab','S':'baaba','T':'baabb','U':'babaa','V':'babab','W':'babba','X':'babbb','Y':'bbaaa','Z':'bbaab',\
            'a':'AAAAA','b':'AAAAB','c':'AAABA','d':'AAABB','e':'AABAA','f':'AABAB','g':'AABBA','h':'AABBB','i':'ABAAA','j':'ABAAA','k':'ABAAB','l':'ABABA','m':'ABABB',\
            'n':'ABBAA','o':'ABBAB','p':'ABBBA','q':'ABBBB','r':'BAAAA','s':'BAAAB','t':'BAABA','u':'BAABB','v':'BAABB','w':'BABAA','x':'BABAB','y':'BABBA','z':'BABBB'}

def usage():
    print '*'*60
    print "Usage: python bacon.py -[e |d <-r>]"
    print "-e       Encode text"
    print "-d       Decode ciphertext"
    print "-r        Init  ciphertext"
    print "-h       for help."
    print '*'*60
    exit(0)


def init_ciphertext(s):
    return "".join([('a' if i.isupper() else 'b') for i in s])

def invert_dict():  
    return dict((v,k) for k,v in DICT.iteritems())

def decode(s,flag = False):
    sub = s.split(" ")
    rDict = invert_dict()
    for ch in sub:
        if flag:
            sys.stdout.write(rDict[init_ciphertext(ch)])
        else:
            sys.stdout.write(rDict[ch])
    print ""

def encode(s):
    for char in s:
        print DICT[char],

def main():
    args = sys.argv

    if len(args) < 2 or '-h' in args:
        usage()
    if "-r" in args:
        iflag = True
    else:
        iflag = False

    if '-e' in args:
        flag = False
    elif '-d' in args:
        flag = True
    else:
        usage()

    print '*'*60
    raw_str = raw_input("\033[1;32mINPUT:\033[0m")
    print "\033[1;32mOUPUT:\033[0m",
    if flag:
        result = decode(raw_str,iflag)
    else:
        result = encode(raw_str)
    print '*'*60

if __name__ == '__main__':
    main()