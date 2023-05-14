from dataclasses import dataclass, field


@dataclass
class Cat:
    name: str
    color: str
    weight: int = field(default=2)
    # 可变参数，需要通过default_factory来指定类型或者默认值
    # children: list = [1, 2, 3] 报错
    childern: list = field(default_factory=list)


if __name__ == '__main__':
    cat = Cat("小三", "yellow", 9, [1, 2, 3])
    print(cat) # 打印：Cat(name='小三', color='yellow', weight=9, childern=[1, 2, 3])
