import sys, os, math, array, time

#floyd warshall for all-pairs shortest path


def uniquePush(x,lineNum,uniqueNum):
    if x == 0:
        return
    try:
        uniqueNum.index(x)
    except ValueError:       
        uniqueNum.append(x)

def getIndex(uniqueNum,num):
    for x in range(len(uniqueNum)):
        if uniqueNum[x] == num:
            return x
    return -1

def main():
    case = 0
    lineZeroCnt = 0 
    lineNum = []
    uniqueNum = []
    for raw in sys.stdin:
        lineNum.clear()
        uniqueNum.clear()
        line = raw.split('\n')[0]
        rawNums = line.split(' ')
        # ==== pass 1 find unique node number and initialize matrix ====
        for i in rawNums:
            if i == '':
                continue
            if i == 0:
                lineZeroCnt+=1
            else:
                lineZeroCnt-=1
            if lineZeroCnt == 2:
                lineZeroCnt=0
                break
            uniquePush(int(i), lineNum, uniqueNum)

        maxNum = len(uniqueNum)
        Distance = [[0 for x in range(maxNum)] for y in range(maxNum)]
        #Predecessor = [[0 for x in range(maxNum)] for y in range(maxNum)]

        for x in range(maxNum):
            for y in range(maxNum):
                if x == y:
                    Distance[x][y] = 0
                else:
                    Distance[x][y] = 999 

        #for x in range(maxNum):
        #    for y in range(maxNum):
        #        Predecessor[x][y] = None

        # ==== pass 2 fillup relation ====
        p2cnt = 0
        fromA = -1
        toB = -1
        lastZero = 0
        for k in range(len(rawNums)):
            if rawNums[k] == '':
                continue
            p2cnt+=1
            if p2cnt % 2 == 0 and int(rawNums[k]) != 0:
                toB = getIndex(uniqueNum, int(rawNums[k]))
            elif p2cnt % 2 == 1 and int(rawNums[k]) != 0:
                fromA = getIndex(uniqueNum, int(rawNums[k]))
            elif int(rawNums[k]) == 0:
                if lastZero == 0:
                    lastZero+=1
                else:
                    break
            if fromA != -1 and toB != -1:
                Distance[fromA][toB] = 1
                #Predecessor[fromA][toB] = uniqueNum[fromA]
                fromA = -1
                toB = -1
                lastZero = 0
        if len(uniqueNum)== 0:
            exit(0)
        # ==== pass 3 find shortest path, Floyd-Warshall ====
        # think: pick two node and do from and to caculate
        for k in range(maxNum): #take 1 from set to be mid node
            for x in range(maxNum): #fromA
                if Distance[x][k] == 999 or k == x:
                    continue
                for y in range(maxNum): #toB
                    if k == y:
                        continue
                    #if Predecessor[x][k] == None:
                    #    continue
                    if Distance[x][y] > Distance[x][k] + Distance[k][y]:
                        Distance[x][y] = Distance[x][k] + Distance[k][y]
                        #Predecessor[x][y] = uniqueNum[k]
        iSum = 0
        for x in range(maxNum):
            if x == y:
                continue
            for y in range(maxNum):
                iSum += Distance[x][y]
        average = iSum/((maxNum*maxNum)-maxNum)

        case+=1
        print('Case %d: average length between pages = %.3f clicks' % (case, average))

if __name__ == '__main__':
    main()
