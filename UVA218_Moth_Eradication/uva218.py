import sys, os, math, array

global area
area = []

class point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return ('(%.1f,%.1f)' % (self.x,self.y))

def cross(o,a,b): #AxB positive counter clockwise, negtive clockwise 
    return (a.x-o.x)*(b.y-o.y)-(a.y-o.y)*(b.x-o.x)#AxBy-AyBx

def AndrewsMonotoneChain(case):
    global area
    lower = []
    upper = []
    #sort for x
    area.sort(key=lambda point: (point.x, point.y)) #first sort x(small to large) then sort y(small
    #print(area)
    #lower parts
    for i in area: #discuss 3 points, 2 vectors
        while len(lower) >= 2 and cross(lower[-2], lower[-1], i) <= 0:
            lower.pop()
        lower.append(i)
    #upper parts
    for j in reversed(area):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], j) <= 0:
            upper.pop()
        upper.append(j)
    return lower[:-1] + upper #requirement

def main():
    global area
    regionPts = 0
    STATE = 0
    pointCnt = 0
    case = 0
    for raw in sys.stdin:
        line = raw.split('\n')[0]
        if STATE == 1:
            xy = line.split(' ')
            pointCnt+=1
            if pointCnt <= regionPts:
                area.append(point(float(xy[0]),float(xy[1])))
                if pointCnt == regionPts :
                    if case != 1 :
                        print('')
                    print('Region #%d:' % (case))
                    myList = []
                    myList.clear()
                    if(pointCnt > 2):
                        myList = AndrewsMonotoneChain(case)
                    else:
                        area.sort(key=lambda point: (point.x, point.y)) #first sort x(small to large) then sort y(small
                        for i in area:
                            myList.append(i)
                        myList.append(area[0])
                    fmtList = [] #for clockwise
                    length = 0
                    for i in reversed(myList):
                        fmtList.append(i)
                    for i in range(len(fmtList)):
                        if i != len(fmtList)-1:
                            print(fmtList[i], end='-')
                        else:
                            print(fmtList[i])
                        if i != 0:
                            length += math.sqrt(math.pow(fmtList[i-1].x-fmtList[i].x,2)+math.pow(fmtList[i-1].y-fmtList[i].y,2))
                    print('Perimeter length = %.2f' % length)
            else:
                STATE=0
        if STATE == 0:
            regionPts = int(line)
            STATE=1
            pointCnt = 0
            area.clear()
            case+=1
    return

if __name__ == '__main__':
    main()
