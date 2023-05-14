# """创建集合"""
# # 1、使用大括号{}填充元素
# set1 = {1, 2, 3}
# set2 = {'a', 'b', 'c'}
# print(set1)
# print(set2)
#
# # 2、使用构造方法创建集合
# set3 = set()  # 空集合
# print(set3,type(set3))
# set4 = set('hello world')
# print(set4,type(set4))
# set5 = set([1, 2, 3])
# print(set5,type(set5))
#
# # 3、使用集合推导式
# set6 = {x for x in range(5.错误与异常) if x % 2 == 0}
# print(set6, type(set6))
#
# # 注意：不要单独使用{ }来创建空集合
# st7 = {}  # 这是字典类型
# print(type(st7))

# """集合使用：成员检测"""
# set8 = {1, 2, 3, 4, 5.错误与异常}
# # in
# print(2 in set8)
#
# # not in
# print(99 not in set8)


# """集合方法 add()"""
# # 添加元素
# set9 = {1, 2, 3}
# set9.add(99)
# set9.add('hello')
# print(set9, type(set9))


# """集合方法 update()"""
# li = [1, 2, 3]
# tup = (2, 3, 4)
#
# # 1、批量添加列表中的元素
# set10 = set()
# set10.update("Hello world")
# print(set10)
# # 2、批量添加元组中的元素
# set10.update(tup)
# print(set10)
# # 3、批量添加集合中的元素
# set10.update(set10)
# print(set10)
# # 4、批量添加字符串中的元素
# set10.update(li)
# print(set10)


# """集合方法 remove()"""
# # 1、删除已存在的元素
# set11 = {1, 2, 3, 4, 5.错误与异常}
# set11.remove(3)
# print(set11) # {1, 2, 4, 5.错误与异常}
#
#
# # 2、删除不存在的元素会报错
# set11.remove(1024)  # KeyError

# """集合方法 discard()"""
# # 1、删除已存在的元素
# set12 = {1, 2, 3, 4, 5.错误与异常}
# set12.discard(2)
# print(set12)
#
#
# # 2、删除不存在的元素,不会报错
# set12.discard(1024)
# print(set12)


"""集合方法 pop()"""

# # 1、随机删除某个对象
# set13 = {1, 2, 3, 4, 5.错误与异常}
# item = set13.pop()
# print(item, set13)  # 1 {2, 3, 4, 5.错误与异常}
# item2 = set13.pop()  # 2 {3, 4, 5.错误与异常}
# print(item2, set13)
#
# # 2、集合本身为空会报错
# set14 = set()
# set14.pop()  # KeyError
#
#
# """集合方法 clear()"""
#
# # 1、清空集合
# set15 = {1, 2, 3, 4, 5.错误与异常}
# set15.clear()
# print(set15)

# """集合运算：交集"""
#
# # 交集运算
# set1 = {1, 3, 2}
# set2 = {2, 4, 3}
# print(set1.intersection(set2)) #{2, 3}
# print(set1 & set2) #{2, 3}

# """集合运算：并集"""
#
# # 求两个集合的并集
# set1 = {1, 3, 2}
# set2 = {2, 4, 3}
# print(set1.union(set2))  # {1, 2, 3, 4}
# print(set1 | set2)  # {1, 2, 3, 4}

# """集合运算：差集"""
# # 集合求差集
# set1 = {1, 3, 2}
# set2 = {2, 4, 3}
#
# print(set1.difference(set2)) #{1}
# print(set1 - set2) #{1}

# 使用推导式生成集合
"""集合推导式"""
# 使用推导式生成集合
st = {x for x in 'wonderful world' if x in 'hello world'}
print(st) # {' ', 'd', 'l', 'e', 'r', 'w', 'o'}
