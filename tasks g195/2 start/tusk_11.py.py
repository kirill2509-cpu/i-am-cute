def factorial(n):
    if n < 0:
        return None
    if n == 0:
        return "1"
    return str(n * int(factorial(n - 1)))
n = int(input("VVedite chislo: "))

result = factorial(n)
print (f"otvet: {result}")
