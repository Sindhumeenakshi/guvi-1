x=int(input())
l1=list(map(int,input().strip().split()))[:x]
l1.sort()
for i in  range(0,x):
  print(l1[i],end=' ')
