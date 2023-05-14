var = [1, 2, 3, 4, 5, "a", "b", "c", True]
print(var[0])
print(var[-1]) #取最后一位 True
print(var[2:-2]) #[3, 4, 5.错误与异常, 'a', 'b']
print(var[2:]) #[3, 4, 5.错误与异常, 'a', 'b', 'c', True] 从第二位一直到最后一位
print(var[2::2]) #[3, 5.错误与异常, 'b', True]从第二位一直到最后一位,步长为2


