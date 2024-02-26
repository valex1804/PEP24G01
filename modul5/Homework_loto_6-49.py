import random

input_utilizator = input('Introduceti 6 numere separate prin virgula [1-49] : ')
numere_alese_str = input_utilizator.split(',')
numere_alese_lista = []

# convertim numere in stringuri si verificam daca sunt valide :
for numere_str in numere_alese_str:
    numar = int(numere_str)
    if 1 <= numar <= 49:
        numere_alese_lista.append(numar)
if len(numere_alese_lista) != 6:
    print('Nu ati introdus 6 numere valide')
    exit()

print(numere_alese_lista)

# Generam 6 numere la intamplare
random_extragere_num = random.sample(range(1, 50), 6)       # where k means : count

# comparam listele pentru a vedea cate numere se porivesc

# numere_ghicite = len(numere_alese_lista) == len(random_extragere_num)

numere_ghicite = 0
numere_alese_unice = []

# Iteram prin numerele alese si le adaugam intr-o lista unica daca nu au fost deja adaugate
for n in numere_alese_lista:
    if n not in numere_alese_unice:
        numere_alese_unice.append(n)

# Acuma iteram prin lista unica si numaram cate sunt prezente in list de numere extrase
for n in numere_alese_unice:
    if n in random_extragere_num:
        numere_ghicite += 1

# Afisare rezultate jucator
print(f'Numere alese sunt : {numere_alese_lista}')
print(f'Numere extrase sunt : {random_extragere_num}')
print(f'Ati ghicit atatea numere : {numere_ghicite}')

# Determinam castigul pe baza numarului de numere ghicite

if numere_ghicite == 3:
    print('Castig : 50 de lei')
elif numere_ghicite == 4 or numere_ghicite == 5:
    print('Castig : 500 lei')
elif numere_ghicite == 6:
    print('Felicitari ! Ai castigat 1500 lei')
else:
    print('Mai incearca , nu ai castigat nimic')
