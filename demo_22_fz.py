

# 封装： 不希望某部分数据或功能被外界去使用或访问，可以使用_或者__

class Students():
    name = "张三"
    __score = "80"
    def set_score(self,score):
         self.__score = score

    def get_score(self):
        return  self.__score

print(Students.name)
# print(Students.__score)

s1 = Students()
s1.get_score()