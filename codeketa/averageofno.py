r=int(input())
lp=list(map(int,input().strip().split()))[:r]
s=0
av=0
for i in range(0,r):
  s=s+lp[i]
av=s//r
print(av)
