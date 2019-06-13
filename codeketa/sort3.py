p=int(input())
l1=list(map(int,input().strip().split()))[:p]
l1.sort()
print(*l1)
