

# 函数： 位置参数，参数个数和顺序要一一对应，不能颠倒

def add(x,y):
    return x + y

print(add(3,4))
print(add('hello','world'))  #: helloworld
# print(add(2,4,6)) 报错
# print()

# 关键字参数： 调用时使用key:value形式进行调用
def student_lesson(grade,subjest):
    z = "{}年纪上{}课".format(grade,subjest)
    return  z
print(student_lesson(grade=2,subjest='语文'))
print(student_lesson(subjest='语文',grade=2))

# 用处： 实现一个函数，参数特别多，调用时不需要记住位置
#connect(host='localhost',username='root',password,database,pory,commit)

# 默认参数： 其中某个参数会有默认值，带有默认值的参数放在最后面
def study_language(name,language='python'):
    info = ("{}要学习{}语言".format(name,language))
    return  info
print(study_language('张三','java'))
print(study_language('李四','python'))
print(study_language('王五'))

# 需求： 可以输入任何个数进行相加

# 可变化参数： 参数的个数可以运行变化的，有两种形式，分别是列表形式和字典形式
# 1.定义列表形式
def add(x,y,*args):
    print(args)
    z = x+y + sum(args)
    return  z
print(add(3,6))
print(add(3,6,7))
print(add(3,6,8,3,6))