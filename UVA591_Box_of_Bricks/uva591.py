import sys, os, math, array

def calculate(setCnt, maxPile, oriPiles):
    allBricks = 0
    for x in oriPiles:
        allBricks+=int(x)
    wall=allBricks/maxPile
    cnt = 0
    for x in oriPiles:
        if int(x) > wall :
            cnt+=int(x)-wall
    print('Set #%d' % setCnt)
    print('The minimum number of moves is %d.' % int(cnt))
    print('')

def main():
    STATE=0 #0 to read how many stacks, 1 to read each pile of stack numbers
    maxPile=0
    oriPiles=[]
    SetCnt = 0
    for line in sys.stdin:
        line= line.strip('\n')
        if STATE == 0:
            maxPile = int(line)
            if maxPile == 0:
                exit(0)
            else:
                SetCnt+=1
            STATE+=1
        elif STATE == 1:
            oriPiles = line.split()
            calculate(SetCnt, maxPile, oriPiles)
            STATE = 0

if __name__ == '__main__':
    main()
