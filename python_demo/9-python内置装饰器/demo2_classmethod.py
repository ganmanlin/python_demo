# 1. 定义
class MethodDemo:
    CLASS_METHOD = 0

    def __init__(self):
        self.a = "abc"

    def demo_method(self):
        print("This is  normal method")

    def demo_method2(self):
        self.demo_method()
        print("This is  normal method2")

    @classmethod
    def classmethod_demo(cls):
        """
        类方法，第一个参数要改为cls
        :return:
        """
        # cls.demo_method()  # 报错，类方法内，不可以直接调用实例方法
        # cls.a  # 报错，类方法内，不可以直接调用实例变量

        print(f"This is a class method {cls.CLASS_METHOD}")
        cls.classmethod_demo2()

    @classmethod
    def classmethod_demo2(cls):
        """
        类方法，第一个参数要改为cls
        :return:
        """
        print(f"This is a class method2")


# 2. 调用
# 在调用的过程中，类和实例都可以直接调用类方法
MethodDemo.classmethod_demo()
md = MethodDemo()
md.classmethod_demo2()