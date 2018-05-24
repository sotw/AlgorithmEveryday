import sys, os, math, array

global N
global myList

myList=[]

class entry:
    def __init__(self,a,b,diff):
        self.a = a
        self.b = b
        self.diff = diff
    def __repr__(self):
        return '($d,%d,%d)' % (self.a, self.b, self.diff)

def perform():
    global myList
    minDiff = -1
    for x in myList:
        if minDiff == -1:
            minDiff = x.diff
        elif minDiff != x.diff:
            return 1
    return 0

def main():
    global myList
    STATE=0 #0: indicate how many line gonna input 1: receive line..
    lnCnt=0
    ret = 0
    totalCase=0
    curCase=0
    for line in sys.stdin:
        if len(line) == 1: #simply skip space
            continue
        if totalCase == 0:
            totalCase = int(line.split('\n')[0])
            continue
        if STATE==0 :
            N = int(line.split('\n')[0])
            STATE=1
            myList.clear()
            curCase+=1
        elif STATE==1:
            e = line.split(' ')
            if len(e)!=2 :
                continue
            myList.append(entry(int(e[0]),int(e[1]),abs(int(e[0])-int(e[1]))))
            lnCnt+=1
            if lnCnt == int(N) :
                ret = perform()
                if ret == 0:
                    print("yes")
                else:
                    print("no")
                if curCase != totalCase:
                    print("")
                ret = 0
                lnCnt=0
                STATE=0
                continue      

if __name__ == "__main__" :
    main()
