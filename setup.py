from datetime import time, datetime, timedelta
import csv_import
import path_finder
import truck

time_format = "%H:%M %p"

address_table = csv_import.create_address()
package_table = csv_import.create_packages(address_table)
truck_table = truck.get_table()

hub = address_table.get(1)

truck1 = truck_table.get(1)
truck2 = truck_table.get(2)
truck3 = truck_table.get(3)

driver1 = "Cody Sparks"
driver2 = "George Washington"

p1 = package_table.get(1)
p2 = package_table.get(2)
p3 = package_table.get(3)
p4 = package_table.get(4)
p5 = package_table.get(5)
p6 = package_table.get(6)
p7 = package_table.get(7)
p8 = package_table.get(8)
p9 = package_table.get(9)
p10 = package_table.get(10)
p11 = package_table.get(11)
p12 = package_table.get(12)
p13 = package_table.get(13)
p14 = package_table.get(14)
p15 = package_table.get(15)
p16 = package_table.get(16)
p17 = package_table.get(17)
p18 = package_table.get(18)
p19 = package_table.get(19)
p20 = package_table.get(20)
p21 = package_table.get(21)
p22 = package_table.get(22)
p23 = package_table.get(23)
p24 = package_table.get(24)
p25 = package_table.get(25)
p26 = package_table.get(26)
p27 = package_table.get(27)
p28 = package_table.get(28)
p29 = package_table.get(29)
p30 = package_table.get(30)
p31 = package_table.get(31)
p32 = package_table.get(32)
p33 = package_table.get(33)
p34 = package_table.get(34)
p35 = package_table.get(35)
p36 = package_table.get(36)
p37 = package_table.get(37)
p38 = package_table.get(38)
p39 = package_table.get(39)
p40 = package_table.get(40)


def pack_all():
    print("Loading...")
    truck_1_load = [p4, p7, p8, p13, p14, p15, p16, p19, p20, p21, p29, p30, p34, p37, p39, p40]
    truck1.packages = truck_1_load
    truck1.departure_time = datetime.strptime("8:00 am", time_format)

    truck_2_load = [p2, p3, p5, p9, p10, p11, p12, p17, p18, p23, p27, p28, p33, p35, p36, p38]
    truck2.packages = truck_2_load
    truck2.departure_time = datetime.strptime("10:20 am", time_format)

    truck_3_load = [p1, p6, p22, p24, p25, p26, p31, p32]
    truck3.packages = truck_3_load
    truck3.departure_time = datetime.strptime("9:05 am", time_format)
    print("Packages are on Trucks!")


def begin_delivery(current_time):
    truck1_points = (current_time - truck1.departure_time).total_seconds() / 60
    truck2_points = (current_time - truck2.departure_time).total_seconds() / 60
    truck3_points = (current_time - truck3.departure_time).total_seconds() / 60

    if truck1_points >= 0:
        truck1.driver = driver1
        leftover_points1 = path_finder.depart(truck1, truck1_points, address_table, package_table)
        if leftover_points1 > 0:
            truck1.status = "HUB"
            truck1.driver = "None"

        if truck2_points >= 0:
            print("Notice!!! Package Number", p9.id_num,
                  "has been updated with new information and is ready for delivery.")
            p9.address = address_table.get(20)
            truck2.driver = driver1
            leftover_points2 = path_finder.depart(truck2, truck2_points, address_table, package_table)
            if leftover_points2 > 0:
                truck2.status = "HUB"
                truck2.driver = "None"

        if truck3_points >= 0:
            truck3.driver = driver2
            leftover_points3 = path_finder.depart(truck3, truck3_points, address_table, package_table)
            if leftover_points3 > 0:
                truck3.status = "HUB"
                truck3.driver = "None"


def space_to_add(item, number):
    space = " "
    return (number - len(item)) * space


def display_truck_info(barrier):
    combined_miles = truck1.mileage + truck2.mileage + truck3.mileage
    x = "|"
    print('')
    print(barrier)
    print("Truck", x, "   Current Driver   ", x, "   Truck  Mileage   ", x, "Truck Status")

    print("--------------------------------------------------------------------------")

    print(str(truck1.truck_num) + "    ", x, truck1.driver + space_to_add(truck1.driver, 20), x,
          str(truck1.mileage) + space_to_add(str(truck1.mileage), 20), x, truck1.status)
    print(str(truck2.truck_num) + "    ", x, truck2.driver + space_to_add(truck2.driver, 20), x,
          str(truck2.mileage) + space_to_add(str(truck2.mileage), 20), x, truck2.status)
    print(str(truck3.truck_num) + "    ", x, truck3.driver + space_to_add(truck3.driver, 20), x,
          str(truck3.mileage) + space_to_add(str(truck3.mileage), 20), x, truck3.status)
    print("")
    print("Total Combined Mileage =", combined_miles)
    print(barrier)


def display_package_info(barrier):
    x = "|"
    print('')
    print(barrier)
    print("Package", x, "Address ID", x, "Deadline", x, "Package Status", x, "Notes")
    print("--------------------------------------------------------------------------")
    i = 1
    while i <= len(package_table.map):
        pkg = package_table.get(i)
        print(str(pkg.id_num) + space_to_add(str(pkg.id_num), 7), x,
              str(pkg.address.add_id) + space_to_add(str(pkg.address.add_id), 10), x,
              str(pkg.deadline.strftime(time_format)) + space_to_add(str(pkg.deadline.strftime(time_format)), 8), x,
              pkg.status + space_to_add(pkg.status, 14), x,
              pkg.notes)
        i += 1
    print("")
    print(barrier)
