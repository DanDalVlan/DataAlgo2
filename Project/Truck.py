class Truck:
    def __init__(this_truck, truck_id, depart_time, current_time, capacity, packages, speed, mileage, location):
        this_truck.truck_id = truck_id
        this_truck.depart_time = depart_time
        this_truck.current_time = current_time
        this_truck.capacity = capacity
        this_truck.packages = packages
        this_truck.speed = speed
        this_truck.mileage = mileage
        this_truck.location = location

    def __str__(this_truck):
        return "%s, %s, %s, %s, %s, %s, %s, %s" % (this_truck.truck_id, this_truck.depart_time,
                                                   this_truck.current_time, this_truck.capacity, this_truck.packages,
                                                   this_truck.speed, this_truck.mileage, this_truck.location)
