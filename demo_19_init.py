

# 实例： 创建学生类，要求有属性：姓和年纪；方法有：学习的方法，打印学生的姓名和班级
class Students():

    name = ""
    grade = ""

# 申明构造方法： __init__()
    def __init__(self):
        print("此方法会被自动执行")


    def study(self):
        print("{}年级的学生{}正在学习".format(self.grade,self.name))

s1 = Students()
s1.name = '张三'
s1.grade = '5'
print(s1.study())

# 以上的需求用构造法实现
class Students1():

    # 申明构造方法： __init__()
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
        print("此方法会被自动执行")

    def study(self):
        print("{}年级的学生{}正在学习".format(self.grade, self.name))
s2 = Students1('王五',6)
s2.study()


# 需求： 实现连接数据库的类，使用构造方法
"""
1. 定义连接数据库的类
2. 必须和数据库建立连接，使用构造方法是最合适的
3. 进行各种的方法调用
"""