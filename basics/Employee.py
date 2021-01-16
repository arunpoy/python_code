class Employee:
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay

    def getFullName(self):
        return self.first +" " + self.last




emp1 = Employee("arun","kumar",5000)

print(emp1.getFullName())
