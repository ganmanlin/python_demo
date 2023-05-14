# list_a = ["a", "b", "c"]
# str_a = "abcde"
# str_b = "bcde"
#
# print("a" in list_a)
# print("a" not in list_a)
# print("a" in str_a)
# print("a" not in str_a)
# print("a" in str_b)


list_a = ["a", "b", "c"]
list_b = ["a", "b", "c"]

print(id(list_a)) # 使用id查看变量的内存地址
print(id(list_b))
print(list_a is list_b)
print(list_a == list_b)