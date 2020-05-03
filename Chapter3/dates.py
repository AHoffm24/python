#
# Example file for working with date information
#
#imports predefined datetime classes
#similar to #import <iostream> in c++
from datetime import date
from datetime import time
from datetime import datetime

def main():
  ## DATE OBJECTS
  # Get today's date from the simple today() method from the date class
  today = date.today()
  print("todays date is ", today)

  # print out the date's individual components
  print("date components: ", today.day, today.month, today.year)
  
  # retrieve today's weekday (0=Monday, 6=Sunday)
  print("Todays weekday number is: ", today.weekday())
  days = ["mon","tue","wed","thur","fri","sat","sun"]
  print("todays day of the week is ", days[today.weekday()])

  ## DATETIME OBJECTS
  # Get today's date from the datetime class
  print("the time and date is currently ", datetime.now())
  t = datetime.time(datetime.now())
  print("The time currently is ", t)

  # Get the current time


  
if __name__ == "__main__":
  main()
  