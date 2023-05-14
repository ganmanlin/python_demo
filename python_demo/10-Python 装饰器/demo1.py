# 函数引用
def hello_world():
    print("Hello World !")


hw = hello_world # 把函数对象赋值给一个对象
print(hw)  # 打印<function hello_world at 0x7fa9000d0f70>
print(hw()) #打印 Hello World !
