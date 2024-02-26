# class Shop:
#     stoc = {}
#     user_input = None
#
#     def modificare_stoc(self):
#         print('''Meniu :
# 1.Visualizare stoc
# 2.Adaugare produs
# 3.Stergere produs
# 4.Iesire''')
#         self.user_input = input('\n: ')
#         if self.user_input == '2':
#             self.adauga_prod('unt', 5, 100)
#
#     def adauga_prod(self, produs, pret, stoc):
#         self.stoc.update({produs: (pret, stoc)})
#
#
# s = Shop()      # deschidere magazin       s = self  , 's' classa noastra
# s.modificare_stoc()
# print(f'Ai ales : {s.user_input}')
# s.adauga_prod('unt', 5, 100 )
# print(s.user_input)


class Shop:
    stoc = {}
    user_input = None

    def modif_stoc(self):
        print('''   
Meniu:
1. Vizualizare stoc
2. Adaugare produs
3. Stergere produs
4. Iesire''')
        self.user_input = input(f'Alege optiune:\n')
        if self.user_input == '2':
            self.adauga_prod('unt', 5, 100)

    def adauga_prod(self, produs, pret, stoc):
        self.stoc.update({produs: (pret, stoc)})


s = Shop()
s.modif_stoc()
print(f'Ai ales: {s.user_input}')
print(s.stoc)
