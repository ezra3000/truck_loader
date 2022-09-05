import hash_table
import package
import address
import csv
import truck

address_id_name_dictionary = {}
dependent_dictionary = {}


def count_rows(filename):
    with open(filename) as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        i = 0
        for rows in csv_reader:
            i += 1

        return i


def count_columns(filename):
    with open(filename) as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        i = len(next(csv_reader))
        return i


def create_packages(address_table):
    with open('packages.csv') as pkg_csv:
        package_file = csv.reader(pkg_csv, delimiter=',')
        package_table = hash_table.HashTable(count_rows('packages.csv'))

        for row in package_file:
            d = address_table.get(address_id_name_dictionary[row[1]])
            p = package.Package(int(row[0]), d, row[2], row[3], row[4],
                                row[5], row[6], row[7], None, "Undelivered", [])
            d.packages.append(p.id_num)
            if "Must be delivered with" in p.notes:
                dependencies = the_dependent_note_parser(p.notes)
                dependent_dictionary[p.id_num] = dependencies

            package_table.add(p.id_num, p)

    return package_table


def create_address():
    with open('distance.csv') as dis_csv:
        distance_file = csv.reader(dis_csv, delimiter=',')
        address_counter = 1

        distance_table = hash_table.HashTable(count_rows('distance.csv'))

        for row in distance_file:
            distance_to_next = {}
            j = 1
            address_name = row[0].strip()
            if address_name != "HUB":
                address_name = address_name[:-8]

            while j <= count_rows('distance.csv'):
                distance_to_next[j] = float(row[j])
                j += 1

            d = address.Address(address_counter, address_name, distance_to_next, [])
            address_id_name_dictionary[d.address_name] = d.add_id
            distance_table.add(d.add_id, d)
            address_counter += 1

    return distance_table


def the_dependent_note_parser(notes):
    if len(notes) == 0:
        return None
    dependencies = []
    string = ''
    i = -1
    while (i * -1) <= len(notes):
        c = notes[i]
        if '0' <= c <= '9':
            string = c + string
        elif c == ' ':
            pass
        elif c == ',':
            dependencies.append(int(string))
            string = ''
        else:
            dependencies.append(int(string))
            break
        i -= 1

    return dependencies
