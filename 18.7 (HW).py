import random

students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
students.sort()
classes = ['Математика', 'Русский язык', 'Информатика']
students_marks = {}
for student in students:
    students_marks[student] = {}
    for class_ in classes:
        marks = [random.randint(1, 5) for i in range(3)]
        students_marks[student][class_] = marks
for student in students:
    print(f'''{student}
            {students_marks[student]}''')

print('''
        Список команд:
        1. Добавить оценки ученика по предмету
        2. Вывести средний балл по всем предметам по каждому ученику
        3. Вывести все оценки по всем ученикам
        4. Удалить оценку ученика по предмету
        5. Удалить ученика
        6. Удалить предмет у ученика
        7. Добавить предмет ученику
        8. Вывести все оценки для ученика
        9. Вывести средний балл по всем предметам по определенному ученику
        10. Выход из программы
        ''')

while True:
    command = int(input('Введите команду: '))
    if command == 1:
        print('1. Добавить оценку ученика по предмету')
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        mark = int(input('Введите оценку: '))
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 2:
        print('2. Вывести средний балл по всем предметам по каждому ученику')
        for student in students:
            print(student)
            for class_ in classes:
                marks_sum = sum(students_marks[student][class_])
                marks_count = len(students_marks[student][class_])
                print(f'{class_} - {marks_sum // marks_count}')
            print()
    elif command == 3:
        print('3. Вывести все оценки по всем ученикам')
        for student in students:
            print(student)
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()
    elif command == 4:
        print('4. Удалить оценку ученика по предмету')
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        mark = int(input('Введите оценку: '))
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            students_marks[student][class_].pop(mark)
            print(f'Для {student} по предмету {class_} удалена оценка {mark}')
    elif command == 5:
        print('5. Удалить ученика')
        student = input('Введите имя ученика: ')
        if student in students_marks.keys():
            del students_marks[student]
            print(f'{student} удален из дневника')
        else:
            print('Данного ученика нет в базе')
            print('Добавить нового ученика?')
            y = 'Да'
            n = 'Нет'
            answer = input('Введите ответ: ')
            if y in answer:
                newbie = input("Введите имя нового ученика: ")
                students.append(newbie)
                for student in students:
                    students_marks[student] = {}
                    for class_ in classes:
                        marks = [random.randint(1, 5) for i in range(3)]
                        students_marks[student][class_] = marks
                print(f'Новый ученик добавлен в базу')
            else:
                print('Выход из редактирования')
    elif command == 6:
        print("6. Удалить предмет у ученика")
        student = input("Введите имя ученика: ")
        class_ = input("Введите название предмета: ")
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            students_marks[student].pop(class_)
            print(f'Для ученика {student} удален предмет {class_}')
        else:
            print('ОШИБКА: неверное имя ученика или назване предмета')
    elif command == 7:
        print('7. Добавить предмет ученику')
        student = input('Введите имя ученика: ')
        new_class = input('Введите новый предмет: ')
        classes.append(new_class)
        if student in students_marks.keys():
            students_marks[student].setdefault(new_class, [])
            print(f'Для ученика {student} добавлен предмет {new_class}')
        else:
            print('Данного ученика нет в базе')
    elif command == 8:
        print('8. Вывести все оценки для ученика')
        student = input('Введите имя студента: ')
        if student in students_marks.keys():
            for classes,marks in students_marks[student].items():
                print(classes + ":", *marks)
        else:
            print('Данного ученика нет в базе')
    elif command == 9:
        print('9. Вывести средний балл по всем предметам по определенному ученику')
        student = input('Введите имя ученика: ')
        if student in students_marks.keys():
            for classes,marks in students_marks[student].items():
                marks_sum = sum(marks)
                marks_count = len(marks)
                print(f'{classes} - {marks_sum//marks_count}')
        else:
            print(f'Данного ученика нет в базе')
    elif command == 10:
        print('10. Выход из программы')
        break