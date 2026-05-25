import re

number = input("Enter mobile number: ")

match = re.fullmatch("[6-9]\\d{9}", number)
if match != None:
    print(number, "valid")
else:
    print(number, "invalid")