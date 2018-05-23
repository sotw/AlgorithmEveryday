import os, sys, math, array

global PositiveArray
global STATEDict
PositiveArray = { 1:'1',2:'4',3:'78'}
STATEDict = { 1:'+',2:'-',3:'*',4:'?'}

def positiveString(n):
    global PositiveArray
    ret = {}
    for x in list(PositiveArray.values()):
        try:
            pos = n.index(x)
            ret[x] = pos
        except ValueError:
            continue
    return ret

def judge(n):
    global PositiveArray
    global STATEDict
    STATE = 4
    length = len(n) -1 #exclude \n
    RETS = positiveString(n)
    for key, value in RETS.items():
        if value == -1:
            STATE=4
        else:
            STATE=1
            startPos = value
            endPos = value + (len(key)-1)
            if  endPos+2 <= length-1 and n[endPos+1] == '3' and n[endPos+2] == '5':
                STATE=2
                break
            elif endPos+1 <= length-1 and startPos-1 >= 0 and n[startPos-1] == '9' and n[endPos+1] == '4':
                STATE=3
                break
            elif startPos-3 >= 0 and n[startPos-3] == '1' and n[startPos-2] == '9' and n[startPos-1] == '0':
                STATE=4
                break
    return STATEDict.get(STATE)

def main():
    lineCnt = 0;
    for line in sys.stdin:
        lineCnt+=1
        if lineCnt > 1 : #skip unnecessary input
            print(judge(line))

if __name__ == "__main__":
    main()
