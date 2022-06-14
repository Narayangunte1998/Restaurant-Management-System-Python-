
class Robot:
    def __init__(self,name,color, weight):
        self.name=name
        self.color=color
        self.weight=weight
    def introduce_self(self):
        print(f"My name is {self.name}")

# creating objects
r1=Robot("Tom","Yellow",30)
r2=Robot("Jam","white",40)
# calling function
r1.introduce_self()
r2.introduce_self()
