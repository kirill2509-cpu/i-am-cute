r = set()
def g(n):
    if n <= 0:
        return 0
    for i in range(1, n):
        if ((i % 3 == 0) + (i % 5 == 0)) >= 1:
            r.add(i)
    return sum(r)
print(g(25092005))