

# 实例： 创建学生类，要求有属性：姓和年纪；方法有：学习的方法，打印学生的姓名和班级
class Students():

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade          #实例变量
        sex = '男'     #局部变量

    def study(self):
        print("这里的self是：",self)
        socre = 60     #局部变量

    def eat(self):
        print(self.name,"是",self.grade,"正在吃饭")

