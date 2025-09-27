import math
def tetration(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        power = tetration(x, n-1)
        return x ** power

print("Proverka:")
print("?2 =", tetration(2, 2))  
print("?2 =", tetration(2, 3)) 
print("?2 =", tetration(2, 4)) 

print("\nSchitaem ?5:")
result_3_5 = tetration(5, 3)
print("?5 =", result_3_5)

digits_3_5 = len(str(result_3_5))
print("cifr v chisle ?5:", digits_3_5)

print("\nSchitaem ?2:")


log_result = tetration(2, 4) * math.log10(2)
digits_5_2 = int(log_result) + 1

print("cifr v chisle ?2:", digits_5_2)

print("\nOtvet:")
print("?5 sostoit iz", digits_3_5, "cifr")
print("?2 sostoit iz", digits_5_2, "cifr")
