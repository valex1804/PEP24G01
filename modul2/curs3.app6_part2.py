# stringuri formatate

# method format

my_str = "text {}"
print(my_str.format('''example'''))
my_str = "text {1} {0}"
print(my_str.format('example1', 'example2'))
my_str = "text {ex1} {ex2}"
print(my_str.format(ex1='example1', ex2='example2'))
my_str = "text {}"
print(my_str.format(2))

print(80 * "#")

# formatted string
ex1 = 'example1'
ex2 = 'example2'
print(f"text2 {ex1}")
print(f"text2 {ex1} {ex2} {ex1}")

print(10 * "*")

# len function

ex1 = "example 1"
print(len(ex1))


some_text = input("Introduceti un sir :")
print("Lungimea sirului este : {} ".format(len(some_text)))
