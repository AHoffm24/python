# 
# Example file for variables
#

# Declare a variable and initialize it
f= "my variable"
print(f)

# # re-declaring the variable works
f = "my new variable"
print(f)
# # ERROR: variables of different types cannot be combined
print("This is a string" + str(123))

# Global vs. local variables in functions
def somefunction():
        f = "def"
        print(f)
somefunction()
print(f)
