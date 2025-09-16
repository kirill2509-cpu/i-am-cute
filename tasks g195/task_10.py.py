a = int(input("Enter the A number: "))
b = int(input("Enter the B number: "))
print(f"Before swap: a = {a}, b = {b}")
a = a + b
b = a - b
a = a - b
print(f"After swap: a = {a}, b = {b}")