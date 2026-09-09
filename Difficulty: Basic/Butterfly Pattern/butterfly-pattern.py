n = int(input())

# code here
max_stars = 2*n - 1
for i in range(1, n):
    stars = i*2
    spaces = max_stars - stars

    print('*'*(stars//2),end = "")
    print(" "*spaces, end = "")
    print('*'*(stars//2))
print('*'*max_stars)
for i in range(n-1,0,-1):
    stars = i*2
    spaces = max_stars - stars

    print('*'*(stars//2),end = "")
    print(" "*spaces, end = "")
    print('*'*(stars//2))