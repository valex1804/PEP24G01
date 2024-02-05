# if + condition

var1 = int(input("Add number :"))

if var1 == 1:
    print(var1)
else:
    print("number is not one")

# true-ish
print(bool(""), 'empty string')
print(bool("0"), '0 string')
print(bool(0), '0 int')
print(bool(-1000), '-1000 int')
print(bool(None), 'None object')

var2 = int(input("Add a  : "))

if 1 + var2:
    print(var2)
else:
    print('number is not x')


#-------

var3 = int(input("Add a number : "))

if 1 + var3:
    print(f"result firts {var3}")
elif 2 + var3:
    print(f"Result second :{2 + var3}")
else:    # not reached
    print('number is not x')

# ex 2

var4 = int(input("Add a number : "))

if var4 > 0:
    print(f"result positive {var4}")
elif var4 < 0:
    print(f"Result negative :{var4}")
else:    # not reached
    print('number is not o')

# and
var5 = int(input("Add a number : "))

if var5 > 10:
    print(f"result positive {var5}")
elif var5 < -10:
    print(f"Result negative :{var5}")
elif var5 <= 10 and var5 > 0:
    print("result is in interval (0-10)")
elif var5 >= 10 and var5 > 0:
    print("result is in interval [-10-0]")  # unde - ( rep.interval)
else:  # not reached
    print('number is not o')