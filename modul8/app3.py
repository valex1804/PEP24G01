# class Clasa:
#     an = None
#
#     def __init__(self, list_nume_data):
#         self.dictionar = {}
#         for entity in list_nume_data[:]:
#             if not self.an:
#                 self.an = entity.split('/')[1].split('-')[0]
#                 self.dictionar.update({entity.split('/')[0]: entity.split('/')[1]})
#                 list_nume_data.remove(entity)
#             else:
#                 if self.an == entity.split('/')[1].split('-')[0]:
#                     self.dictionar.update({entity.split('/')[0]: entity.split('/')[1]})
#                     list_nume_data.remove(entity)
#                 else:
#                     pass
#
#     def __str__(self):
#         return str(self.dictionar)
#
#
# with open('elevi.txt') as file:
#     elevi = file.readlines()
#
# while elevi:
#     print(Clasa(elevi))


import datetime
class Class:
    year = None

    def __init__(self, list_name_date):
        self.students_info = {}
        for entity in list_name_date[:]:
            if not self.year:
                self.year = entity.split("/")[1].split("-")[0]
                self.students_info.update({entity.split("/")[0]: entity.split("/")[1].strip()})
                list_name_date.remove(entity)
            else:
                if self.year == entity.split("/")[1].split("-")[0]:
                    self.students_info.update({entity.split("/")[0]: entity.split("/")[1].strip()})
                    list_name_date.remove(entity)
                else:
                    pass

        self.students_info_ = self.students_info.copy()


    def __iter__(self):
        return self

    def __next__(self):
        new_info = dict(map(lambda item: (item[0], datetime.datetime(int(datetime.datetime.now().year),
                                                                     int(item[1].split("-")[1]),
                                                                     int(item[1].split("-")[2]))),
                            self.students_info_.items()))
        today = datetime.datetime.now()
        for new_info_ in new_info.items():
            print(today - new_info_[1])

    def __str__(self):
        return str(self.students_info)


with open("elevi.txt") as f:
    students = f.readlines()

classes = []
while students:
    classes.append(Class(students))

for class_ in classes:
    next(class_)

