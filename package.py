from datetime import time, datetime


def time_string_check(time_string):
    try:
        time_str_converter(time_string)
        return 2
    except ValueError:
        return -1


def time_str_converter(time_string):
    if time_string == 'EOD':
        t = datetime.strptime("23:59 pm", "%H:%M %p")
        return t
    else:
        deadline = datetime.strptime(time_string, '%I:%M %p')
    return deadline


class Package:
    def __init__(self, id_num, address, city, state, zip_code, deadline, weight, notes, on_truck, status, dependent):
        self.id_num = id_num
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = time_str_converter(deadline)
        self.weight = weight
        self.notes = notes
        self.on_truck = on_truck
        self.status = status
        self.dependent = dependent

    All_Packages = []
