class SampleClass:

    def __init__(self, a):
        ## private varibale or property in Python
        self.__a = a

    ## getter method to get the properties using an object
    def get_a(self):
        print("getter called")
        return self.__a

    ## setter method to change the value 'a' using an object

    def set_a(self, a):
        print("setter called")
        self.__a = a

s1 = SampleClass(10)
