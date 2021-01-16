from datetime import date
class person:
    count = 0
    country = 'India'
    def __init__(self,name,age):
        self.name=name
        self.age=age
        person.count +=1

    @classmethod
    def fromBirthYear(cls,name,year):
        return cls(name,date.today().year - year)

    @staticmethod
    def isAdult(age):
        return age > 18

    def getCount():
        return person.count


p1 = person("arun",30)
p2 = person.fromBirthYear("kumar",1981)

print(p1.age)
print(p1.count)
print(p2.age)
print(p1.country)

print(person.isAdult(22))
print(person.getCount())

#print(help(person))
