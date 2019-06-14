 o=int(input())
  p=int(input())
  cnt=0
  l2=list(map(int,input().strip().split()))[:o]
  for i in range(0,o):
    if(l2[i]==p):
      cnt=cnt+1
  print(cnt)
