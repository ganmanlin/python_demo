# 1.定义
class StaticMethod:
    # 定义: 1. 要用staticmethod 装饰器 2.这个方法没有self/cls
    @staticmethod
    def static_method(param1):
        print("This is a static method", param1)

    def demo_method(self):
        print("This is a normal method")

    @classmethod
    def class_method(cls):
        print("This is a class method")


StaticMethod.static_method("Hello")
demo = StaticMethod()
demo.static_method("Hello2")
