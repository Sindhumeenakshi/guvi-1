p=int(input())
l1=list(map(int,input().strip().split()))[:p]
for i in range(0,p):
  print(l1[i],'',i)
