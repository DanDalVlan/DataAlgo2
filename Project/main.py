import csv
import datetime

from Hash_Table import Hash_Table
from Package import Package

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

    for item in package_table.hash_table:
        print(str(item))

    print(package_table.get(22))