# """
# 函数体开始执行与结束执行的时候分别添加打印信息
# """
#
#
# # 1. 不使用装饰器的代码
# def decorate_demo():
#     print("装饰器demo")
#
#
# print("函数开始执行")
# decorate_demo()
# print("函数结束执行")
#
#
# # 2. 不使用装饰器的代码，封装函数
# def decorator_demo2():
#     print("装饰器demo")
#
#
# def function_tips(func):
#     print("函数开始执行")
#     func()
#     print("函数结束执行")
#
#
# function_tips(decorator_demo2)

# 3. 使用装饰器的代码
# 第一步，定义2个函数，一个内函数，一个外函数
def timer(func):
    def inner():
        # 第二步，在内函数添加装饰器的逻辑
        print("计数开始")
        func()  # 第六步，添加被装饰函数的执行步骤
        print("计数结束\n")

    # 第三步，把内函数对象return出去
    return inner


# 第四步，装饰器的使用
@timer
def decorator_demo():
    print("装饰器demo")


# 第四步，装饰器的使用
@timer
def decorator_demo2():
    print("装饰器demo2")


decorator_demo()
decorator_demo2()
