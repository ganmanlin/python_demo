from dataclasses import dataclass


# 1. 加类装饰器@dataclass
# 2. 为类变量添加类型提示
@dataclass
class Cat:
    name: str
    color: str
    weight: int


if __name__ == '__main__':
    cat = Cat("菠萝", "橘猫", 9)
    print(cat)
