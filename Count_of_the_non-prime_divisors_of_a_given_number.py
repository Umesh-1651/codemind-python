def is_prime(n):
    if n==1:
        return 0
    for i in range(2,n):
        if n%i==0:
            return 0
    return 1
    
a=int(input())
cnt=0
for i in range(1,a+1):
    if is_prime(i)==0:
        if a%i==0:
            cnt=cnt+1
print(cnt)