import shutil
import os


with open("old.txt") as f:
    content=f.read()
with open("renamed_python.txt","w") as f:
    f.write(content)
    


os.remove("old.txt") 