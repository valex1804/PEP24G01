# generator

r = range(11)
print(type(r))

result_generator = (_ for _ in range(3))
print(type(result_generator))

print(next(result_generator))
print(next(result_generator))
print(next(result_generator))
# print(next(result_generator))

result_generator = (_ for _ in range(10000000000))

def my_generator():
    for _ in range(3):
        yield _

print(type(my_generator()))



generator = my_generator()
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

# generator.__next__()