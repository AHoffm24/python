#
# Read and write files using the built-in Python file methods
#

def main():  
  # Open a file for writing and create it if it doesn't exist
  #f = open("textfile.txt", "w+") #opening textfile.txt for write access, + sign means to create file if it doesnt exist. 
  #f variable is the file object you will use to write to. 



  # Open the file for appending text to the end
  #f = open("textfile.txt", "a") #a is for appending text and allows you to add on to an already existing file. 

  # Open the file for reading
  #f = open("textfile.txt, "r"")

  # write some lines of data to the file
  #for i in range(10):
  #  f.write("This is line"+ str(i) + "\r\n") #\r == carriage return
  
  
  
  # close the file when done
  #f.close()
  
  # Open the file back up and read the contents
  f = open("textfile.txt", "r")
  if f.mode == 'r': #do this for error checking that the file exist and was open. If not will give you error. Proper for all Operated Oriented Programming
    contents = f.read()
    print(contents)

  f.close() 
if __name__ == "__main__":
  main()
