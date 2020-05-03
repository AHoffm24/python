#
# Example file for working with Calendars
#


# import the calendar module
import calendar 

# create a plain text calendar
c = calendar.TextCalendar(calendar.MONDAY)
string = c.formatmonth(1992, 2, 0, 0)
print(string)
# create an HTML formatted calendar
hc = calendar.HTMLCalendar(calendar.SUNDAY)
string = hc.formatmonth(1992,2)
print(string)

# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
for i in c.itermonthdays(1992,2):
    print(i)
  
# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms
for name in calendar.month_name:
    print(name)



for day in calendar.day_name:
    print(day)  

# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:
print("Team meetings will be on: ")
for m in range(1,13): #13 will not be included because it stops when m reaches 13
    cal = calendar.monthcalendar(2020, m) #Returns a matrix representing a month’s calendar. 
                                          #Each row represents a week; days outside of the month a represented by zeros. 
                                          #Each week begins with Monday unless set by setfirstweekday().
    weekone = cal[0] #friday has to be in one of the first 2 weeks because the month could have started on a saturday
    weektwo = cal[1] 
    #say weekone began on saturday its list would look like [0,0,0,0,0,1,1]
    #by calling Calendar.FRIDAY it checks the 5th place in the list to see if its a 1 or zero
    if weekone[calendar.FRIDAY] != 0:
        meetday = weekone[calendar.FRIDAY]
    else:
        meetday = weektwo[calendar.FRIDAY]

    print("%10s %2d" % (calendar.month_name[m], meetday))