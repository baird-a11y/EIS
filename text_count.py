class Bird:
    
    def __init__(self, flying: bool):
        self.flying = True
    
    
    def fly(self) -> bool:
        if self.flying==True:
            return("Flying high!")
        else:
            print("Cannot Fly")

class Penguin(Bird):
    def __init__(self,flying: bool):
        super().__init__(flying)
    
    def fly(self):
        return("Penguins can't fly!")

elster = Bird(True)
elster.fly()

kaiser = Penguin(False)
kaiser.fly()