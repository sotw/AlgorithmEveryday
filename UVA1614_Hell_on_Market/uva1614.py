import sys, os, array, math

#split to two pile, one pile is 1, one pile is -1
#sort and pick up from big one and greedy to get the number of sum/2

global N
global inputNumList

inputNumList = []

class myEntry():
    def __init__(self,index,value,ret):
        self.index = index
        self.value = value
        self.ret = ret
    def __repr__(self):
        return '(%d,%d,%d)' % (self.index, self.value, self.ret)

def hellOnMarkets():
    global N
    global inputNumList
    helfSum = 0
    for x in inputNumList:
        helfSum += x.value
    if helfSum % 2 == 1:
        print("No")
    else:
        print("Yes")
        helfSum/=2
        inputNumList.sort(key=lambda myEntry: myEntry.value, reverse=True)
        for x in range(N):
            if helfSum >= inputNumList[x].value:
                helfSum -= inputNumList[x].value
                inputNumList[x].ret = 1
        inputNumList.sort(key=lambda myEntry: myEntry.index)
        for y in range(N):
            if y == N-1:
                print(inputNumList[y].ret)
            else:
                print(inputNumList[y].ret, end=' ')

def main():
    global N
    global inputNumList
    LSN = 0
    for line in sys.stdin:
        if len(line) == 1:
            continue
        line = line.strip('\n')
        LSN+=1
        if LSN % 2 == 1 : #max numebrs of input
            N = int(line)
            ret = [-1 for i in range(N)]
        else:
            numbers = line.split(' ')
            inputNumList.clear()
            for x in range(N):
                inputNumList.append(myEntry(x,int(numbers[x]),-1))
            hellOnMarkets()
        
if __name__ == "__main__":
    main()
