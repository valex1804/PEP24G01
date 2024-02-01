# index of string

hello = "Hello word"
        #0123456789
print(hello[2])         # (this is index)
print(hello[2:4])      # importanta opentru noi ( this is slice) , ultimul element nu se ia in considerare
print(hello[3:7])      # last index not included
print(hello[0:10:2])   # not all version of python 3 ( pas de 2 , asa numara el)
print(hello[0:12:2])   # not all version of python 3
print(hello[::2])      # default value cu numar de pas de 2

hello = "H e l l o  w o r d"
        #        -6-5-4-3-2-1
print(hello[::-1])

hello = "H e l l o  w o r l d"    # cu numere negative
        #-10-9-8-7-6-5-4-3-2-1
print(hello[::-1])   # pas cu -1 , default textul invers afisat
print(hello[-5::1]) # importanta pentru noi
print(hello[-5:-10:-1])
print(hello[-5:-1:1])

# cand avem trei elemente , al treilea element reprinta pasul