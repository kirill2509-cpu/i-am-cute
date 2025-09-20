def evenFibSum(limit):
    a, b = 1, 2
    s = 0
    
    while a <= limit:
        if a % 2 == 0:
            s += a
        a, b = b, a + b
    
    return s


result = evenFibSum(4000000)
print(result)  