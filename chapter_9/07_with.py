# f=open("file.txt") # for open the file

# data = f.read()   #to read the file
# print(data)

# f.close() #for close the file


# the same can be written using with statement like this:

with open("file.txt") as f:
    print(f.read() )


