class FirstExample(object):
    def __init__(self):
        self.s = ''

    def getString(self):
        self.s = input("Give me some strings.....")

    def printString(self):
        print(self.s.upper())


x = FirstExample()
print(x)
x.getString()
x.printString()
