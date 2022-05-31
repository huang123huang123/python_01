

# 字符串演示方法

# 1. 连接字符串
astr = "+"
bstr = astr.join("world")
print(bstr)

# 2. 分割字符串： split(str=""),其中str代表分隔符
cstr = "hello world phython"
dstr = cstr.split("o")
print(dstr)

# 3.查找字符串： find(substr),如果找到了返回的是最小索引。没有找到返回-1
estr = "helloworld"
print(estr.find("l"))
print(estr.find("x"))
print(estr.index("l"))  #==> 没有会报错

# 4.查找以xxx结尾的字符串：endswith('xxx')
fstr = "测试文档.doc"
if fstr.endswith('.doc'):
    print("它是一个world文档")

# 5.替换字符串： replace(old_value,new_value)
gstr = "hello world"
hstr = gstr.replace('world','python')
print(hstr)

# 6.返回字符串长度
gstr = "hello world"
print(len(gstr))

# 7.查找开头字符，是为true，否为false
gstr = "hello world"
x = gstr.startswith('hello')
print(x)

# 8.字符串中只包含数字返回true，否返回false
gstr = "453"
print(gstr.isdigit())

# 9.字符串中全是字母的返回true,否返回false
gstr1 = "hehhhfdbv6"
print(gstr1.isalpha())