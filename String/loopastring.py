name = "arunkumar"

for letter in name:
    length= len(name)
    print(length)

print(name[::-1])

count = 0

for letter in name:
    count=count+1
print("the string name is {}  length is {} ".format(name,count))

print(f"the string length is {count}")
