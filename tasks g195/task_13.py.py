name = input("Vvedite vashe imya: ")
age = int(input("Vvedite vash vozrast: "))

from datetime import datetime
current_year = datetime.now().year

year_100 = current_year + (100 - age)

print(f"{name}, vam ispolnitsya 100 let v {year_100} godu!")
