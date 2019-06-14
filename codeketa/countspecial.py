x=input()
count=0
a=0
b=0
for i in x:
  if (i.isalpha()):
    a=a+1
  elif(i.isdigit()):
    b=b+1
  else:
    count=count+1
print(count
