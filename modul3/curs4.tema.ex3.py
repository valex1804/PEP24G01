cappuccino = 4
espresso = 3.5
print("Cappuccino .... 4 lei [1]")
print("Espresso   .... 3.5 lei [2]")

user_input = input("Ce optiune alegeti [1,2] :")
user_bacnota = int(input("Introduceti o bacnota [5,10] : "))

if user_input == "1":
    rest = user_bacnota - cappuccino
    print("Ati ales optiunea 1")
    print(f'Restul dumneavoasta va fi : {rest} lei')
    print("Produsul se livreaza ....")
elif user_input == "2":
    rest = float(user_bacnota) - espresso
    print("Ati ales optiunea 2")
    print(f"Restul dumneavoastra va fi : {rest} lei")
    print("Produsul se livreaza.....")
else:
    print("Erroare : Optiune nevalida sau Bacnota nevalida")

