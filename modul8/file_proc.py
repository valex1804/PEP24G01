result = open('modul8/example.py', 'rt')
print(result.readlines())
result.flush()   # write to disk
result.close     # no more write operation can be done

with open('modul8/example.py', 'rt') as file:
    output = file.readlines()
print(output)

with open('modul8/test.txt', 'xt') as file:
    file.write("\n # comment ")

with open('modul8/test.txt', 'xt') as file:
        pass

