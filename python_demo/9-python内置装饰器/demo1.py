# 1. 定义
class MethodDemo:
    param_a = 0

    def normal_demo(self):  # 定义一个方法类，第一个参数必须为self
        """
        普通方法
        :return:
        """

        print(f"This is a normal method {self.param_a}")


# 2. 调用
md = MethodDemo()
md.normal_demo()
