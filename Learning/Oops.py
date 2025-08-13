# classes are user defined blueprint or prototype
# sum, multiplication, addition, constant operation required in a calculator
# methods, class variables, instance variable, connstructor all are the different terminalogies here when you say classes
# Basically functions used in class are called as a method there is no such difference in functions and methods
# if you use function without wrapping in classes and use them independently then these are treated as functions
# but when you bring this complete methodologies inside the class then we called them as method.

class Calculator:
    num = 100

    def getData(self):
        print("I am now executing as method in class")

# obj = Calculator() # syntax to create objects in python
# obj.getData()
# print(obj.num)


#self keyword is mandatory for calling variable names into method (Self is a nothing but object and passes as first argument and attaching with variables)
#instance and class variables have whole different purpose
#instance variables differs for each and every object but where as class variables are constant no matters how many object you created
#constructor name should be __init__
#new keyword is not required when you create object

class Calculator:
    num = 100  #class variables

    #default constructor
    # __init__ is a keyword to declare the constructor in python
    #Parametarize constructor
    def __init__(self, a, b): #when you sending parameters you have to make sure that those parameter are catched here in your constructor if not then it will through an error
        self.firstNumber = a #Instance variable
        self.secondNumber = b #Storing the value in instance variables
        print("I am called automatically when object is created")

    def getData(self):
        print("I am now executing as method in class")

    def Summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num
                                                      #class variable and class is calculator

# obj = Calculator(2, 3)
# obj.getData()
# print(obj.Summation())
#
# obj1 = Calculator(4, 5) # Instance variable value changes here
# obj1.getData()
# print(obj1.Summation())