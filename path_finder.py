def find_next_closest(distance_list, searching):
    sorted_list = sorted(distance_list.values())
    sorted_dictionary = {}
    for i in sorted_list:
        for k in distance_list.keys():
            if distance_list[k] == i:
                sorted_dictionary[k] = distance_list[k]

    for q in sorted_dictionary.keys():
        if q in searching:
            return q
        else:
            continue
    return -1


def depart(truck, points, address_table, package_table):
    destinations = []
    visited = [1]

    for p in truck.packages:
        if p.address.add_id not in destinations:
            destinations.append(p.address.add_id)

    for n in visited:
        distance_list = address_table.get(n).distance_list
        next_stop_id = find_next_closest(distance_list, destinations)
        if next_stop_id != -1:
            next_stop = address_table.get(next_stop_id)
            truck.status = "On route to: " + next_stop.address_name
            miles_traveled = next_stop.distance_list[n]
            points_to_minus = miles_traveled / 0.3
            points -= points_to_minus
            if points >= 0:
                truck.mileage += miles_traveled
                visited.append(next_stop_id)
                destinations.remove(next_stop_id)
                for pkg_num in next_stop.packages:
                    pkg = package_table.get(pkg_num)
                    if pkg in truck.packages:
                        pkg.status = "Delivered"
                        truck.packages.remove(pkg)
        else:
            hub = address_table.get(1)
            truck.status = "Returning to: " + hub.address_name
            miles_traveled = hub.distance_list[n]
            truck.mileage += miles_traveled

            points_to_minus = miles_traveled / 0.3
            points -= points_to_minus
    return points
