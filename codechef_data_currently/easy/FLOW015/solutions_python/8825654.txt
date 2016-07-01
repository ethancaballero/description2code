import sys

days = ['saturday','sunday','monday','tuesday','wednesday','thursday','friday']

def is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def get_days_count_in_year(year):
    if is_leap_year(year):
        return 366
    else:
        return 365

def get_jan1_day(year):
    current_year = 2001
    day_index = days.index('monday')

    while current_year > year:
        current_year = current_year - 1
        day_index = day_index - get_days_count_in_year(current_year)
    while current_year < year:
        day_index = day_index + get_days_count_in_year(current_year)
        current_year = current_year + 1
    return days[day_index % len(days)]

if __name__=="__main__":
    lines = sys.stdin.readlines()
    n = int(lines[0])

    for i in range(n):
        year = int(lines[1+i])
        print get_jan1_day(year)
