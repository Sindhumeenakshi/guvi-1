x=int(input())
def fact(x):
  if (x==1):
    return x
  else:
    return x*fact(x-1)
if (x==0):
  print("1")
else:
  print(fact(x))
