def pickme(k1):
    k2 = k1 + 1
    for n in range(1, 10000):
        x = n * k1
        y = n * k2
        if sorted(str(x)) == sorted(str(y)):
            return n
k1 = int(input())
res = pickme(k1)
print(res)