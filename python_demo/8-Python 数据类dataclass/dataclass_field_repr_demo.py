from dataclasses import dataclass, field


@dataclass
class Cat:
    name: str
    color: str
    # repr=False, 在打印这个对象的时候，就不会包括这个字段
    weight: str = field(default=2, repr=False)


"""
如果为 True（默认值），该字段作为参数包含在生成的 init() 方法中。
如果为 False，该字段不会包含 init() 方法参数中。

体现在，实例化的时候，是否需要传递这个参数
"""
cat = Cat(name="喵喵", color="black")
print(cat)
