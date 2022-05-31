

# 将一个列表的数据复制到另一个列表中
alst = [1,6,3]
blst = ['s',4,'v']
blst.extend(alst)
print(blst)

#输出 9*9 乘法口诀表
for x in range(1,10):
    for y in range(1,x+1):
        print(x,' * ',y, '=' ,x*y,end='  ')
    print()

# 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数
astr = "djihs7370m@&^%4dn"
zm = 0
kg = 0
sz = 0
other = 0
for x in astr:
   if x.isalpha():
       zm += 1
   elif x.isdigit():
        sz += 1
   elif x.isspace():
        kg += 1
   else:
        other += 1
print('字母：',zm)
print('空格:',kg)
print('数字：',sz)
print('其他：',other)
