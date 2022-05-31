

# range函数
"""
range(start,end,step)
start: 开始索引，默认是从0开始，可以忽略
end: 代表结束，必选项
step: 步长，默认就是1
"""
# 需求1： 打印1-10的数

# for 循环列表 in 序列
for x in range(0,10,1):
    print(x)
print('======')

# 需求2： 开始位置为1，循环到10
for x in range(1,10,1):
    print(x)
print('=====')
# 需求3: 开始位置是1，循环到10，步长为2
for x in range(1,10,2):
    print(x)

# break 语句断开循环
# 需求： 循环1-10，当遇到7退出循环
for x in range(1,11,1):
    print(x)
    if x == 7:
        break
print('======')

# continue 跳过该循环
# 需求： 循环1-10，当遇到7跳过该次循环
for x in range(1,11,1):
    if x == 7:
        continue
        print(x)