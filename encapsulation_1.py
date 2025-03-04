class A:
     _a=10 # Protected
     __b=30 # Private
     def Show(self):
          print("a=",self._a)
          print("b=",self.__b)
obj=A()
obj.Show()
print("Outside of class ",A._a)
# print("Outside of class ",A.__b)


# Public Members - Public members are accessible from anywhere, both inside and outside the class. These are the default members in Python.

class Public:
     def __init__(self):
          self.name = "Jone" # Public attribute
          
     def display_name(self):
          print("self.name") # Public method

obj = Public()
obj.display_name() # Accessible
print(obj.name) # Accessible


# Protected members - Protected members are identified with a single underscore (_). They are meant to be accessed only within the class or its subclasses.

class Protected:
     def __init__(self):
          self._age = 30 # Protected attribute

class Subclass(Protected):
     def display_age(self):
          print(self._age) # Accessible in subclass

obj = Subclass()
obj.display_age()


# Private members - Private members are identified with a double underscore (__) and cannot be accessed directly from outside the class. Python uses name mangling to make private members inaccessible by renaming them internally.
class Private:
    def __init__(self):
        self.__salary = 50000  # Private attribute

    def salary(self):
        return self.__salary  # Access through public method

obj = Private()
print(obj.salary())  # Works
#print(obj.__salary)  # Raises AttributeError
