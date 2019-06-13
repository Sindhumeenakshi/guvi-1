x=int(input())
l1=list(map(int,input().strip().split()))[:x]
l1.sort()
a=l1[int(len(l1)/2)]
print(a)
