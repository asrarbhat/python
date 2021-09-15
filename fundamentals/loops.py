string = "there is no lord of the rings"
for i in range(len(string)):
    print(string[i], end=" ")
print()
for i in string:
    print(i, end=" ")
print()
for i in range(0, len(string), 2):
    print(string[i], end=" ")
print()


while True:
    print("hey")
    n = input("enter exit: ")
    if n == "exit":
        break


for i in range(10):
    break
else:
    print("you did used break")

for i in range(10):
    pass
else:
    print("you diddn't used break")
