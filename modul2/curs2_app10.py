
txt1 = "Hello Python"
txt2 = "Ana are mere"
txt3 = "Pizza party"
print("Hello " * 4, "Python", sep="_", end=".\n", )
print("Ana " * 4, "are", "mere", sep="_", end=".\n")
print("Pizza " * 4, "party", sep="_", end=".\n")

print("separator _____" * 10)

a = 5.
b = 5
c = "ana"

print(f"""Location for a is: {hex(id(a))}
Location for b is: {hex(id(b))}
Location for c is: {hex(id(c))}""")

print(f"""
Type of a: {type(a)}
Type of b: {type(b)}
Type of c: {type(c)}""")