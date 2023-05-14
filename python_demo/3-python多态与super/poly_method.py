class China:
    def speak(self):
        print("汉语")


class USA:
    def speak(self):
        print("English")


cn = China()
en = USA()

# 遍历
for x in (cn, en):
    x.speak()
