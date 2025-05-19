

        # 1   -------- Using Self ----------

class Student:

    def __init__(self , name , marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"My name is {self.name} and My score is {self.marks} ")

s1 = Student("Erum Sikander" , 98)
s1.display()