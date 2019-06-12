n=int(input())
k=int(input())
l1=list(map(int,input().strip().split()))[:n]
a=sum(l1[:k])
print(a)
