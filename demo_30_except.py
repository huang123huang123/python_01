

# 错误和异常

# def div(x,y):
#     z = x/y
#     return z

# print(div(3,4))
# print(div(3,0))
# print(div(6,6))     # 不被运行

# 使用try ...except语句
"""
语法格式：
try:
    正常代码块
except Exception as e:
    处理异常代码块
"""

# def div1(x,y):
#     try:
#         z = x / y
#         return z
#     except Exception as e:
#         print("除法不能出现被0除的情况")
#
# print(div1(3,4))
# print(div1(3,0))
# print(div1(6,6))

# finally

try:
    f = open('a.txt','r')
    linea = f.readlines()
    print(2/0)
    for x in linea:
        print(x)
    f.close()
except Exception as e:
    print(e)

finally:
    print("是否运行该代码区域")
    f.close()