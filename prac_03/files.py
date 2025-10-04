# 1.
name = input("Enter your name: ")
file = open("name.tet", "r")
file.write(name)
file.close()

# 2.
file = open("name.tet", "r")
name = file.read()
file.close()
print(f"Hi {name}")

# 3.
with open("number", "r") as file:
    number1 = int(file.readline())
    number2 = int(file.readline())
    total = number1 + number2
print(total)

# 4.
total = 0
with open("number", "r") as file:
    for line in file:
        total += int(line)
print(total)

