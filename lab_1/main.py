groupmates = [
    {"name": "Иван", "surname": "Иван", "exams": ['Филасофия', 'Высшая математика', 'ВВИТ'], "marks": [4, 4, 4]},
    {"name": "Михаил", "surname": "Михайлович", "exams": ['Филасофия', 'Высшая математика', 'ВВИТ'],
     "marks": [4, 5, 4]},
    {"name": "Доплер", "surname": "Уизли", "exams": ['Филасофия', 'Высшая математика', 'ВВИТ'], "marks": [3, 4, 5]},
    {"name": "Гарри", "surname": "Промов", "exams": ['Филасофия', 'Высшая математика', 'ВВИТ'], "marks": [3, 4, 3]},
    {"name": "Олег", "surname": "Ефремов", "exams": ['Филасофия', 'Высшая математика', 'ВВИТ'], "marks": [5, 5, 5]}]


def print_students(students, filt):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(42), u"Оценки".ljust(20), u"Средний балл".ljust(10))
    for student in students:
        if sr_ball(student["marks"]) > filt:
            print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30),
                  str(student["marks"]).ljust(20), str(round(sr_ball(student["marks"]), 3)).ljust(20))


def sr_ball(marks):
    s = 0
    for mark in marks:
        s += mark
    return float(s/len(marks))


filt = float(input("Введите число для фильтрации: "))
print_students(groupmates, filt)