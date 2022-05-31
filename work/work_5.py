
#题目：打印出如下图案（菱形）
for i in range(1, 8, 2):
    str = '*' * i
    print(str.center(7))
for i in range(5, 0, -2):
    str = '*' * i
    print(str.center(7))