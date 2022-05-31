

# 列表

# 格式:变量名 = []
alst = []
blst = [11,23,'hds',None]

#print(alst)
#print(blst)

# 循环列表
#for x in blst:
 #   print("列表中的值：",x)

# 列表的方法
clst = ['red','green','blue']

# 向列表中添加元素： list.append(obj),列表的元素
clst.append('black')
print("使用append添加元素后的列表:",clst)

# 向列表中追加一个其他列表内的元素： list.extend(seq)
clst.extend(blst)
print("追加blst的结果：",clst)

# 列表反转： list.reverse()
clst.reverse()
print("反转后的结果：",clst)

# 列表排序： list.sort(),里面的元素必须是同类型的
#clst.sort()
#print("排序后的结果:"clst)

# 统计在列表中中出现的次数： list.count(obj)
print(clst.count('blue'))

# 从列表中找出某个元素的位置： list.index(obj)
print(clst.index('black'))

# 向列表中的某个位置插入元素：list.insert(index,obj)
clst.insert(1,'hello')
print(clst)

# 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值： list.pop([index=-1])
print("返回的值：",clst.pop(3))

# 移除列表中某个值的第一个匹配项： list.remove(obj)
print(clst.remove('blue'))

# 复制列表： list.copy()
print(blst.copy())

# 清空列表中的所有元素： list.clear
print(blst.clear())
