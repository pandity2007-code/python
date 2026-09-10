n=int(input('enter the number :'))

table=[i*n for i in range(1,11)]
with open("file.txt","a") as f:
    f.write(f"table of {n}:{str(table)}\n")