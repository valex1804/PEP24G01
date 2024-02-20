# dictionary

my_dict = {'one': 1, 'two': 2, 'true': True}
print(my_dict)
print(type(my_dict))

my_dict = dict(one=1, two=2)
print(my_dict)
print(type(my_dict))


# iterate dictionary

for element in my_dict:  # same as my_dict.keys()
    print('dict key :', element)

for element in my_dict.values():
    print('dict key :', element)

for element in my_dict.items():
    print('dict key :', element)

for key, value in my_dict.items():
    print('dict key :', key, value)

print("----------------------")
# get key / value
value = my_dict['one']
print('returned value is :', value)
value = my_dict['one'] = '''one'''
print('returned value is :', value)
print("----------------------")
# problema de rezolvat cu dictionary : un cos de cumparaturi

cart = {'apple': 10, 'plums': 15, 'bananas': 5}   # cantitate
#
# shop_k = {'apple': 1.2, 'plums': 4, 'bananas': 5.5}   # price
# shop_p = {'apple': 1.3, 'plums': 3, 'bananas': 8}        # price
# shop_l = {'apple': 1.4, 'plums': 2, 'bananas': 10}         # price
#
# shop = {'pro': shop_p, 'lil': shop_l, 'kau': shop_k}


# Tuple

a, b = (1, 2)  # se poate scrie si fara paranteze , same as 1, 2 ; Un tuple cu un singur element a = 1,
print(a)
print(b)

a, b = b, a
print(a)
print(b)