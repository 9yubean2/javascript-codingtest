# BOJ 1568 새
n = int(input())
result = 0
k = 1

while n != 0:
    if k > n:
        k = 1
    n -= k
    k += 1
    result +=1

print(result)
