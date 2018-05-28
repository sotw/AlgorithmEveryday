import sys, os, math, array

def ifact(n):
    ret = 1
    for i in range(1,n+1):
        ret = ret*i
    return ret

def Combination(n,m):
    return ifact(n)/(ifact(m)*ifact(n-m))

def H(n,m):
    return Combination(n+m-1,m)

def main():
    for raw in sys.stdin:
        line = raw.split('\n')
        number = int(line[0])
        if number == 0:
            return
        if number == 1:
            print(1)
            continue
        if number == 2:
            print(2)
            continue
        if number > 2:
            ans=0
            ans+=1 #All Vertical counts one
            maxFlatStyle = math.floor(number/2)
            k = 1
            while k <= maxFlatStyle :
                ans+=H(k+1,number-(k*2))
                k+=1
            print(int(ans))

if __name__ == "__main__":
    main()
