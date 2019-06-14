r=int(input())
a=0
b=1
i=1
while(i<=r):
  if(i<=1):
    n=i
  else:
    n=a+b
    a=b
    b=n
  print(n,end=' ')
  i=i+1
