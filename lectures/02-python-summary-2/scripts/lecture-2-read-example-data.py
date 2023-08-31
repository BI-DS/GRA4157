import os

filepath = os.path.join("..", "data", "example_data.txt")

infile = open(filepath)

infile.readline()
infile.readline()
infile.readline()

c1  = []
c2 = []
c3 = []
for line in infile:
    info = line.split()
    c1.append(float(info[0]))
    c2.append(float(info[1]))
    c3.append(float(info[2]))
    
print(c1,c2,c3)
