class Employee:
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole
    @classmethod
    def from_dash(cls, string):
        # params = string.split("-")
        # print(params)
        # return cls(params[0], params[1], params[2])
        return cls(*string.split("-"))  # will split all value and pass to class which will create all
        # varibles for karan (will execute def __init__(self, aname, asalary, arole):)

karan = Employee.from_dash("Karan-480-Student")
print(karan.role)

str_1="Karan-480"
def fun_1(str_2):
    list_1=[]
    list_1=print(*str_2.split('-'))
    print(list_1)
fun_1(str_1)