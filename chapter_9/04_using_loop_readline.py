f = open("line.txt")

line1 = f.readline()

print(line1)
line2 = f.readline()

print(line2)
line3 = f.readline()

print(line3)

f.close()


line = f.readline()

while(line!= ""):
    print(line)
    line=f.readline()

f.close()