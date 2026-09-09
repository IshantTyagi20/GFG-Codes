n = int(input())

# code here
a = 0
while a < n:
    row = ""
    for j in range((a * (a + 1)) // 2 + 1,(a * (a + 1)) // 2 + 2 + a):
        row += str(j) + " "
    print(row)
    a += 1