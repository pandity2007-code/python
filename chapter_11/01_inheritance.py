class employe:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"my name is {self.name}")


class programmer(employe):
    def __init__(self, name, language="python"):
        super().__init__(name)
        self.language = language

    def show(self):
        super().show()
        print(f"language is {self.language}")

    def language_skill(self):
        print(f"language is {self.language}")


a = employe("yash")
b = programmer("yash", "python")
print(a.name, b.language)
b.show()
