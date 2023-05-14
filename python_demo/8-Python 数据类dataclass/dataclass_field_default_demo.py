from dataclasses import dataclass, field


@dataclass
class Cat:
    name: str
    color: str = field(default="white")
    weight: str = field(default=5)
    children: list = field(default_factory=list)
    children1: list = field(default_factory=lambda: [1, 2, 3])
    children2: dict = field(default_factory=lambda: {"name": "喵"})


if __name__ == '__main__':
    cat = Cat("喵喵", "yellow")
    print(cat)
