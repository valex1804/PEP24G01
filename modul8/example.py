# map all object to letter "a"

all_objects = input('provide letters: ')


#              function return
print(''.join(map(lambda letter: 'a', all_objects)))


# map odd object to letter "a" and even objects to letter "b"


all_objects = input('provide letters: ')
print(''.join(map(lambda letter: 'a' if letter[0] % 2 else 'b', enumerate(all_objects))))  # this show index


# map odd object to index of iterated object

'abcd'
'0123'

all_objects = input('provide letters: ')
# print('\n'.join(map(lambda letter: str(letter[0]), enumerate(all_objects))))
print(''.join(map(lambda letter: str(letter[0]), enumerate(all_objects))))



