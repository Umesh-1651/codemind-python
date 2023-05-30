t=int(input())
l=list(map(int,input().split()))
cnt=0
for i in l:
    cnt=cnt+i
cnt=int(cnt/t)
for i in l:
    if(cnt==i):
        print("True")
        break
else:
    print("False")