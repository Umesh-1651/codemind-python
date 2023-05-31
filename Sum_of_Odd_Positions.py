t=int(input())
l=list(map(int,input().split()))
cnt=0
ct=0
for i in range(t):
    if(i%2==0):
        cnt+=l[i]
    else:
        ct+=l[i]
print(ct)