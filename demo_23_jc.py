

# 类的继承

"""
1. 必须具有父子关系，有父类和子类
"""
class people():

    age = 0

    def eat(self,people_type):
        print(people_type,"在吃饭")

class Students(people):
    pass

class Teacher(people):

    pass

s = Students()
s.eat("学生")
Students.age = '20'
print(Students.age)

t = Teacher()
t.eat("老师")
Teacher.age ='40'
print(Teacher.age)
