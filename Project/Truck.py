class Truck:
    def __init__(this_truck, depart_time, capacity, packages, speed, mileage, location):
        this_truck.depart_time = depart_time
        this_truck.capacity = capacity
        this_truck.packages = packages
        this_truck.speed = speed
        this_truck.mileage = mileage
        this_truck.location = location

    def __str__(this_truck):
