#
# Example file for working with functions
#

# define a basic function
def func1():
    print("This is Function 1")

# function that takes arguments
def func2(arg1, arg2):
  print (arg1, " ", arg2)

# function that returns a value
def cube(x):
    return x*x*x

# function with default value for an argument
def power(num, x=2):
    result = 1
    for i in range(x):   #_ is the default character for an unused variable being used instead of i
        result = result * num
    return result
#function with variable number of arguments
def multi_add(*args):
    result = 0
    for x in args:
       result = result + x
    return result
     



func1()
print(func1()) #Python sees the return value of calling func1 as non because func1 returns nothing, but by calling it it still prints, but the print occurs before the return value of none
print(func1)  #this prints the memory location of the function 1
func2(10,20) 
print(func2(10,20))
print(cube(3)) #prints value returned by function cube which would be 3*3*3 = 27
print(power(2))
print(power(2,3))
print(power(x=3, num=2)) #in python you can directly reference the variables in the function in any order you would like an assign values to them. 
print(multi_add(1,2,3,4))