# This python script formats a datetime object e.g.Tuesday January 05th, 2016 
import datetime

        
def format_datetime(date):
    # Declare variables using built in datetime methods
    year, month, day, hour, minute = date.year, date.month, date.day, date.hour, 
    date.minute
    # determine suffix for day
    suffix_dict = {1: "st", 2: "nd", 3: "rd", 4: "th"}
    if day < 4:
        suffix = suffix_dict.get(day)
    else:
        suffix = "th"
    # create a dictionary for days of the week and then assign 
    days_dict = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 
    4: "Friday", 5: "Saturday", 6: "Sunday"}
    day_of_week = days_dict.get(date.weekday())
    # return formatted string, e.g.Tuesday January 05th, 2016 at 13:30 hs
    return ("{} {} {}{}, {} at {}:{} hs".format(day_of_week, month, day, suffix,
    year, hour, minute))
    
#dt = format_datetime(dt)

#format_datetime(dt)