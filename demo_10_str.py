

# 格式化字符： %s
my_str = "my name is %s" %('zhangsan')
print(my_str)

# 格式化整数： %d
my_str = "张三 今年 %d 岁" % (34)
print(my_str)

#格式化浮点数： %f
my_str = "一斤苹果%f元" %(5.273)
print(my_str)

# 辅助指令： m.n
my_str = "一斤苹果%12.2f元" %(5.273)
print(my_str)

# 显示左对齐： -
my_str = "一斤苹果%-12.2f元" %(5.273)
print(my_str)

# 数字前面显示： +
my_str = "一斤苹果%+12.2f元" %(5.273)
print(my_str)

# 前面显示0： 0
my_str = "一斤苹果%012.2f元" %(5.273)
print(my_str)

# 使用format去格式化： "{}".format("字符串")
my_str ="张三 今年{}岁".format(32)
print(my_str)

# format格式化两个参数： "{}  {}".format(参数1,参数2）
my_str ="今天星期{}，张三买了{}斤苹果".format('一','5')
print(my_str)

# format的位置参数： "{0}{1}{2}{3}".format(第一个数，第二个数，第三个数，第四个数）
my_str ="今天星期{0}，张三买了{1}斤苹果".format('一','5')
print(my_str)

# format的关键字参数： "{x}{y}".format(x='hello‘,y='world’）
my_str ="今天星期{x}，张三买了{y}斤苹果".format(x='五',y='2')
print(my_str)

# format的位置参数和关键字结合使用： "{0}{x}".format('hello',x='world'）
my_str ="今天星期{0}，张三买了{x}斤苹果".format('一',x='5')
print(my_str)

