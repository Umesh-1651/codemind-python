t=int(input())
l=list(map(int,input().split()))
se=int(input())
cnt=0
for i in l:
    if(se == i):
        print("True")
        break
else:
    print("False")