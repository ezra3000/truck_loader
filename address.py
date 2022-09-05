class Address:
    def __init__(self, add_id, address_name, distance_list, packages):
        self.add_id = add_id
        self.address_name = address_name
        self.distance_list = distance_list
        self.packages = packages


def find_next_closest(distance_list, exclusion_list):
    sorted_list = sorted(distance_list.values())
    sorted_dictionary = {}
    for i in sorted_list:
        for k in distance_list.keys():
            if distance_list[k] == i:
                sorted_dictionary[k] = distance_list[k]

    for q in sorted_dictionary.keys():
        if q not in exclusion_list:
            return q
        else:
            continue
    return -1


def tie_dependencies(dependent_dictionary, package_table):
    for key in dependent_dictionary.keys():
        p = package_table.get(key)
        for values in dependent_dictionary[key]:
            if key not in package_table.get(values).dependent:
                package_table.get(values).dependent.append(key)
            p.dependent.append(values)
    return None
