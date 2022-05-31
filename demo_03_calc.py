

# 赋值运算符

#  a += b   ==> a = a + b
#  a -= b   ==> a = a - b
#  a %= b   ==> a = a % b
a = 3
b = 7
a += b
print(a)

a %= b
print(a)

# 逻辑运算符
# 1. a and b ==> 两个条件都满足，返回真，否则返回假

print(a > 2 and b < 10)
print(a > 2 and b > 10)

# 2. a or b ==> 两个条件满足其一返真，否则为假
print(a > 2 or b > 10)
print(a < 2 or b > 10)

#  not a  ==> 条件为真，加上not变成假，反之变为真
print(not a > 2)
print(not a < 2)