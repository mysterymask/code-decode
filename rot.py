#!/usr/bin/python
#-*- coding:utf-8 -*-

import sys
    
def rot5(s):
    res = ""
    for c in s:
        tmp = (ord(c)-48+5)%10+48
        res = res+chr(tmp)
    return res


def rot13(s, OffSet=13):
    def encodeCh(ch):
        f=lambda x: chr((ord(ch)-x+OffSet) % 26 + x)
        return f(97) if ch.islower() else (f(65) if ch.isupper() else ch)
    return ''.join(encodeCh(c) for c in s)

def rot18(s):
    res = ""
    for c in s:
        if ord(c)>=48 and ord(c) <=57:
            tmp = (ord(c)-48+5)%10+48
            res = res+chr(tmp)
        else:
            if c.islower():
                offset = 97
            elif c.isupper():
                offset = 65
            tmp = (ord(c)-offset+13)%26+offset
            res = res+chr(tmp)
    return res

def rot47(s):
    res = ""
    for c in s:
        tmp = (ord(c)-33+47)%94+33
        res = res+chr(tmp)
    return res


def main():
    print '*'*30+'  INPUT  '+'*'*30
    raw_str = raw_input("INPUT：")
    print '*'*30+'  OUPUT  '+'*'*30
    if raw_str.isalpha():
        print "USE ROT13: \033[1;32m"+rot13(raw_str)+ "\033[0m"
    if raw_str.isdigit():
        print "USE ROT5: \033[1;32m"+rot5(raw_str)+ "\033[0m"
    if raw_str.isalnum():
        print "USE ROT18: \033[1;32m"+rot18(raw_str)+ "\033[0m"
    
    print "USE ROT47: \033[1;32m"+rot47(raw_str)+ "\033[0m"
    print '*'*69

if __name__ == '__main__':
    main()

