class A:
    def __init__(self, a):
        self.a = A

    def speak(self):
        print(self.a)

class B:
    def __init__(self, b):
        self.b = B

    def speak(self):
        print(self.b)

class Child(A,B):
    def __init__(self, a, b):
        self.a = a
        self.b = b

child = Child("item1", "item2")

child.speak()
