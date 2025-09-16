def kb_to_b(kb): return kb * 1024
def b_to_kb(b): return b / 1024

choice = input("1 - KB?B  2 - B?KB: ")

if choice == "1":
    result = float(input("KB: ")) * 1024
    print(f"Baiti: {result}")
elif choice == "2":
    result = float(input("B: ")) / 1024
    print(f"Kilobaiti: {result}")
else:
    print("Error")
