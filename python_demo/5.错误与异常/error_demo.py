# # num = 1
# # if num <= 1:
# #     print("num >1")
# # elif num <= 100:
# #     print("num <100")
#
# def div(a, b):
#     return a / b
#
#
# try:
#     print(div(1, 0))
#     list1 = [1, 2, 3]
#     print(list1[3])
# except ZeroDivisionError as e:
#     print(e)
#     print("这里有个异常")

# def div(a, b):
#     return a / b
#
#
# try:
#     print(div(1, 1))
#     list1 = [1, 2, 3]
#     print(list1[3])
# except Exception as e:
#     print(e)
#     print("这里有个异常")

# def div(a, b):
#     return a / b
#
#
# f = open("data.txt")
# try:
#     print(div(1, 1))
#     list1 = [1, 2, 3]
#     print(list1[3])
#     f.readlines()
# except Exception as e:
#     print(e)
#     print("这里有个异常")
# finally:  # 不管有没有异常都会执行的代码
#     f.close()

# def set_age(num):
#     if num <= 0 or num > 200:
#         raise ValueError(f"值错误{num}")
#     else:
#         print(f"设置的年龄为：{num}")
#
# set_age(-1)


class MyException(Exception):
    def __init__(self, msg):
        print(f"This is a exception: {msg}")

    def __str__(self):
        return repr(self.msg)


def set_age(num):
    if num <= 0 or num > 200:
        raise MyException(f"值错误{num}")
    else:
        print(f"设置的年龄为：{num}")


set_age(-1)
