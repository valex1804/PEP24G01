# for i in range(10):
#     user_input = input('give letter: ')
#     print(user_input)

def get_leter_frrom_user():
    for i in range(10):
        user_input = input('give letter/letters: ')
        for letter in user_input:
            yield letter

user_letter = get_leter_frrom_user()

for letter in user_letter:     # varianta de luat in considerare
    print(letter)

# or
# print(next(user_letter))
# print(next(user_letter))
# print(next(user_letter))