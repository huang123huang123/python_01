

# for循环
"""
for 循环变量 in 序列
代码块
"""

# 需求： 循环字符串abcdef中的每个字符
for x in 'abcdef':
    print(x)

# whlie 循环
"""
while 条件语句（condition）
代码块（staements)
"""
# 需求： 打印1-5的数
a = 1
while a <= 5:
    print(a)
    a += 1 # a = a + 1

# 需求：计算1-100内所有的和
sum = 0
a = 1
while a <= 100:
    sum += a  #  ==> sum = sum + a
    a += 1    #  ==> a = a + 1
print(sum)

