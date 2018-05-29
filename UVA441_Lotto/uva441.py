import os, sys, math, array

global myList
myList = []

class myEntry():
    maxNums = 0
    maxMarked = 0
    def __init__(self, value, mark):
        self.value = value
        self.mark = mark
    def markMe(self):
        self.mark = 1
        myEntry.maxMarked+=1
        #print("mark value %d" % (self.value))
    def unMarkMe(self):
        self.mark = 0
        myEntry.maxMarked-=1
        #print("unmark value %d" % (self.value))
    def __repr__(self):
        return ('(%d,%d)' % (self.index,self.value))

def printMarkedList():
    markCnt = 0
    for x in myList:
        if x.mark == 1 :
            markCnt+=1
            if markCnt != 6 :
                print('%d' % (x.value), end=(' '))
            else:
                print('%d' % (x.value))

def backtracking(pos):
    #end condition
    if (myEntry.maxMarked == 6):
        printMarkedList()
        return
    for pos in range(pos,myEntry.maxNums):
        myList[pos].markMe()
        if pos+1 < myEntry.maxNums+1: #need to add one to meet end condition in the corner case
            backtracking(pos+1)
        myList[pos].unMarkMe()

def main():
    inputCnt=0
    for rawLine in sys.stdin:
        inputCnt+=1
        line = rawLine.split('\n')
        numbers = line[0].split(' ')
        if int(numbers[0]) == 0:
            exit(0)
        else :
            numCnt=0
            for x in numbers:
                if numCnt == 0:
                    myEntry.maxNums = int(x)
                    myEntry.maxMarked = 0
                else:
                    myList.append(myEntry(int(x),0))
                numCnt+=1
            if inputCnt > 1:
                print('')
            backtracking(0)
        myList.clear()

if __name__ == "__main__":
    main()
