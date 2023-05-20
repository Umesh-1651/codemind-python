p,r,t = map(float,input().split())
amt = p * ((1 + (r/100))**t)
print("%.2f"%amt)