with open("log.txt","r") as f:
    lines=f.readlines()

lineno=1    
for line in lines:
    if "python " in line:
        print(f"yes word is present in this file lineno:{lineno}")
        break
    lineno+=1
else:
    print("no this word is not present in file")
