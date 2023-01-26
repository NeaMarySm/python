def read_file_data(path):
    result = []
    with open(path, 'r', encoding='utf8') as datafile:
        for line in datafile:
            result.append(line.strip('\n').split(','))
    return result


def save_data_to_file(path, data_list):
    with open(path, 'w', encoding='utf8') as datafile:
        for rawdata in data_list:
            datafile.write(','.join(rawdata)+'\n')


def show_commands(commands):
    for item in commands:
        print(f'{item[0]} - {item[1]}')


def show_route_detail(routes, drivers, buses):
    temp_list = []
    for i in range(0, len(routes)):
        temp_list.append(routes[i].copy())
        for driver in drivers:
            if routes[i][3] == driver[0]:
                temp_list[i][3] = driver[1]
        for bus in buses:
            if routes[i][2] == bus[0]:
                temp_list[i][2] = bus[1]
        show_route(temp_list[i])


def show_driver(record):
    print(
        f'id: {record[0]} | Driver: {record[1].title()} {record[2].title()} | Year of birth: {record[3]} \n ')


def show_route(record):
    print(
        f'id: {record[0]} | Number: {record[1]} | Driver: {record[3].title()} | Bus: {record[2].upper()}\n ')


def show_bus(record):
    print(
        f'id: {record[0]} | Registration number: {record[1].upper()}\n ')


def show_drivers_list(drivers):
    for el in drivers:
        show_driver(el)


def show_buses_list(buses):
    for el in buses:
        show_bus(el)


def add_driver(path, drivers):
    id = input('Enter id: ').lower()
    surname = input('Enter surname: ').lower()
    name = input('Enter name: ').lower()
    birth = input('Enter year of birth: ')
    result_record = [id, surname, name, birth]
    drivers.append(result_record)
    save_data_to_file(path, drivers)


def add_bus(path, buses):
    id = input('Enter id: ').lower()
    number = input('Enter registration number: ').lower()
    result_record = [id, number]
    buses.append(result_record)
    save_data_to_file(path, buses)


def add_route(path, routes):
    id = input('Enter id: ').lower()
    number = input('Enter number: ').lower()
    bus_id = input('Enter bus id: ').lower()
    driver_id = input('Enter driver id: ').lower()
    result_record = [id, number, bus_id, driver_id]
    routes.append(result_record)
    save_data_to_file(path, routes)


def delete_record(path, records_list):
    id = input('Enter id of the record: ')
    for record in records_list:
        if record[0] == id:
            records_list.remove(record)
    save_data_to_file(path, records_list)
