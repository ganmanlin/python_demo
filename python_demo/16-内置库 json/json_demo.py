import json

# 1. python 对象转json字符串
# 定义python结构
data = {
    'a': 1,
    'b': ['2', '3'],
    'c': True,
    'd': False,
    'e': None
}

json_data = json.dumps(data)
print(json_data)  # 打印{"a": 1, "b": ["2", "3"], "c": true, "d": false, "e": null}
print(type(json_data))  # 打印<class 'str'>

# 2. json 字符串转换成python对象
# 定义json字符串

json_data = '''{"a": 1, "b": ["2", "3"], "c": true, "d": false, "e": null}'''
# 将json 字符串转换成python对象
python_data = json.loads(json_data)
print(python_data)  # 打印{'a': 1, 'b': ['2', '3'], 'c': True, 'd': False, 'e': None}
print(type(python_data))  # 打印<class 'dict'>

# 3. 将python 对象转换成json字符串，且写入json文件
data = {
    'a': 1,
    'b': ['2', '3'],
    'c': True,
    'd': False,
    'e': None
}
with open('data.json', 'w') as f:
    json.dump(data, f)  # 当前目录生成一个文件data.json，文件内容为：{"a": 1, "b": ["2", "3"], "c": true, "d": false, "e": null}

# 4. 读取json文件，并且转化为python对象
with open('data.json', 'r') as f:
    data = json.load(f)
    print(data)  # 打印：{'a': 1, 'b': ['2', '3'], 'c': True, 'd': False, 'e': None}

# 定义python结构
data = {
    'a': 1,
    'b': '五一劳动节',
    'c': True,
    'd': False,
    'e': None
}
# 转化为json格式
json_data1 = json.dumps(data)
json_data2 = json.dumps(data, ensure_ascii=False)
json_data3 = json.dumps(data, ensure_ascii=False, indent=4)
print(json_data1)  # 打印 {"a": 1, "b": "\u4e94\u4e00\u52b3\u52a8\u8282", "c": true, "d": false, "e": null}
print(json_data2)  # 打印{"a": 1, "b": "五一劳动节", "c": true, "d": false, "e": null}
print(json_data3)
# 打印
# {
#     "a": 1,
#     "b": "五一劳动节",
#     "c": true,
#     "d": false,
#     "e": null
# }
