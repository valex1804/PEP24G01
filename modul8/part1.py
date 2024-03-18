result = 'abc'.__iter__()  # this is an iterable object
print(type(result))

print(id(result))
print(id(result.__iter__()))

print(next(result))  # this is function
print(result.__next__())  # this is method
print(result.__next__())
# print(result.__next__())
print('Iterator is consumed')

result = 'abc'
iterator = result.__iter__()
for i in iterator:
    print(i)


# number = 5
# for i in number:
#     print(i)

# class Number:
#
#     def __init__(self, number):
#         self.number = number
#
#     def __iter__(self):
#         return range(self.number).__iter__()  ### but we want strings
#
# n = Number(5)
#
# for i in n:
#     print(i)


class Number(int):

    def __init__(self, number):
        self.number = number

    def __iter__(self):
        return NumberIterator()


class NumberIterator:
    number_list = []


    def __init__(self, number):
        self.number = number
        self.number.list = []
        for i in range(self.number):
            self.number.list.append(i+1)
        self.number.list.sort(reverse=True)


    def __iter__(self):
        return self


    def __next__(self):
        try:
            self.number_list.pop()
        except IndexError:
            raise StopIteration
        return float(result)


n = Number(5)

for i in n:
    print(i)
