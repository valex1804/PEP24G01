# 1
# my_list = ["Masa", 5, "Scaun", 4.5, [5, 6, 7], 8]
# for obj in my_list:
#     print(f"Tipul obiectului {obj} Masa este {type(obj)}")

    # challnage
my_list = ["Masa", 5, "Scaun", 4.5, [5, 6, 7], 8, ['a']]
for obj in my_list:
    print(f"Tipul obiectului {obj} Masa este {type(obj)}")
    if type(obj) == list:
        print(obj)
        for inner_obj in obj:
            print(f"tipul obiectului {inner_obj} esre {type(inner_obj)}")


