import design
import package
import path_finder
import setup
import design
from datetime import time, datetime

design.print_title()
time_format = "%H:%M %p"
open_time = datetime.strptime("8:00 am", time_format)
open_datetime = datetime.time(open_time)
print("Good morning! Business begins at:", open_time.__format__(time_format))
start = input("Press Enter to load the packages:")
setup.pack_all()

time_str = input("Enter the current time (use format --:-- am/pm): ").strip()
i = -1
while i < 0:
    i = package.time_string_check(time_str)
    if i < 0:
        time_str = input("Enter the current time (use format --:-- am/pm): ").strip()
current_time = package.time_str_converter(time_str)

if current_time < open_time:
    print("The business is not open yet! Please check back at a later time.")
else:
    setup.begin_delivery(current_time, open_time)

