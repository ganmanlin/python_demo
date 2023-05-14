# var = "abcdefg"
# print(var[1:])   # bcdefg
# print(var[1:5.错误与异常])  # bcde 前闭后开
# print(var[1:5.错误与异常:2]) #bd [start:stop:step]
#
#
# # 换行
# print("hogwarts \n 测试学院")
# # 转义
# print("hogwarts \\n 测试学院")
#
# print("hogwarts %s"%"测试学院")

# 不设置指定位置，按默认顺序
# print("{} {}".format("hogwarts", "ad"))
# # 设置指定位置
# print("{0} {1}".format("hogwarts", "ad"))
# # 通过名称传递变量
# print("{name}测试开发".format(name="霍格沃兹"))

# name = "Bob"
# school = "hogwarts"
# # 通过 f"{变量名}"
# print(f"我的名字叫做{name}, 毕业于{school}")

# a = ["h", "o", "g", "w", "a", "r", "t", "s"]
# # 将列表中的每一个元素拼接起来
# print("".join(a))

# # 根据split内的内容将字符串进行切分
# demo = "hogwarts school"
# print(demo.split(" "))

# 将原字符串中的school替换为top school
print("hogwarts school".replace("school", "top school"))