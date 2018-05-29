import sys, os, math, array

global myDict
global scrumbTarget
myDict = []
scrumbTarget = []

class myWord():
    totalWords = 0
    def __init__(self, wordLen, word, usedList, ans):
        self.word = word
        self.wordLen = wordLen
        self.usedList = usedList
        self.ans = ans
    def renewUsedList(self):
        for x in range(len(self.usedList)):
            self.usedList[x] = -1
    def checkUsedList(self):
        for x in range(len(self.usedList)):
            if self.usedList[x] == -1:
                return -1
        tmpAns = ''
        for y in range(self.wordLen):
            for z in range(self.wordLen):
                if self.usedList[z] == y:
                    tmpAns+=self.word[z]
        self.ans.append(tmpAns)
        return 0
    def sortAns(self):
        if len(self.ans) > 1:
            self.ans.sort()

def renewAllUsedList():
    for x in scrumbTarget:
        x.renewUsedList()

def startDeScrumb():
    for x in myDict:
        renewAllUsedList()
        for y in scrumbTarget:
            if y.wordLen != len(x):
                continue
            for dIdx in range(len(x)):
                for idx in range(y.wordLen):
                    if x[dIdx] == y.word[idx]:
                        if y.usedList[idx] == -1:
                            y.usedList[idx] = dIdx
                            break
            y.checkUsedList()

def output():
    for x in scrumbTarget:
        if len(x.ans) == 0:
            print('NOT A VALID WORD')
            print('******')
        else:
            x.sortAns()
            for y in x.ans:
                print(y)
            print('******')

def main():
    global myDict
    STATE = 0
    for rawLine in sys.stdin:
        line = rawLine.split('\n')[0]
        if line == 'XXXXXX':
            STATE+=1
            if STATE == 2:
                startDeScrumb()
                output()
            else:
                continue
        if STATE == 0:
            myDict.append(line)
        elif STATE == 1:
            usedList = [-1]*len(line)
            ans = []
            scrumbTarget.append(myWord(len(line),line,usedList,ans))

if __name__ == '__main__':
    main()
