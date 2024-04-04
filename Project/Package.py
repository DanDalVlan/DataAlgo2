class Package:
    def __init__(this_package, package_id, address, city, state, zip_code, deadline, weight, status):
        this_package.package_id = package_id
        this_package.depart_time = None
        this_package.arrival_time = None
        this_package.address = address
        this_package.city = city
        this_package.state = state
        this_package.zip_code = zip_code
        this_package.deadline = deadline
        this_package.weight = weight
        this_package.status = status

    def package_status(this_package, time_queried):
        this_package.status = "At Hub"
        if this_package.depart_time <= time_queried < this_package.arrival_time:
            this_package.status = "En route"
        elif time_queried >= this_package.arrival_time:
            this_package.status = "Delivered"
