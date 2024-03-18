class Masina:
    def __init__(self, marca: str, usi: int, culoare: str, an:
    int, pret: float):
        self.marca = marca
        self.usi = usi
        self.culoare = culoare
        self.an = an
        self.__pret = pret
    def getPret(self):
        return self.__pret

    def __str__(self):
        return f'Marca: {self.marca}, Culoare: {self.culoare}'

    def __repr__(self):
        return f'Marca: {self.marca}, Culoare: {self.culoare}'
    def getSum(self, other):
        return other + self.__pret

masina1 = Masina("Audi", 4, "gri", 2006, 3400)
masina2 = Masina("BMW", 2, "maro", 2007, 4788.60)
masina3 = Masina("Volvo", 4, "gri", 2017, 27000)
masina4 = Masina("Audi", 4, "negru", 2013, 10200)
masina5 = Masina("Audi", 2, "gri", 2005, 3400)
masina6 = Masina("BMW", 4, "negru", 2017, 22000)
masina7 = Masina("Volvo", 4, "gri", 2017, 27000)

masini = [masina7, masina6, masina5, masina4, masina3, masina1, masina2]

total = 0

for masina in masini:
    total += masina.getPret()
medie = total / len(masini)
print(medie)

print(list(filter(lambda masina: True if 'BMW' == masina.marca else False, masini)))

audi = list(filter(lambda masina: True if masina.marca == "Audi" else False, masini))

total = 0
for masina in audi:
    total += masina.an
medie = total / len(audi)
print(medie)
