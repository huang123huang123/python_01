
""""
# 输入a,b,c,d4个整数，计算a+b-c*d的结果
a = input("请输入一个整数：")
b = input("请输入一个整数：")
c = input("请输入一个整数：")
d = input("请输入一个整数：")
print(int(a)+int(b)-int(c)*int(d))
"""
# 打印1~100内被3整除的所有数的和
sum1 = 0
for x in range(1,101):
    if x % 3 == 0:
        sum1 += x
print(sum1)

sum2 = 0
for x in range(3,101,3):
    sum2 += x
print(sum2)

sum3 = 0
x = 1
while x <= 100:
    if x % 3 ==0:
        sum3 += x
    x += 1
print(sum3)

# 使用range()输出1~10内的所有奇数
for x in range(1,10,2):
    print(x)
