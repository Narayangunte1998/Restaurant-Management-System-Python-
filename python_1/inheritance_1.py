# define a class

# main function for default reading
if __name__ == "__main__":
    data = "My data read from the Web"
    print(data)




class class_1:
    school="COEP"
    name = "narayan"
    game = 10
    job_type = 'Python Developer'
    def print_value(self):
        self.name="narayan"
        self.game=10
        self.job_type='Python Developer'

    def testAddition(self,a,b):
        self.a = a
        self.b = b
        return (self.a + self.b)


print("Hi I am Narayan")
# def ____init__(self):  # only can be used in class used for object initialization
#     obj_1 = class_1()  # creating object
#     obj_2 = class_1()  # creating object
#     print(obj_1.school)
#     print(obj_1.testAddition(2, 3))
#     # print("Hi I am Narayan")