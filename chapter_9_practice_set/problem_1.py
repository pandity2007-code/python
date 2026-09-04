
f=open("poem.txt")
word=f.read()

if ("twinkle"in word):
    print("yes twinkle present in file")
else:
    print("the given word is not in list")   

f.close    