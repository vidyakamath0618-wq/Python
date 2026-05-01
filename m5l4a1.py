#class creation
class myclass:
    #private variable
    __privateVar = 27
#private mathod
def __privMeth(self):
    print("i'm inside class myClass")
    #function to print value of private variable
def hello(self):
    print("private variable value:",self.__privateVar)
    self.__privMeth()
foo = myclass()
foo.hello()