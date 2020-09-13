x = 500
print(id(x))
y=x
print(id(y))

print(y is x)
print(y == x)

a = [3,4,5]
b = a
print(b is a)
a[2]= 67
print(b)

m = [3,4,5]
n = [3,4,5]
print(m is n)  #Identity comparison

print (m == n) #value comparison
m.append(45)
print(m)
