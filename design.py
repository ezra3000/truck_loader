version = "version 1.0"
border = "==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-=="
title_line1 = "  _____                _          _                    _           "
title_line2 = " |_   _| __ _   _  ___| | __     | |    ___   __ _  __| | ___ _ __ "
title_line3 = "   | || '__| | | |/ __| |/ /     | |   / _ \ / _` |/ _` |/ _ | '__|"
title_line4 = "   | || |  | |_| | (__|   <      | |__| (_) | (_| | (_| |  __| |   "
title_line5 = "   |_||_|   \__,_|\___|_|\_\     |_____\___/ \__,_|\__,_|\___|_|   "
title_line6 = "                         The Truck Loader                          "
separator = "...................................................................."

delayed_warning_message_border = "~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*"
delayed_warning_message1 = "Warning!!! Tt appears that some packages have been delayed."
delayed_warning_message2 = "When they've arrived at the HUB, pack the remaining packages."


vertical_menu_border = "_______________________________________________________________________"
menu_separator = "|  ...................................................................  |"
menu1 = "|  Main Menu:                                                           |"
menu3 = "|  1  =  Inspect Trucks                                                 |"
menu4 = "|  2  =  Inspect Packages                                               |"
menu5 = "|  3  =  Pack the remaining packages                                    |"
menu6 = "|  4  =  Quit                                                           |"

p_menu1 = "|  Package Menu:                                                        |"
p_menu3 = "|  1  =  Look-up a specific package                                     |"
p_menu4 = "|  2  =  Look-up a list of all packages                                 |"
p_menu5 = "|  3  =  Update a package's information                                 |"
p_menu6 = "|  4  =  Return to main menu                                            |"

t_menu1 = "|  Truck Menu:                                                          |"
t_menu5 = "|  1  =  End of day total miles covered                                 |"
t_menu6 = "|  4  =  Return to main menu                                            |"


def print_warning():
    print("")
    print(delayed_warning_message_border)
    print(delayed_warning_message1)
    print(delayed_warning_message2)
    print(delayed_warning_message_border)
    print("")


def print_t_menu():
    print("")
    print("*" + vertical_menu_border + "*")
    print(t_menu1)
    print(menu_separator)
    print(t_menu5)
    print(t_menu6)
    print("|" + vertical_menu_border + "|")
    print("")


def print_p_menu():
    print("")
    print("*" + vertical_menu_border + "*")
    print(p_menu1)
    print(menu_separator)
    print(p_menu3)
    print(p_menu4)
    print(p_menu5)
    print(p_menu6)
    print("|" + vertical_menu_border + "|")
    print("")


def print_menu():
    print("")
    print("*" + vertical_menu_border + "*")
    print(menu1)
    print(menu_separator)
    print(menu3)
    print(menu4)
    print(menu5)
    print(menu6)
    print("|" + vertical_menu_border + "|")
    print("")


def print_title():
    print(border)
    print(title_line1)
    print(title_line2)
    print(title_line3)
    print(title_line4)
    print(title_line5)
    print(title_line6)
    print(border)
    print(version)
    print(separator)
