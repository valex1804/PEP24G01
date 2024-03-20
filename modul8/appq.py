# class Employer:
#     angajat = []
#     salari = []
#
#     def add_employer(self, employer_add):
#         self.employer_add = employer_add
#
#     def __init__(self, add_salary):
#         self.add_salary = add_salary
#


salarii_input = input("Introduceti salariile separate cu virgula: ")
# salarii = [int(s) for s in salarii_input.split(",")]    # genereaza o lista , cu 'list comprehension' , pt var 1

# procent_maj = float(input("Introduceti procentul de marire: "))  # use for var 1, 2 , 3
procent_maj = input("Introduceti procentul de marire: ") # var 4

# salarii_marite = list(map(lambda x: x * (1 + procent_maj / 100), salarii)) # var1

# print("Salariile marite sunt:")   # var1
# for salariu in salarii_marite:
#     print(salariu)


# print("Salariile marite sunt:")
# for salariu in map(lambda x: x * (1 + procent_maj / 100), salarii):   # var 2
#     print(salariu)

# print("Salariile marite sunt:")
# for salariu in map(lambda x: int(x) * (1 + procent_maj / 100), salarii):   # var 3
#     print(salariu)

# print("Salariile marite sunt:")
# for salariu in map(lambda x: int(x) * (1 + float(procent_maj) / 100), salarii_input.split(",")):   # var 4
#     print(salariu)

print("Salariile marite sunt:")
print('\n'.join(map(lambda x: str(int(x) * (1 + float(procent_maj) / 100)), salarii_input.split(","))))  # var 5



# Version 6 with generators

salarii_input = input("Introduceti salariile separate cu virgula: ")
procent_maj = input("Introduceti procentul de marire: ")
print("Salariile marite sunt :")

def marire():
    for sal in salarii_input.split(","):
        yield str(int(sal) * (1 + float(procent_maj) / 100))

print('\n'.join(marire()))