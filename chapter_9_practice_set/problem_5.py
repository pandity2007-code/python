words=["boy","aman","tinku"]
with open("file2.txt","r") as f:
    content = f.read()
for word in words:
    content = content.replace(word, "#" * len(words))

with open("file2.txt","w") as f:
    f.write(content)

