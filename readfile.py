file1 = open('input.txt','r')
lines = file1.readlines()

for line in lines:
    print(line.strip())
