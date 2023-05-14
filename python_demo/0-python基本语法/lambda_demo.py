import math

# # 常规写法
# def circle_area(r):
#     '''
#     计算圆的面积
#     '''
#     result = math.pi * r * r
#     return result
#
#
# r = 10
# print(f"半径为{r}的圆的面积为{circle_area(r)}")
#
# # 用lambda表达式
# result2 = lambda r: math.pi * r * r
# print(f"半径为{r}的圆的面积为{result2(r)}")

# 对获取到的信息进行排序
# 书籍信息
book_info = [
    ("Python 零基础入门", 22.5),
    ("Java 零基础入门", 20),
    ("软件工程 零基础入门", 25),
]

# 指定规则进行排序
# lambda x: (x[1]) 返回了列表中每个元组的第二个元素
book_info.sort(key=lambda x: (x[1]))
print(book_info)
# 输出: [('Java 零基础入门', 20), ('Python 零基础入门', 22.5.错误与异常), ('软件工程 零基础入门', 25)]
