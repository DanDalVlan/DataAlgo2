# Custom "Package" object that holds all the relevant information for each package
import datetime


class Package:
    def __init__(this_package, package_id, address, city, state, zip_code, deadline, weight, status):
        # Storing original package details as private attributes to reference later if needed
        this_package.package_id = package_id
        this_package._original_address = address
        this_package._original_city = city
        this_package._original_state = state
        this_package._original_zip_code = zip_code
        # Storing everything else as public attributes to be changed if needed
        this_package.depart_time = None
        this_package.arrival_time = None
        this_package.address = address
        this_package.city = city
        this_package.state = state
        this_package.zip_code = zip_code
        this_package.deadline = deadline
        this_package.weight = weight
        this_package.status = status
        this_package.truck = None

    # Function that updates the "status" attribute of a package by checking the "arrival_time" against a user given time
    def package_status(this_package, time_queried):
        this_package.status = "At Hub"
        if this_package.depart_time <= time_queried < this_package.arrival_time:
            this_package.status = "En route"
        elif time_queried >= this_package.arrival_time:
            this_package.status = "Delivered"

    # Function that updates the package info for package #9 if the current time is past 10:20am when the update comes in
    def update_details_based_on_time(this_package, current_time):
        # Update only if it's package #9 and after 10:20 AM
        if this_package.package_id == 9 and current_time >= datetime.timedelta(hours=10, minutes=20):
            this_package.address = '410 S State St'
            this_package.city = 'Salt Lake City'
            this_package.state = 'UT'
            this_package.zip_code = 84111
        else:
            this_package.address = this_package._original_address
            this_package.city = this_package._original_city
            this_package.state = this_package._original_state
            this_package.zip_code = this_package._original_zip_code
