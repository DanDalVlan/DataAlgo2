class Package:
    def __init__(this_package, package_id, address, city, state, zip_code, deadline, weight, notes, status):
        this_package.package_id = package_id
        this_package.depart_time = None
        this_package.arrival_time = None
        this_package.address = address
        this_package.city = city
        this_package.state = state
        this_package.zip_code = zip_code
        this_package.deadline = deadline
        this_package.weight = weight
        this_package.notes = notes
        this_package.status = status

    def __str__(this_package):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (this_package.package_id, this_package.depart_time,
                                            this_package.arrival_time, this_package.address, this_package.city,
                                            this_package.state, this_package.zip_code, this_package.deadline,
                                            this_package.weight, this_package.notes, this_package.status)

    #def package_status(this_package):