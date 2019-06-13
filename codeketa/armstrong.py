n=int(input())
t=n
sum=0
while t>0:
  d=t%10
  sum=sum+(d**3)
  t=t//10
if(n==sum):
  print("yes")
else:
  print("no")
