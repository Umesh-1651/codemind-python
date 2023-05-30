t=int(input())
l=list(map(int,input().split()))
cnt=0
for i in l:
    cnt=cnt+i
cnt=cnt/t
print("%.2f"%cnt)