# Эта программа получает от пользователя данные о сотрудниках
# и сохраняет их в виде записей в файле employees.txt.

def main():
    # Получить количество записей о сотрудниках для создания.
    num_emps = int(input('Сколько записей о сотрудниках ' +
                         'Вы хотите создать? '))

    # Открыть файл для записи.
    emp_file = open('employees.txt', 'w')

    # Получить данные каждого сотрудника
    # и записать их в файл.
    for count in range(1, num_emps + 1):
        # Получить данные о сотруднике.
        print('Введите данные о сотруднике № ', count, sep='')
        name = input('Имя: ')
        id_num = input('Идентификационный номер: ')
        dept = input('Отдел: ')

        # Записать в файл данные как запись.
        emp_file.write(name + '\n')
        emp_file.write(id_num + '\n')
        emp_file.write(dept + '\n')

    # Показать пустую строку.
    print()

    # Закрыть файл.
    emp_file.close()
    print('Записи о сотрудниках сохранены в employees. txt. ')
    read_file = open('employees.txt', 'r')
    print(read_file.read())
    read_file.close()
# Вызвать главную функцию.
main()
