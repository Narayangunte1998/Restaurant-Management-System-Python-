class StudentInfo:
  def __init__(self,Name,ID,Age):
    self.name=Name
    self.id=ID
    self.age=Age
    # return f'name of the studetn is {self.Name}, ID:{self.ID} and Age:{self.Age}'

Krish=StudentInfo("Krishna","RITM0034",75)
print(Krish.id)