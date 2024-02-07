# varianta 1 with : for

# passwd = 7788
#
# for incercare in range(100000000):
#     user_input = int(input("Introduceti parola : "))
#     if passwd == user_input:
#         print('Acces permis')
#         break
#     else:
#         print("Parola gresita")



# varianta 2 with " while "

passwd = 7788

while True:
    parola_introdusa = int(input("Introduceti parola : "))
    if passwd == parola_introdusa:
        print('Acces permis')
        break
    else:
        print("Parola gresita")



