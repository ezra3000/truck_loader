version = "version 1.0"
border = "==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-=="
title_line1 = "  _____                _          _                    _           "
title_line2 = " |_   _| __ _   _  ___| | __     | |    ___   __ _  __| | ___ _ __ "
title_line3 = "   | || '__| | | |/ __| |/ /     | |   / _ \ / _` |/ _` |/ _ | '__|"
title_line4 = "   | || |  | |_| | (__|   <      | |__| (_) | (_| | (_| |  __| |   "
title_line5 = "   |_||_|   \__,_|\___|_|\_\     |_____\___/ \__,_|\__,_|\___|_|   "
title_line6 = "                         The Truck Loader                          "
separator = "...................................................................."
Tborder = "~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*"

vertical_menu_border = "_______________________________________________________________________"
menu_separator = "|  ...................................................................  |"
menu1 = "|  Main Menu:                                                           |"
menu3 = "|  1  =  Inspect Trucks                                                 |"
menu4 = "|  2  =  Inspect Packages                                               |"
menu6 = "|  4  =  Quit                                                           |"


def print_menu():
    print("")
    print("*" + vertical_menu_border + "*")
    print(menu1)
    print(menu_separator)
    print(menu3)
    print(menu4)
    print(menu6)
    print("|" + vertical_menu_border + "|")
    print("")


def print_title():
    print(Tborder)
    print(title_line1)
    print(title_line2)
    print(title_line3)
    print(title_line4)
    print(title_line5)
    print(title_line6)
    print(Tborder)
    print(version)
    print(separator)
