# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

def write_file(file_book, content):
    with open(file_book, 'a') as data:
        data.writelines(f'\n{content}')


def read_file(file_book):
    result = []
    with open(file_book, 'r+') as data:
        data_list = data.read().split('\n')
    for elem in data_list:
        result.append(elem.split(','))
    return result


def show_person(id, persons):
    print(
        f'-- {id+1} --\n Person: {persons[id][0].title()} {persons[id][1].title()} {persons[id][2].title()} \n Number: {persons[id][3]}\n ')


def show_phonebook(persons):
    for i in range(0, len(persons)):
        show_person(i, persons)


def find_number(records_list):
    value = input('Enter name: ').lower()
    for i in range(0, len(records_list)):
        if value in records_list[i]:
            show_person(i, records_list)


def find_person(records_list):
    value = input('Enter number: ')
    for i in range(0, len(records_list)):
        if records_list[i][3] == value:
            show_person(i, records_list)


def add_record(path):
    surname = input('Enter surname: ').lower()
    name = input('Enter name: ').lower()
    fathers_name = input("Enter father's name: ").lower()
    number = input('Enter phone number: ')
    result_data = f'{surname},{name},{fathers_name},{number}'
    write_file(path, result_data)


def delete_record(path):
    persons = read_file(path)
    value = input('Delete by:\n1-"id"\n2-"phone number"\n')
    if value == '1':
        id = int(input("Enter id: "))
        persons.pop(id-1)
    elif value == '2':
        number = input("Enter phone number: ")
        for person in persons:
            if person[3] == number:
                persons.remove(person)
    else:
        print('Unknown command!')
        return
    with open(path, 'w') as data:
        lines = list()
        for person in persons:
            line = ','.join(person)
            lines.append(line)
        data.write('\n'.join(lines))


file_book = 'book.txt'
commands = [(1, 'Show all records'), (2, 'Add record'), (3, 'Search by person'),
            (4, 'Search by phone number'), (5, 'Delete record'), (6, 'Exit')]
records = read_file(file_book)

while (True):
    print('___PhoneBook___\n')
    for item in commands:
        print(f'{item[0]} - {item[1]}')
    print()
    command = input('Enter command: ')
    match command:
        case '1':
            show_phonebook(records)
        case '2':
            add_record(file_book)
            records = read_file(file_book)
        case '3':
            find_number(records)
        case '4':
            find_person(records)
        case '5':
            delete_record(file_book)
            records = read_file(file_book)
        case '6':
            exit(0)
        case _:
            print('--Unknown command!--')
