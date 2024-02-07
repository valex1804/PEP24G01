# lists

result = "5,10".split(",")
print(type(result))
print(result)

my_str = "hello"
print(id(my_str))
print(id(my_str.capitalize()))

my_list = []
print(id(my_list), 'in memory')
my_list.append(1)
print(my_list, "after append")
print(id(my_list), 'in memory')
my_list.pop()
print(my_list, "after pop")
print(id(my_list), 'in memory')

print(10 * "#")

# id keyword
my_var1 = "test 1"
print(id(my_var1))
my_var1 = "test 1"
print(id(my_var1))

my_var1 = "test 1"
print(id(my_var1))
my_var2 = "test 1"
print(id(my_var1 is my_var2))

print("---------------------------")

my_var3 = f"test 1 {10-9}".capitalize()
print(id(my_var1))
my_var4 = "Test 1 1"
print((my_var3 is my_var4))
print((my_var3 == my_var4))

print("-" * 20)

# for with list

# new_list = [1, "5", True, None, [1,2,3]]
# for obj in new_list:
#   print(obj)
#   new_list.pop(2)

new_list = [1, "5", True, None, [1, 2, 3]]
print(id(new_list) == id(new_list[::]))
print(new_list == new_list[::])
print(new_list, new_list[::])



