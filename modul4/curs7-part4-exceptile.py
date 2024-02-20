# exceptions

# try:
#     result = 1/0
#     print(result)
# except:
#     print('failed')

# try:
#     raise NotImplemented('This is a test')
#     print(result)
#     result = 1/0
#     print(result)
# except ZeroDivisionError:
#     print('failed')
# except NameError:
#     print('Variable result does not exit')


try:
    # raise NotImplemented('This is a test')
    # print(result)
    # result = 1/0
    # print(result)
    pass
except Exception:
    print('some unexpected error occured ')
except ZeroDivisionError:
    print('Cannot divide by 0')
except NameError:
    print('Variable result does not exit')
# except Exception:
    print('some unexpected error occured ')
else:
    print('Everything executed successfully')
finally:
    print('This will always get printed ')