str = "hello world arun"
array = str.split(" ")
print(array)

for i in range(len(array)-1,-1, -1):
    print(array[i],end=" ")