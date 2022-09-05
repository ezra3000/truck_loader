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
    truck_1_load = [p1, p4, p13, p14, p15, p16, p19, p20, p21, p34, p39, p40]
    truck1.packages = truck_1_load
    truck1.departure_time = datetime.strptime("8:00 am", time_format)

    truck_2_load = [p3, p5, p6, p7, p8, p18, p25, p26, p29, p30, p31, p32, p36, p37, p38]
    truck2.packages = truck_2_load
    truck2.departure_time = datetime.strptime("9:05 am", time_format)

    truck_3_load = [p2, p9, p10, p11, p12, p17, p22, p23, p24, p27, p28, p33, p35]
    truck3.packages = truck_3_load
    truck2.departure_time = datetime.strptime("10:20 am", time_format)
    print("Packages on Truck!")


def begin_delivery(current_time, open_time):
    leftover_points = 0
    points = (current_time - open_time).total_seconds() / 60
    print("STARTING POINTS = ", points)
    if points >= 0:
        leftover_points = path_finder.depart(truck1, points, address_table, package_table)

    minutes_passed = truck1.departure_time + timedelta(minutes=(truck1.mileage / 0.3))
    print(minutes_passed.strftime(time_format))



