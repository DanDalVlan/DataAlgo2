# Daniel Monahan - Student ID: 010793260
# Data Structures and Algorithms II - Performance Assessment

import csv
import datetime

from Hash_Table import Hash_Table
from Package import Package
from Truck import Truck

header = ["ID", "Dept Time", "Arr Time", "Due By", "Status", "Weight", "Zip", "State", "City", "Address"]
column_widths = [5, 15, 15, 15, 15, 10, 10, 10, 20, 30]
header_row = "".join(word.ljust(column_widths[index]) for index, word in enumerate(header))

with open("WGUPS_Address_File_CSV.csv", encoding='utf-8-sig') as address_file:
    address_csvs = csv.reader(address_file)
    address_table = {}
    for row in address_csvs:
        address_table.__setitem__(row[0], row[1])

with open("WGUPS_Distance_File_CSV.csv") as distance_file:
    distance_csvs = csv.reader(distance_file)
    distance_table = []
    for row in distance_csvs:
        distance_table.append(row)

with open("WGUPS_Package_File_CSV.csv") as package_file:
    package_csvs = csv.reader(package_file)
    package_table = Hash_Table()
    for row in package_csvs:
        package_id = int(row[0])
        address = str(row[1])
        city = str(row[2])
        state = str(row[3])
        zip_code = int(row[4])
        deadline = str(row[5])
        weight = str(row[6])
        status = "At HUB"

        open_package = Package(package_id, address, city, state, zip_code, deadline, weight, status)
        package_table.insert(package_id, open_package)

    truck_1 = Truck("truck_1", datetime.timedelta(hours=8, minutes=0), datetime.timedelta(hours=8, minutes=0),
                    16, [5, 7, 8, 13, 14, 15, 16, 19, 20, 21, 29, 30, 34, 37, 39], 18,
                    0.0, "4001 South 700 East")

    truck_2 = Truck("truck_2", datetime.timedelta(hours=9, minutes=5), datetime.timedelta(hours=9, minutes=5),
                    16, [1, 3, 4, 6, 12, 17, 18, 24, 25, 26, 28, 31, 32, 36, 38, 40], 18,
                    0.0, "4001 South 700 East")

    truck_3 = Truck("truck_3", datetime.timedelta(hours=10, minutes=20),
                    datetime.timedelta(hours=10, minutes=20), 16, [2, 9, 10, 11, 22, 23, 27, 33, 35],
                    18, 0.0, "4001 South 700 East")

    def get_address(temp_address):
        return int(list(address_table.keys())[list(address_table.values()).index(str(temp_address))])

    def get_distance(address_1, address_2):
        distance = distance_table[address_1][address_2]
        if distance == '':
            distance = distance_table[address_2][address_1]
        return float(distance)

    def sort_and_deliver(truck):
        temp_truck = []
        for package_id in truck.packages:
            temp_package = package_table.get(package_id)
            temp_truck.append(temp_package)

        truck.packages.clear()

        while len(temp_truck) > 0:
            next_package = None
            next_distance = 100
            for t_package in temp_truck:
                if next_distance >= get_distance(get_address(truck.location), get_address(t_package.address)):
                    next_distance = get_distance(get_address(truck.location), get_address(t_package.address))
                    next_package = t_package

            truck.packages.append(next_package.package_id)
            temp_truck.remove(next_package)

            truck.location = next_package.address
            truck.mileage = truck.mileage + next_distance
            truck.current_time = truck.current_time + datetime.timedelta(hours=next_distance / truck.speed)
            next_package.depart_time = truck.depart_time
            next_package.arrival_time = truck.current_time

    def print_package(input_package, input_time):
        output_package = package_table.get(input_package)
        output_package.package_status(input_time)
        package_info = [
            output_package.package_id,
            output_package.depart_time,
            output_package.arrival_time if output_package.arrival_time else "",
            output_package.deadline,
            output_package.status,
            output_package.weight,
            output_package.zip_code,
            output_package.state,
            output_package.city,
            output_package.address,
        ]
        package_row = "".join(str(field).ljust(column_widths[index]) for index, field in enumerate(package_info))
        print(package_row)

    def get_valid_input(prompt, min_value, max_value):
        while True:
            user_input = input(prompt)
            try:
                user_input = int(user_input)
                if min_value <= user_input <= max_value:
                    return user_input
                else:
                    print(f"Please enter a number between {min_value} and {max_value}")
            except ValueError:
                print("Please enter an integer")

    class Main:
        sort_and_deliver(truck_1)
        t1_final_package = package_table.get(truck_1.packages[-1])
        t1_final_address = get_address(t1_final_package.address)
        t1_return_distance = get_distance(t1_final_address, get_address("4001 South 700 East"))
        truck_1.mileage = truck_1.mileage + t1_return_distance

        sort_and_deliver(truck_2)
        sort_and_deliver(truck_3)

        total_mileage = truck_1.mileage + truck_2.mileage + truck_3.mileage

        print("\nHello and welcome to the WGUPS Delivery System Main Menu")
        print("Total mileage today was: " + str(total_mileage) + " miles\n")

        print("What time would you like data from?")
        input_hours = get_valid_input("Hours (24 hour format): ", 0, 23)
        input_minutes = get_valid_input("Minutes (60 minute format): ", 0, 59)
        input_time = datetime.timedelta(hours=input_hours, minutes=input_minutes)

        input_selection = 0
        while True:
            input_selection = get_valid_input(
                "Please select an option:\n1. View a package\n2. View all\n3. Choose a new time\n9. Exit\n",
                1, 9)

            if input_selection == 1:
                input_package = get_valid_input("Which package number?: ", 1, 40)
                print(header_row)
                print_package(input_package, input_time)

            elif input_selection == 2:
                print(header_row)
                for package_id in range(1, 41):
                    print_package(package_id, input_time)

            elif input_selection == 3:
                print("What time would you like data from?")
                input_hours = get_valid_input("Hours (24 hour format): ", 0, 23)
                input_minutes = get_valid_input("Minutes (60 minute format): ", 0, 59)
                input_time = datetime.timedelta(hours=input_hours, minutes=input_minutes)

            elif input_selection == 9:
                break

            else:
                print("Invalid selection")



