import sys, os, array, math

def iFact(n): #just for memory refresh, I knew there is a factorial module inside math
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    return fact

def combination(n,m):
    return iFact(n)/(iFact(m)*iFact(n-m))

def main():
    for line in sys.stdin:
        numbers = line.split()
        if(len(numbers)!=2):
            continue
        n = int(numbers[0])
        m = int(numbers[1])
        if n == 0 and m == 0:
            exit(0)
        if not(n >= 5 and 100 >= n):
            continue
        if not(m >= 5 and 100 >= m):
            continue
        ret = combination(n,m)
        print('%d things taken %d at a time is %d exactly.' % (n,m,ret))

if __name__ == "__main__":
    main()
