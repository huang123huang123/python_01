

# 读取文件：

# 1. 打开文件： open(filename,mode)  # filename 代表的是文件名， mode: 读写模式
f = open('a.txt','r')

# 2. 读取文件： read()           #  按行读取： readline()         # 读取所有的行： readlines()
result = f.read()              #   whlie True:                # for x f.readlines():
print(result)                  #       line = f.readline()    # print(x)
                               #       print(line,end='')
                               #       if not line:
                               #           break
# 3.关闭文件： close()
f.close()