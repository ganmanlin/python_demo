class Cat:
    name: str
    color: str
    weight: int

    def __init__(self, name, weight, color):
        self.name = name
        self.weight = weight
        self.color = color

    def __str__(self): # 在Python中，print函数打印对象时，默认会调用对象的__str__()方法
        return f"喵星人姓名：{self.name}, 年龄：{self.weight}，颜色：{self.color}"

    def __repr__(self):
        return f"===>>>>> 喵星人姓名：{self.name}, 年龄：{self.weight}，颜色：{self.color}"


if __name__ == '__main__':
    cat = Cat("橘座", 10, "橘色")
    print(cat)
    print(cat.__repr__())
