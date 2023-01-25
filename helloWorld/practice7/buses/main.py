import functions as fn

commands = [(1, 'Route detail'), (2, 'Add record'), (3, 'Show drivers'),
            (4, 'Show buses'), (5, 'Modify record'), (6, 'Exit')]

data_lists = [(1, 'Drivers', 'drivers.txt'),
              (2, 'Buses', 'buses.txt'), (3, 'Routes', 'routes.txt')]

drivers = fn.read_file_data(data_lists[0][2])
buses = fn.read_file_data(data_lists[1][2])
routes = fn.read_file_data(data_lists[2][2])


while (True):
    print('___Bus Station Dashboard___\n')
    fn.show_commands(commands)
    print()
    command = input('Enter command: ')
    match command:
        case '1':
            fn.show_route_detail(drivers=drivers, buses=buses, routes=routes)
        case '2':
            fn.show_commands(data_lists)
            current_list = input('Enter list number: ')
            match current_list:
                case '1':
                    fn.add_driver(data_lists[0][2], drivers)
                    drivers = fn.read_file_data(data_lists[0][2])
                case '2':
                    fn.add_bus(data_lists[1][2], buses)
                    buses = fn.read_file_data(data_lists[1][2])
                case '3':
                    fn.add_route(data_lists[2][2], routes)
                    routes = fn.read_file_data(data_lists[2][2])
                case _:
                    print('--Unknown command!--')

        case '3':
            fn.show_drivers_list(drivers)
        case '4':
            fn.show_buses_list(buses)
        case '5':
            pass
        case '6':
            exit(0)
        case _:
            print('--Unknown command!--')
