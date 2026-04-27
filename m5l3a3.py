#parent class
class bird:
    def __init__(self):
        print("the bird is ready")
    def whoisThis(self):
        print("bird")
    def swim(self):
        print("swim faster")
#child class
class penguin(bird):
    def __init__(self):
        #call super() function
        super().__init__()
        print("penguin is ready")
    def whoisThis(self):
        print("penguin")
    def run(self):
        print("run faster")
#object creation
peggy = penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()