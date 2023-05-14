# 实现一个计时器的装饰器，计算函数执行时间
# 三步骤:
# 1.定义一个外函数，外函数有一个形参，接受被装饰的函数对象 ；
# 2. 定义一个内函数，内函数内调用传入参数
# 3. 定义外函数的返回值，外函数的返回值固定格式为内函数的函数对象
import datetime


def timer(func):
    # 如果被装饰函数有参数，那么需要在内函数加形参，在函数调用的时候添加参数信息
    # 如果参数个数不固定，把2个地方的参数都换成布丁场参数
    def inner(*args, **kwargs):
        start_time = datetime.datetime.now()
        func(*args, **kwargs)
        end_time = datetime.datetime.now()
        print("函数的执行时间:", end_time - start_time, "\n")

    return inner


@timer
def decorator_demo():
    print("decorate demo print")


@timer
def decorator_demo2(name, age, gender):
    print("decorate demo2 print")
    print(f'{name}-{age}-{gender}')


decorator_demo()
decorator_demo2("罗恩", 11, "男生")
