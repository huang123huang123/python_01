

# 字典

# 1.字典的定义： 变量名 = {key1:value1 , key2:value2}
dct1= {}
dct2 = {'a':1,'b':2,'c':3}
print(dct1)
print(dct2)

# 2.字典的获取: dict['键名']  键名不存在会报错
print("获取字典dct2中键名为b的值：",dct2['b'])

# 字典的获取: dict。get(键名) 键名不存在时不会报错，返回None
print("获取字典dct2中键名为b的值：",dct2.get('b'))

# 3.更新字典的某个值： dict['键名'] = 新值
dct2['c'] = 32
print(dct2)

# 4.更新字典里的值到另外一个字典： dict.update(dict1)
dct3 = {'e':22,'f':'hello'}
dct2.update(dct3)
print("更新后的字典显示：",dct2)

# 5.判断字典中是否存在某个键名： '键名' in dict
print('e' in dct2)
print('g' in dct2)

# 6.获取字典中的所有键名 ：dict.keys()
print("获取字典中所有的键名：",dct2.keys())

for x in dct2.keys():
    print(x)

# 7.获取字典中所有的值： dict.values()
print("获取字典中所有的值：",dct2.values())

for x in dct2.values():
    print(x)

# 8.获取字典中所有的键值段： dict.items()
print("获取字典中所有的键值对：",dct2.items())

for x,y in dct2.items():
    print(x,"====",y)

# 9.删除字典内的所有元素： dict.clear()
print(dct3.clear())

# 10.返回一个浅拷贝的字典： dict.copy()
print(dct2.copy())

# 11.返回一个新字典，以序列seq中元素做字典的键，值为字典所有键对应的初始值：dict.fromkeys(seq)
print(dct2.fromkeys('a','f'))

# 12.和get（）类似，但如果键不存在于字典中，将会添加键并将值设为None： dict.setdefault(key,v=None)
print(dct2.setdefault('g'))

# 13.删除字典给定键key所对应的值，返回值为被删除的值，key值必须给出，否则，返回default值： dict.pop(key)
print(dct2.pop('b'))

# 14.随机返回并删除字典中的最后一对键和值： dict.popitem()
print(dct2.popitem())
print(dct2)