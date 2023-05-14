class DateFormat:
    def __init__(self, year=0, month=0, day=0):
        self.year = year
        self.month = month
        self.day = day

    def out_date(self):
        return f"输入的时间为{self.year}年，{self.month}月，{self.day}日"

    @classmethod
    def json_format(cls, json_data):
        """
        输入一个字典格式的数据信息，返回(2023,1,2)
        """
        year, month, day = json_data["year"], json_data["month"], json_data["day"]
        print(year, month, day)
        return cls(year, month, day)


json_data = {"year": 2017, "month": 7, "day": 1}
demo = DateFormat.json_format(json_data)
print(demo.out_date())
