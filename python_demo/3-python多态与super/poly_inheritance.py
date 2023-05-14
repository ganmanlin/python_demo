class Human:
    message = "This is Human's property"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def live(self):
        print("Live on earth")


class Student(Human):
    """学生类"""

    def __init__(self, name, age, school):
        # 访问父类的构造方法
        super().__init__(name, age)
        self.school = school

    def live(self):
        print(f"Live on {self.school}")


class Student2(Human):
    """学生类"""

    def __init__(self, name, age, school):
        # 访问父类的构造方法
        super(Student2, self).__init__(name, age)
        self.school = school

    def live(self):
        print(f"Live on {self.school}")


stu = Student('Tom', 12, "NO.1 school")
stu.live()
stu2 = Student('Annie', 15, "NO.2 school")
stu2.live()
