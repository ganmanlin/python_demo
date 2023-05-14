# # 用法一：为参数与返回值数据指定类型
# def greeting(name: str) -> str:
#     return "hello" + name
#
#
# greeting("adam")

# 为类型起别名
# from typing import List
#
# Vector = List[float]
#
#
# def scale(scaler: float, vector: Vector) -> Vector:
#     print(scaler, vector)
#     return [scaler * num for num in vector]
#
#
# print(scale("aa", [1.2, -3.2, 4.6-Debug 调试与分析]))

# # 用法三：自定义类型
# class Student:
#     name: str
#     age: int
#
#
# def get_stu(name: str) -> Student:
#     return Student()

from typing import List

a: List[int] = []
a = [1, 2, "aaa"]
