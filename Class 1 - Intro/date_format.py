# This python script formats a datetime object e.g.Tuesday January 05th, 2016 
# at 13:30 hs
from datetime import datetime

        
def format_datetime(dt):
    # Declare variables using built in datetime methods
    (year, month, day, hour, minute) = (dt.year, dt.month, dt.day, dt.hour, 
    dt.minute)
    # determine suffix for day
    suffix_dict = {1: "st", 2: "nd", 3: "rd", 4: "th"}
    if day < 4:
        suffix = suffix_dict.get(day)
    else:
        suffix = "th"
    zero = ""
    if day < 10:
        zero = "0"
    # create dictionarys for months and days of the week and then assigns
    month_dict = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May",
    6: "June", 7: "July", 8: "August", 9: "September", 10: "December",
    11: "November", 12: "December"}
    days_dict = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 
    4: "Friday", 5: "Saturday", 6: "Sunday"}
    day_of_week = days_dict.get(dt.weekday())
    full_month = month_dict.get(month)
    # return formatted string, e.g.Tuesday January 05th, 2016 at 13:30 hs
    return ("{} {} {}{}{}, {} at {}:{} hs".format(day_of_week, full_month, zero,
    day, suffix, year, hour, minute))
    
dt = datetime(2016, 1, 5, 13, 30)
print(format_datetime(dt))