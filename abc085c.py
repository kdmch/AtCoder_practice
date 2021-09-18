n,p=map(int, input().split())
for x in range(n+1):
    for y in range(n-x+1):
        z=n-x-y
        if x*10000+y*5000+z*1000 == p:
            print(x,y,z)
            exit()
print(-1,-1,-1)