import os, sys, math, array

STATEDict = { 1:'+',2:'-',3:'*',4:'?'}

def judge(n):
    global PositiveArray
    global STATEDict
    STATE = 4
    length = len(n)
    lastPos = length-1
    flag=0
    if n=='1' or n=='4' or n=='78' :
        STATE = 1
        flag = 1
    
    if flag == 0:
        try:
            spos = n.rfind('35')
            if spos+1 == lastPos :
                STATE = 2
                flag = 1
        except ValueError:
            pass

    if flag == 0:
        try:
            spos = n.index('9')
            epos = n.rfind('4')
            if spos == 0 and epos == lastPos:
                STATE = 3
                flag = 1
        except ValueError:
            pass
    
    if flag == 0:
        try:
            spos = n.index('190')
            if spos == 0:
                STATE = 4
        except ValueError:
            pass

    return STATEDict.get(STATE)

def main():
    lineCnt = 0;
    maxLine = 0;
    for line in sys.stdin:
        lineCnt+=1
        stripLine = line.strip('\n')
        if lineCnt == 1:
            maxLine = int(stripLine) + 1
        elif maxLine < lineCnt:
            exit(0)
        elif lineCnt > 1 :
            print(judge(stripLine))

if __name__ == "__main__":
    main()
