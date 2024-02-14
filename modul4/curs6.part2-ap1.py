 # varianta 1 : neterminata

# def check_passwd():
#     requires_chars = ["!", "@", "%"]
#     passwd = input("Introduceti o parola : ")
#     print(passwd)
#     if len(passwd) < 7:
#         print("Parola cu lungime gresita")
#         check_passwd()
#     for character in requires_chars:
#         if character not in passwd:
#             print("Parola trebuie sa contina : ! @ %")
#             check_passwd()
#
# check_passwd()

# varainata 2 : aproape terminata

# def check_passwd():
#     requires_chars = ["!", "@", "%"]
#     passwd = input("Introduceti o parola : ")
#     print(passwd)
#     if len(passwd) < 7:
#         print("Parola cu lungime gresita")
#         check_passwd()
#     else:
#         for character in requires_chars:
#             if character in passwd:
#                 break
#         else:
#             print("Parola trebuie sa contina : ! @ %")
#             check_passwd()
#     for character in range(10):
#        if str(character) in passwd:
#            break
#     else:
#         print("Parola trebuie sa contina : ! @ %")
#
#
# check_passwd()

# Variante a 3 : indeplioneste conditile dar ara si dezavantaje

def check_passwd():
    requires_chars = ["!", "@", "%"]
    passwd = input("Introduceti o parola : ")
    print(passwd)
    condition_not_ok = False
    if len(passwd) < 7:
        print("Parola cu lungime gresita")
        condition_not_ok = True
    else:
        for character in requires_chars:
            if character in passwd:
                break
        else:
            print("Parola trebuie sa contina : ! @ %")
            condition_not_ok = True
    for character in range(10):
        if str(character) in passwd:
            break
    else:
        print("Parola trebuie sa contina : ! @ %")
        condition_not_ok = True
    if condition_not_ok:
        check_passwd()
check_passwd()
