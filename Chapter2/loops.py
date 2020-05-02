#
# Example file for working with loops
#

def main():
  x = 0

  # define a while loop
  while(x<5):
    print(x)
    x = x+1

  print("\n")
 
  # define a for loop - x is the itterator; range function goes from 5 to 10
  for x in range(5,10):
    print(x)

  print("\n")
  # use a for loop over a collection
  days = ["mon","tue","wed","thur","fri","sat","sun"]
  for d in days: #is able to tell days is a list and automatically iterates through each position in the list
    print(d)

  print("\n")
  # use the break and continue statements
  #should only print 5 6 7 8 for break statement
  for x in range(5,10):
    if(x == 9): 
      break
    print(x)
  print("\n")
  #prints only odd numbers 
  for x in range(5,10):
    if(x%2 == 0 ): 
      continue
    print(x)

  print("\n")
  #using the enumerate() function to get index 
  days = ["mon","tue","wed","thur","fri","sat","sun"]
  for i,d in enumerate(days): #returns the value inside of the list to d, as well as the position to i
    print(i, d)
    

if __name__ == "__main__":
  main()
