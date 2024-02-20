number_participants = int(input('Cati participanti avem la sondaj ? '))
ages = []
for i in range(1, number_participants + 1):
    try:
        age = int(input('Introduceti varsta participantului:'))
    except ValueError:
        age = int(input(f'Nu ati introdus un format valid la participantul {i}. Type again : '))
    ages.append(age)


def avg(lis_of_numbers):
    # total = 0
    # for age in lis_of_numbers:
    total = sum(lis_of_numbers)
    average_age = total / len(lis_of_numbers)
    return average_age


print(avg(ages))
