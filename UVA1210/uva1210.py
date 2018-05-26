import sys, os, array, math

global prime
global ans

def erasto(n):
    marks = [1]*n
    i = 2
    while math.pow(i,2) < n :
        if marks[i-1] == 1:
            j = 2
            while i*j < n+1:
                marks[i*j-1] = 0
                j+=1
        i+=1
    k= 1
    while k < n:
        if marks[k] == 1:
            prime.append(k+1)
        k+=1

def calRepresentation():
    global prime
    global ans
    x=0
    while x < len(prime):
        y=x+1
        ans[prime[x]-1]+=1
        tmp=prime[x]
        while y < len(prime):
            tmp+=prime[y]
            if tmp < 10000 :
                ans[tmp-1]+=1
            y+=1
        x+=1
    

def main():
    global ans
    for line in sys.stdin:
        num = int(line)
        if num == 0:
            exit(0)
        else:
            print(ans[num-1])

def init():
    global prime
    global ans
    prime = []
    ans = [0]*10000
    erasto(10000)
    #print(prime)
    #print(prime)
    calRepresentation()
    #print(ans)

if __name__ == "__main__":
    init()
    main()
