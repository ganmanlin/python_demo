# def func_with_params(a, b, c):
#     '''
#     这是一个携带参数和注释的函数
#     '''
#     print(f"传入的参数为:a={a},b={b},c={c}")

#
# # 打印函数comments的内容
# print(func_with_params.__doc__)
# # 输出：这是一个携带参数和注释的函数
#
# help(func_with_params)
#
#
# # Help on function func_with_params in module __main__:
# #
# # func_with_params(a, b, c)
# #     这是一个携带参数和注释的函数
#
# # 定义空函数
# def filter_char(s):
#     '''
#     功能：过滤敏感词
#     '''
#     # pass

# def func_demo():
#     print("这是一个函数")
#
#
# def func_with_params(a, b, c):
#     '''
#     这是一个携带参数和注释的函数
#     '''
#     print(f"传入的参数为:a={a},b={b},c={c}")
#
#
# func_demo()
# func_with_params(1, 2, 3)
#
# # 输出:
# # 这是一个函数
# # 传入的参数为:a=1,b=2,c=3


def demo_func(a, b, c):
    print(a, b, c)


# # 1 赋值给 a, 2 赋值给 b, 3 赋值给 c
# demo_func(1, 2, 3)  # 输出：1 2 3
# # 位置参数错误例子，数量错误
# demo_func(1, 2)
# demo_func(1, 2, 3, 4)

# def person(name, age, personality="China"):
#     print(f"姓名为:{name}")
#     print(f"国籍为:{personality}")
#     if age >= 18:
#         print(f"{name} 已成年")
#     else:
#         print(f"{name} 未成年")
#
#
# person(age=12, name="Tom")
# # 输出
# # 姓名为:Tom
# # 国籍为:China
# # Tom 未成年

# # 指定参数默认值错误
# def wrong_demo(a=1, b, c):
#     pass
#
# # 错误示范，默认值为空列表
# def wrong_demo2(a, b, c=[]):
#     c.append(a)
#     c.append(b)
#     print(a, b, c)
#
#
# wrong_demo2(1, 2)
# # 输出: 1 2 [1, 2]
# wrong_demo2(3, 4)
# # 输出: 3 4 [1, 2, 3, 4]

def print_language(*args):
    print(args)
    # for i in args:
    #     print(i)


#
# param = ['China', 'Korea']
# print_language(*param)
# param2 = ('China', 'Korea')
# print_language(*param2)
# print_language('China', 'Korea', 'USA')

def print_info(**kwargs):
    print(kwargs)


print_info(Tom=18, Lily=12)
# {'Tom': 18, 'Lily': 12}
print_info(Tom=18, Lily=12, Anna=16)
# {'Tom': 18, 'Lily': 12, 'Anna': 16-内置库 json}
data = {'Tom': 18, 'Lily': 12, 'Anna': 16}
print_info(**data)
# {'Tom': 18, 'Lily': 12, 'Anna': 16-内置库 json}