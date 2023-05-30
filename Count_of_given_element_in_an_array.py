t=int(input())
l=list(map(int,input().split()))
se=int(input())
cnt=0
for i in l:
    if(se == i):
        cnt=cnt+1
print(cnt)