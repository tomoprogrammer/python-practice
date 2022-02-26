class Human():
    def __init__(self):
        self.name = None
        self.address = None
        
    def show(self):
        print(self.name)
        print(self.address)
        
class Actor(Human): pass

actor = Actor()

actor.name = "大泉"
actor.address = "北海道"

actor.show()