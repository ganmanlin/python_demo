# """字典使用：创建"""
# # 1、使用大括号填充键值对
# dc1 = {'name': 'Harry Potter', 'age': 18}
# print(type(dc1), dc1)#输出 <class 'dict'> {'name': 'Harry Potter', 'age': 18}
#
# # 2、使用字典构造方法
# dc2 = dict()  # 空字典
# print(type(dc2), dc2)  # 输出：<class 'dict'> {}
# dc2 = dict(name="Harry Potter", age=18)  # 关键字参数赋值
# print(type(dc2), dc2) #输出 ： <class 'dict'> {'name': 'Harry Potter', 'age': 18}
#
# # 3、使用字典推导式
# dc4 = {k: v for k, v in [("name", "Harry Potter"), ("age", 18)]}
# print(type(dc4), dc4) # 输出 ： <class 'dict'> {'name': 'Harry Potter', 'age': 18}
#
#

# """字典使用：访问元素"""
#
# dc = {"name": "Harry Potter", "age": 18}
# # 1、访问存在的key
# print(dc["name"])  # Harry Potter
# print(dc["age"])  # 18
#
# # 2、访问不存在的key，会报KeyError错误
# print(dc['hobby']) # KeyError: 'hobby'


# """字典使用：操作元素"""
# dc = {"name": "Harry Potter", "age": 18}
# # 1、修改年龄，改为20
# dc['age'] = 20
# print(dc)  # {'name': 'Harry Potter', 'age': 20}
#
# # 2、新增hobby字段
# dc['hobby'] = 'Magic'
# print(dc) # {'name': 'Harry Potter', 'age': 20, 'hobby': 'Magic'}


# """字典使用：嵌套字典"""
#
# dc = {
#     "name": "Harry Potter",
#     "age": 18,
#     "course": {
#         "magic": 90,
#         "python": 80
#     }
# }
#
# # 1、获取课程Magic的值
# print(dc['course']['magic']) # 90
#
# # 2、把python分数改成100分
# dc['course']['python'] = 100
# print(dc) #{'name': 'Harry Potter', 'age': 18, 'course': {'magic': 90, 'python': 100}}

# """字典方法 values()"""
# dc = {"name": "Harry Potter", "age": 18}
# values = dc.values()
# print(type(values), values)
# #输出：<class 'dict_values'> dict_values(['Harry Potter', 18])
#
# # 1、遍历查看所有的值
# for value in values:
#     print(value)
# # 输出：
# # Harry Potter
# # 18
#
# # 2、将视图对象转成列表
# print(list(values))
# #输出 ： ['Harry Potter', 18]


# """字典方法 items()"""
# dc = {"name": "Harry Potter", "age": 18}
# items = dc.items()
# print(type(items), items)
# #输出 <class 'dict_items'> dict_items([('name', 'Harry Potter'), ('age', 18)])
# # 1、遍历查看所有的项
# for item in items:
#     print(item)
# # 输出
# ('name', 'Harry Potter')
# ('age', 18)
#
# # 2、将视图对象转成列表
# print(list(items))
# #输出：[('name', 'Harry Potter'), ('age', 18)]


# """字典方法 get()"""
#
# dc = {"name": "Harry Potter", "age": 18}
# # 1、访问存在的key
# name = dc['name']
# print(name)  # Harry Potter
# name2 = dc.get("name")
# print(name2)  # Harry Potter
#
# # 2、访问不存在的key
# hobby = dc.get('hobby')
# print(hobby)  # None

# dc = {"name": "Harry Potter", "age": 18}
# dc.update({"age": 20, "hobby": "magic"})
# print(dc)
# # 输出：{'name': 'Harry Potter', 'age': 20, 'hobby': 'magic'}
# dc.update({"name" : "Harry Potter2"})
# print(dc)
# # 输出：{'name': 'Harry Potter2', 'age': 20, 'hobby': 'magic'}

# """字典方法 pop()"""
#
# dc = {"name": "Harry Potter", "age": 18}
# # 1、弹出
# item = dc.pop("age")
# print(dc, item)
# # 输出：{'name': 'Harry Potter'} 18
#
# # 2、删除不存在的key
# dc.pop("hobby")  # 报错 KeyError: 'hobby'

# # 未使用字典推导式的写法
# dc = [("name", "Harry Potter"), ("age", 18)]
# # 使用字典推导式
# d_new = {k: v for k, v in dc}
# print(d_new)
# # 输出：{'name': 'Harry Potter', 'age': 18}
#
# dc2 = {'a': 1, 'b': 2, 'c': 3}
# dc2_new = {k: v ** 2 for k, v in dc2.items()}
# print(dc2_new)
# # 输出：{'a': 1, 'b': 4, 'c': 9}


"""
给定一个字典对象，请使用字典推导式，将它的key和value分别进行交换。也就是key变成值，值变成key。

输入: {'a': 1, 'b': 2, 'c': 3}
输出: {1: 'a', 2: 'b', 3: 'c'}
"""
dc = {'a': 1, 'b': 2, 'c': 3}
dc_2 = {dc.get(k): k for k, v in dc.items()}
print(dc_2)
dc_3 = {v: k for k, v in dc.items()}
print(dc_3)
