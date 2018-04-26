#!/usr/bin/env python

from MiniAES import EncMiniAES, DecMiniAES

def digits (num, base):
    digits=[]

    while(num != 0):
        digits = [num%base] + digits
        num//=base

    return digits


def PrintBin(args):
    msg=""

    for i in args:
        binary = bin(i).split("b")[-1][-4:]
        binary = '0'*(4-len(binary))+binary
        msg+=binary + " "

    print(msg)

PrintBin(DecMiniAES(digits(0x1234,0x10), EncMiniAES(digits(0x1234,0x10), digits(0x5678,0x10))))
