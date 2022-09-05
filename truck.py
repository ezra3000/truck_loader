import hash_table


def get_table():
    truck_table = hash_table.HashTable(3)
    truck_table.add(1, Truck(1, "None", [], 0))
    truck_table.add(2, Truck(2, "None", [], 0))
    truck_table.add(3, Truck(3, "None", [], 0))

    return truck_table


class Truck:
    def __init__(self, truck_num, driver, packages, mileage):
        self.truck_num = truck_num
        self.driver = driver
        self.packages = packages
        self.mileage = mileage
        self.status = "HUB"

    def set_driver(self, driver_name):
        self.driver = driver_name

    def load(self, package):
        package.status = "Out for delivery"
        package.on_truck = self
        self.packages.append(package)

    def front_load(self, package):
        package.status = "Out for delivery"
        package.on_truck = self
        self.packages + package
