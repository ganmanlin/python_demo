from dataclasses import dataclass, field, asdict


# 1. 加类装饰器@dataclass
# 2. 为类变量添加类型提示
@dataclass
class Cat:
    name: str
    color: str
    weight: int = field(default=5)


# addict() 直接将实例对象转化成字典格式
cat = Cat("小三", "yellow", 9)
print(asdict(cat))  # 打印{'name': '小三', 'color': 'yellow', 'weight': 9}
