import yaml

# data = {
#     "client": {"default-character-set": "utf8"},
#     "mysql": {"user": 'root', "password": 123},
#     "custom": {
#         "user1": {"user": "张三", "pwd": 666},
#         "user2": {"user": "李四", "pwd": 999},
#     }
# }
#
# # 用dump 方法把python对象转为 yaml 文档
# with open('myyaml.yml', 'w', encoding='utf-8') as f:
#     # 如果写入内容包含中文，需要将allow_unicode设置为True
#     yaml.dump(data, f, allow_unicode=True)

# 用load方法
with open('myyaml.yml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

print(data)
# 打印 {'client': {'default-character-set': 'utf8'}, 'custom': {'user1': {'pwd': 666, 'user': '张三'}, 'user2': {'pwd': 999, 'user': '李四'}}, 'mysql': {'password': 123, 'user': 'root'}}
print(type(data))  # 打印<class 'dict'>

# 取user1的姓名
user1_name = data['custom']['user1']['user']
print(user1_name) # 打印张三
