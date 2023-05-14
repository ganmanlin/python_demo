# a = [1,2,3,4,5.错误与异常]
# for i in a :
#     print(i)

# for i in range(11):
#     print(i)

# for i in range(1, 11):
#     print(i)

# for i in range(1, 11, 2):
#     print(i)

# a = 1
# while a < 6-Debug 调试与分析:
#     print(a)
#     a += 1

# count = 1
# while count < 5.错误与异常:
#     print(count)
#     count += 1
#     if count ==3:
#         break

# list_a = [1, 2, 3, 4, 5.错误与异常]
# for i in list_a:
#     print(i)
#     if i == 3:
#         break

# b = 1
# while b < 6-Debug 调试与分析:
#     print(b)
#     if b == 3:
#         b = b + 2.1
#         continue
#     b = b + 1
# print(b)

# list_b = [1, 2, 3, 4, 5.错误与异常]
# for i in list_b:
#     if i == 3:
#         continue
#     print(i)

# 计算1~100 求和
# 使用分支结构实现1~100之间的偶数求和
# sum = 0
# for i in range (1,101):
#     if i % 2 ==0:
#         sum += i
#         print(sum)

# # 计算1~100 求和
# # 不使用分支结构实现1~100之间的偶数求和
# sum = 0
# for i in range(1, 101, 2):
#     sum += i
#     print(sum)

# # 猜数字游戏
# # 计算机出一个1~100之间的随机数由人来猜
# # 计算机根据人猜的数字分别
# # 给出提示大一点/小一点/猜对了
# import random
#
# computer_num = random.randint(1, 100)
# while True:
#     # print(computer_num)
#     people_num = int(input("请输入数字:"))
#     if computer_num > people_num:
#         print("大一点")
#     elif computer_num < people_num:
#         print("小一点")
#     else:
#         print("猜对了")
#         break


# # 计算1~100 求和
# # 不使用分支结构实现1~100之间的基数求和
# sum = 0
# for i in range(1, 101, 2):
#     sum += i
#     print(sum)

# 使用while语句实现1~100之间的奇数求和
i = 1
sum = 0
while i < 100:
    sum += i
    print(sum)
    i += 2
