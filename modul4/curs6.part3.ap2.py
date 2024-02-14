# Creați o aplicație care sa ceara input de la utilizator cu un număr. Creați o funcție care
# sa ia ca parametru numărul introdus de către utilizator si sa calculeze puterea acestuia.
# Cereți input de la utilizator în interiorul unei bucle infinite. Dacă utilizatorul dorește sa
# iasa, trebuie sa scrie q.


def putere():
    result = None
    while True:
        user_data_1 = input("Numar1:")
        if user_data_1 in ['Q', 'q']:
            return result
        num1 = int(user_data_1)
        num2 = int(input("Numar2:"))
        result = num1 ** num2
print(putere())
