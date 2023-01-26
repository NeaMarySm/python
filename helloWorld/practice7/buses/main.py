import functions as fn

commands = [(1, 'Route detail'), (2, 'Add record'), (3, 'Show drivers'),
            (4, 'Show buses'), (5, 'Delete record'), (6, 'Exit')]

data_lists = [(1, 'Drivers', 'drivers.txt'),
              (2, 'Buses', 'buses.txt'), (3, 'Routes', 'routes.txt')]

drivers_file = data_lists[0][2]
buses_file = data_lists[1][2]
routes_file = data_lists[2][2]

drivers = fn.read_file_data(drivers_file)
buses = fn.read_file_data(buses_file)
routes = fn.read_file_data(routes_file)

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
                    fn.add_driver(drivers_file, drivers)
                    drivers = fn.read_file_data(drivers_file)
                case '2':
                    fn.add_bus(buses_file, buses)
                    buses = fn.read_file_data(buses_file)
                case '3':
                    fn.add_route(routes_file, routes)
                    routes = fn.read_file_data(routes_file)
                case _:
                    print('--Unknown command!--')

        case '3':
            fn.show_drivers_list(drivers)
        case '4':
            fn.show_buses_list(buses)
        case '5':
            fn.show_commands(data_lists)
            current_list = input('Enter list number: ')
            match current_list:
                case '1':
                    fn.show_drivers_list(drivers)
                    fn.delete_record(drivers_file, drivers)
                    drivers = fn.read_file_data(drivers_file)
                case '2':
                    fn.show_buses_list(buses)
                    fn.delete_record(buses_file, buses)
                    buses = fn.read_file_data(buses_file)
                case '3':
                    fn.show_route_detail(
                        drivers=drivers, buses=buses, routes=routes)
                    fn.delete_record(routes_file, routes)
                    routes = fn.read_file_data(routes_file)
                case _:
                    print('--Unknown command!--')
        case '6':
            exit(0)
        case _:
            print('--Unknown command!--')
