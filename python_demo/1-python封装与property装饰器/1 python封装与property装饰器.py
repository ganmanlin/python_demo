class Account:
    """账户"""

    # 普通属性
    bank = "BOC"

    # 保护属性
    _username = "Harry Pott"

    # 私有属性
    __password = "888"

    @property
    def password(self):  # 计算属性
        return self.__password

    @password.setter  # @计算属性名.setter装饰器
    def password(self, value):
        # 增加数据校验
        if len(value) >= 8:
            self.__password = value
        else:
            print("密码长度最少要有8位！")


# 实例化对象
account = Account()

# 修改私有属性
account.password = "^&&"
print(account.password)  # 将会打印w&(&*)(^()

# # 实例化对象
# account = Account()
# # 访问私有属性
# print(account.password)

# print(Account.bank)
# # print(Account._username)
# # print(Account.__password)
# print(Account.__dict__)  # __dict__ 获取对象所拥有的所有可写属性
