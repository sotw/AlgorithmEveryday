import sys, os, math, array

global clsLst
global qusLst
global ansLst
clsLst = []
qusLst = []
ansLst = []

class LETTER():
    def __init__(self,letter,cls):
        self.letter = letter
        self.cls = cls

def genSoundex():
    global clsLst
    for x in range(65,91): #ascii code
        if chr(x) == 'A' or chr(x) == 'E' or \
           chr(x) == 'I' or chr(x) == 'O' or \
           chr(x) == 'U' or chr(x) == 'Y' or \
           chr(x) == 'W' or chr(x) == 'H':
               clsLst.append(LETTER(chr(x),-1))
        elif chr(x) == 'B' or chr(x) == 'P' or \
             chr(x) == 'F' or chr(x) == 'V':
                 clsLst.append(LETTER(chr(x),1))
        elif chr(x) == 'C' or chr(x) == 'S' or \
             chr(x) == 'K' or chr(x) == 'G' or \
             chr(x) == 'J' or chr(x) == 'Q' or \
             chr(x) == 'X' or chr(x) == 'Z':
                 clsLst.append(LETTER(chr(x),2))
        elif chr(x) == 'D' or chr(x) == 'T':
                 clsLst.append(LETTER(chr(x),3))
        elif chr(x) == 'L':
                 clsLst.append(LETTER(chr(x),4))
        elif chr(x) == 'M' or chr(x) == 'N':
                 clsLst.append(LETTER(chr(x),5))
        elif chr(x) == 'R':
                 clsLst.append(LETTER(chr(x),6))
        else:
            print('something wrong, you shouldn\'t find this line')
    return

def soundex(S):
    length = len(S)
    ret = ''
    for x in range(length):
        if x == 0:
            ret+=S[x]
        else:
            for y in clsLst:
                if y.letter == S[x]:
                    if y.cls == -1:
                        break
                    elif x-1 >= 0:
                        for z in clsLst:
                            if z.letter == S[x-1]:
                                if z.cls == y.cls:
                                    pass
                                else:
                                    ret+=str(y.cls)
                                break
                    else:
                        ret+=str(y.cls)
    return ret

def prettyPrint():
    global ansLst
    global qusLst
    print('{0:9}{1:25}{2:}'.format(' ','NAME','SOUNDEX CODE'))
    for x in range(len(ansLst)):
        print('{0:9}{1:25}{2:}'.format(' ',qusLst[x],ansLst[x]))
    print('{0:19}{1:10}'.format(' ','END OF OUTPUT'))

def main():
    global clsLst
    for rawLine in sys.stdin:
        line = rawLine.split('\n')[0]
        if len(line) <= 20 and len(line) > 0:
            qusLst.append(line)
            idxStr = soundex(line)
            fmtStr = idxStr[:4]+'000'
            fmtStr2 = fmtStr[:4]
            ansLst.append(fmtStr2)
    return

if __name__ == '__main__':
    genSoundex()
    main()
    prettyPrint()
