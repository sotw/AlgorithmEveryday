import os, sys, math, array
global tNums
global cache

def gInit():
    global cache
    cache = [0]*1000000

def treeNplusOne(n):
    if n%2 == 1 :
        return 3*n+1
    else :
        return n>>1

def circleLength(n):
    global cache
    if n == 1:
        return 1
    if n < 1000000 and cache[int(n)] != 0 :
        return cache[int(n)]
    length = 1 + circleLength(treeNplusOne(int(n)))
    if n < 1000000:
        cache[int(n)]=length
    return length


def main():
    global tNums
    gInit()
    clmax=1
    #while True:
    #    line = sys.stdin.readline()
    #    if not line:
    #        break
    for line in sys.stdin:
        tNums = line.split()
        if(len(tNums)==2):
            for x in range(min(int(tNums[0]),int(tNums[1])),max(int(tNums[0]),int(tNums[1])+1)):
                clmax=(max(clmax, circleLength(x)))
            print("%d %d %d" %(int(tNums[0]),int(tNums[1]),clmax))
            clmax=1
                        
if __name__ == "__main__":
    gInit()
    main()
    exit(0)
