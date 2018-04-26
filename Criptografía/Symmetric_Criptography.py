from MiniAES import MiniAES

def PrintBin(args):
    msg=""

    for i in args:
        binary = bin(i).split("b")[-1][-4:]
        binary = '0'*(4-len(binary))+binary
        msg+=binary + " "

    print(msg)

PrintBin(MiniAES(0x1234, 0x5678))
