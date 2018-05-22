import os, sys, math, array

global tNums
global sequence
global container

def init():
    return

def main():
    global tNums
    global sequence
    global container
    container = []
    for line in sys.stdin:
        tNums = line.split()
        sequence = int(tNums[0])
        container.clear()
        for x in range(0,sequence-1):
            container.append(abs(int(tNums[x+1])-int(tNums[x+2])))
        exceptFlag=0
        for y in range(sequence-1):
            try:
                container.index((y+1))
            except ValueError:
                print("Not jolly")
                exceptFlag=1
                break
        if exceptFlag != 1:
            print("Jolly")


if __name__ == "__main__":
    init()
    main()

