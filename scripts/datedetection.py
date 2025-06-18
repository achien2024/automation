import re
import sys

month_dict = {1: 31, 2: 28, '2l': 29, 3: 31, 4: 30, 5: 31, 6: 30, 7:31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
pattern = re.compile(r'(\d?\d)/(\d?\d)/(\d\d\d\d)')
# () group for day, month, year
# ? is optional character

print("Input valid date (DD/MM/YYYY): ")
date = input()

valid_date = pattern.search(date)
n = 0 

while not valid_date and n < 3:
    print("Invalid date. Try again (DD/MM/YYYY)")
    valid_date = pattern.search(input())
    n += 1
    if n == 3:
        print("Too many tries. Goodbye")
        sys.exit()

day = int(valid_date.group(1))
month = int(valid_date.group(2))
year = int(valid_date.group(3))

if month >= 13 or month < 1:
    print(f"invalid date, month: {valid_date.group()}")
    sys.exit()

# check for leap year
if month == 2 and (year % 4 == 0 or year % 400 == 0) and year % 100 != 0:
    # centuries do not count
    if not (day <= month_dict['2l']):
        print(f"invalid date, leap year: {valid_date.group()}")
        sys.exit()
elif not (day <= month_dict[month]):
    print(f"invalid date, incorrect days: {valid_date.group()}")
    sys.exit()

print(f"Valid date: {valid_date.group()}")



