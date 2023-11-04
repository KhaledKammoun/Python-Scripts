def is_leap_year(year):
    #your code here. Try to do it in one line.
    return ((year%4 == 0 and year%100!=0) or year%400==0)

"""
import calendar
def is_leap_year(year) :
    return calendar.isleap(year)

OR

import calendar
is_leap_year = lambda year: calendar.isleap(year)
    
"""

