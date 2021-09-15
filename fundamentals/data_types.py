name = "asrar farooq bhat"
usn = "1MS18CS032"
age = 22
is_single = True
PI = 3.14159
compex_number = 3+4j

name = input("enter your name: ").strip()
usn = input("enter you usn: ").strip()
age = int(input("enter you age: ").strip())
is_single = input(
    "you are single (True/False): ").strip() == "True"
PI = float(input("enter the value of PI: ").strip())
compex_number = complex(input("enter a complex number: ").strip())

print(name, type(name))
print(usn, type(usn))
print(age, type(age))
print(PI, type(PI))
print(is_single, type(is_single))
print(compex_number, type(compex_number))
