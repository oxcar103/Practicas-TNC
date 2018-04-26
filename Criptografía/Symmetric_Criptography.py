#!/usr/bin/env python

from MiniAES import MiniAES

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

PrintBin(MiniAES(0x1234, 0x5678))
