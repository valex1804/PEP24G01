# for and range
for i in range(10):
    print(i)

print(i)

# check one of the following chars are in the string

my_str = "adcd1232"
check_chars = ["2", "!"]

for char_ in check_chars:
    if char_ in my_str:
        print(f"success found : {char_}")
        break
else:
    print(f'Could not find ant char in : {check_chars}')
