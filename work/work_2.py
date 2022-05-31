

# 打印1~100所有偶数的和 减去 所有奇数的和的值
sum1 = 0
sum2 = 0
for x in range(1,101):
    if x % 2 ==0:
        sum1 += x
    else:
        sum2 += x
print(sum1-sum2)

# 求1+2+3+...+100的和
sum = 0
for x in range(1,101):
    sum += x
print(sum)

# 判断一个数n能同时被3和5整除
n = input("请输入一个数：")
if int(n) % 3 == 0 and int(n) % 5 == 0:
    print("能被3和5整除")
else:
    print("不能被3和5整除")