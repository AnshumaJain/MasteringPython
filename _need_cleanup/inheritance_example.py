
class Parent():
    def __init__(self):
        self.myvar = 1

class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        print(self.myvar)
        self.myvar = 2
        print(self.myvar)

if __name__ == '__main__':
    child = Child()