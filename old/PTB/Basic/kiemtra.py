L,K = list(map(int,input().split()))
N = input()

for i in "QWERTYUIOPASDFGHJKLZXCVBNM":
    d=0
    for j in range(L):
        if N[j] == i :
            d += 1
        if d >= K:
            print(i,end="")
            break
        
