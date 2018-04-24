#!/usr/bin/env python

EXP = {
0x0: 0b0000, 0x1: 0b0010, 0x2: 0b0100, 0x3: 0b1000,
0x4: 0b0011, 0x5: 0b0110, 0x6: 0b1100, 0x7: 0b1011,
0x8: 0b0101, 0x9: 0b1010, 0xA: 0b0111, 0xB: 0b1110,
0xC: 0b1111, 0xD: 0b1101, 0xE: 0b1001, 0xF: 0b0001}
EXP_INV = {}

SUB = {
0b0000: 0b0011, 0b0001: 0b1000, 0b0010: 0b1111, 0b0011: 0b0111,
0b0100: 0b0001, 0b0101: 0b0010, 0b0110: 0b1011, 0b0111: 0b000,
0b1000: 0b1100, 0b1001: 0b1110, 0b1010: 0b1010, 0b1011: 0b0110,
0b1100: 0b1001, 0b1101: 0b1101, 0b1110: 0b0101, 0b1111: 0b0100}
SUB_INV = {}

for i in EXP:
  EXP_INV[EXP[i]] = i
  SUB_INV[SUB[i]] = i

def Prod(a, b):
    if a == 0 or b == 0:
        return 0
    else:
        exp = EXP_INV[a] + EXP_INV[b]
        if exp >= len(EXP):
            exp = exp % len(EXP) + 1

        return EXP[exp]

def SubBytes(a0, a1, a2, a3):
    return [SUB[a0], SUB[a1], SUB[a2], SUB[a3]]

def ShiftRows(a0, a1, a2, a3):
    return [a0, a3, a2, a1]

def MixColumns(a0, a1, a2, a3):
    C = [0b0011, 0b0010, 0b0010, 0b0011]

    return [Prod(a0, C[0])^Prod(a1, C[2]), Prod(a0, C[1])^Prod(a1, C[3]), Prod(a2, C[0])^Prod(a3, C[2]), Prod(a2, C[1])^Prod(a3, C[3])]

def AddRoundKey(k0, k1, k2, k3, a0, a1, a2, a3):
    return [k0^a0, k1^a1, k2^a2, k3^a3]

