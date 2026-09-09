age:int=12 # variable type hint

def greeting(name:str)->str:
    return f"hello,{name}!"
greeting("yash")

print(greeting("hello yash"))