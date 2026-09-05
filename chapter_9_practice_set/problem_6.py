with open("log.txt","r") as f:
    content=f.read()
if("python " in content):
    print("yes word is present in this file")
else:
    print("no this word is not present in file")
