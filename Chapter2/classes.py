#
# Example file for working with classes
#

#methods are functions in python
#self argument refers to the object itself. Self refers to the particular instance of the object being operated on


#  class Person: #example of how to initalize a class with variables 
#    def __initialize__(self, name, age, sex):
#      self.name = name
#      self.age = age
#      self.sex = sex   

class myClass(): #super class
  def method1(self):
    print("myClass Method1")
  def method2(self, someString):
    print(someString + " myClass Method2 ")


class anotherClass(myClass): #inherited class allows you to call methods from myClass inside of anotherClass
    def method1(self):
      myClass.method1(self)
      print("another class method1")
    def method2(self, someString):
      print("another calss method2")

def main():
  c = myClass()
  c.method1()
  c.method2("this is my string for")
  c2 = anotherClass()
  c2.method1()
  c2.method2("This is a string")

if __name__ == "__main__":
  main()
