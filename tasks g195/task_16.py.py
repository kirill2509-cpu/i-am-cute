n = int(input())
a = list(map(int, input().split()))
b = [0] * (n + 1)

for k in range(1, n + 1):
    p = a[k - 1]
    b[p] = k

print(' '.join(str(b[i]) for i in range(1, n + 1)))