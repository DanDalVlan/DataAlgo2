# Daniel Monahan - Student ID: 010793260
# Data Structures and Algorithms II - Performance Assessment

import csv
import datetime

from Hash_Table import Hash_Table
from Package import Package
from Truck import Truck

with open("WGUPS_Address_File_CSV.csv") as address_file:
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
        notes = str(row[7])
        status = "HUB"

        temp_package = Package(package_id, address, city, state, zip_code, deadline, weight, notes, status)
        package_table.insert(package_id, temp_package)
        print(temp_package)

#    for item in package_table.hash_table:
#       print(str(item))

#    print(package_table.get(22))

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
        for row in address_table:
            if temp_address in row[1]:
                return int(row[0])

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
            for temp_package in temp_truck:
                if next_distance >= get_distance(get_address(truck.location), get_address(temp_package.address)):
                    next_distance = get_distance(get_address(truck.location), get_address(temp_package.address))
                    next_package = temp_package

            truck.packages.append(next_package.package_id)
            temp_truck.remove(next_package)

            truck.location = next_package.address
            truck.mileage = truck.mileage + next_distance
            truck.current_time = truck.current_time + datetime.timedelta(hours=next_distance / truck.speed)
            next_package.depart_time = truck.depart_time
            next_package.arrival_time = truck.current_time

    sort_and_deliver(truck_1)
    sort_and_deliver(truck_2)
    sort_and_deliver(truck_3)



