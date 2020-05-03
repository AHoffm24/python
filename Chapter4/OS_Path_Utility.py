#
# Example file for working with os.path module
#
import os #allow use of operating system features
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
  # Print the name of the OS
  print("The os name is ", os.name)

  # Check for item existence and type
  print("item textfile.txt exist: " + str(path.exists("textfile.txt")))
  print("item is a file: " + str(path.isfile("textfile.txt")))
  print("item is a dir: " + str(path.isdir("textfile.txt")))
  # Work with file paths
  print("item path: " + str(path.realpath("textfile.txt")))
  print("iteam path and name: " + str(path.split(path.realpath("textfile.txt"))))
  # Get the modification time
  t = time.ctime(path.getmtime("textfile.txt")) #get modification time
  print(t)
  print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))) #another way to print modfication time and date
  # Calculate how long ago the item was modified
  td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
  print("it had been " + str(td) + " since the file was last modified")
  print("or " + str(td.total_seconds()) + " seconds")
  
if __name__ == "__main__":
  main()
