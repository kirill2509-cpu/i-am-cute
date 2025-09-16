def find_min_number(arr):
    return min(arr)

input_numbers = input("Vvedite chisla cherez probel: ")

numbers = list(map(int, input_numbers.split()))

min_number = find_min_number(numbers)

print("Massiv:", numbers)
print("Minimalnoe chislo:", min_number)
