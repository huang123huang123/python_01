

# 需求： 可以输入任何个数进行相加

# 可变化参数： 参数的个数可以运行变化的，有两种形式，分别是列表形式和字典形式
# 1.定义列表形式
def add(x,y,*args):
    print(args)
    z = x+y + sum(args)
    return  z
print(add(3,6))
print(add(3,6,7))
print(add(3,6,8,3,6))   #传递多个参数

# 使用列表的方式进行调用
print(add(3,4,*[5,6,7,8]))  # 传递列表

# 2.可变化参数-字典形式的参数
def show_info(**kwargs):
    print(kwargs)

dt_date = {'x':1,'y':2,'z':3}
print(show_info(a='hello',b='world',c=123))
print(show_info(a='hello',b='world'))
print(show_info(**dt_date))

def show_info1(*args,**kwargs):
    print(args,kwargs)