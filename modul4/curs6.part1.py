# def add_(x, y):
#     print(locals())
#     return x + y
#    # print(x)  will never execute

# result = add_(3, 4)
# print(result)
#

# ex sa calculam un numar factorial

# local variable

# def factorial(x):
#     result = 1
#     for i in range(1, x+1):
#         result *= i
#     return result

# global variable

# result = 1
# def factorial(x):
#     global result
#     for i in range(1, x+1):
#         result *= i
#
# factorial(4)
# print(result)


# ex suma lui gaus
# result = 0
# def gauss(n):
#     global result
#     for i in range(1, n+1):
#         result += i
# gauss(100)
# print(result)
#
# print((100 * (100+1))/2)


# result = 0
# def gauss(n):
#     global result
#     for i in range(1, n+1):
#         result += i
# gauss(100)
# print(result)
#
# print((100 * (100+1))/2)


# suma fractilor
# def sumafractii(x):
#     suma = 0
#     for i in range(1, x+1):
#         suma += 1/i
#     return suma
#
# x = int(input())
# print(sumafractii(x))

# def sum():
#     number1 = 20
#     number2 = 30
#     summ = 30 + 20
#     print(summ)
# sum()