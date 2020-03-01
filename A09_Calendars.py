#
# Example file for working with Calendars
#

# import the calendar module
import calendar

# create a plain text calendar
c = calendar.TextCalendar(calendar.SUNDAY)
# st = c.formatmonth(2017, 1, 0, 0)
# print(st)

# create an HTML formatted calendar
hc = calendar.HTMLCalendar(calendar.SUNDAY)
# st = hc.formatmonth(2017, 1)
# print(st)

# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
for i in c.itermonthdates(2017, 8):
    print(i)

# The 0 are the dates in that month does not belong to August
for i in c.itermonthdays(2017, 8):
    print(i)

for name in calendar.month_name:
    print(name)

# Show as it with the current local machine
for day in calendar.day_name:
    print(day)
  
# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms
print("Team meetings will be on: ")
# remember 13 is not inclusive and not looped

# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:
for m in range(1, 13):
    cal = calendar.monthcalendar(2018, m)
    weekone = cal[0]
    weektwo = cal[1]

    # Use the friday constant to index to the cal array
    # This particular month started on saturday
    # Because date does not belong to this month has value of 0
    if weekone[calendar.FRIDAY] != 0:
        meetday = weekone[calendar.FRIDAY]
    else:
        meetday = weektwo[calendar.FRIDAY]

    print("%10s %2d" % (calendar.month_name[m], meetday))