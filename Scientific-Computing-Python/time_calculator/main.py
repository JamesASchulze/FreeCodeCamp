# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main


print("-_-_-_-_-_-_-_-_-")
# print(add_time("10:06 AM", "2:02"))
# print(add_time("3:30 PM", "2:12"))
# print(add_time("8:16 PM", "36:02", "tuesday"))
# print(add_time("8:16 PM", "466:02", "tuesday"))
# print(add_time("2:59 AM", "24:00", "saturDay"))
print(add_time("11:59 PM", "24:05"))
print("-_-_-_-_-_-_-_-_-")


# Run unit tests automatically
main(module='test_module', exit=False)