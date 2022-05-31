

# 类的多肽

"""
1. 必须是继承关系
2. 子类中的方法覆盖了父类的方法

继承和多肽的区别：
如果说子类调用的直接是父类的方法：  继承
如果说子类的方法直接覆盖了父类的方法：   多肽
"""
class people():

    def eat(self,people_type):
        print(people_type,"在吃饭")

class Students(people):
    def eat(self,grade):
        super().eat(grade)         # 把父类中的已有功能继承掉了
        print((grade,"年级学生正在吃饭"))    #下面是对该功能的扩展

class Teacher(people):

    def eat(self,subject,time):
        print("{}的老师在{}时间吃饭".format(subject,time))

s = Students()
s.eat("2年级")

t = Teacher()
t.eat("语文学科",'12:00')