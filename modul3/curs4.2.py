number = int(input("Give number:"))

print(range(0, number, 2))
print(type(range(number)))

for number in range(0, number + 1, 2):
    print(number)

print(f"last value : {number}")  # can be undefined



