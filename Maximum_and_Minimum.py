n=int(input())
li=list(map(int,input().split()))
sli = set(li)
fli= []
for i in sli:
    c=0
    for j in li:
        if i==j:
            c+=1
    if c==i:
        fli.append(i)
if(len(fli) == 0):
    print("-1")
else:
    print(min(fli),max(fli),end="")