class DateFormat:
    def __init__(self, year=0, month=0, day=0):
        self.year = year
        self.month = month
        self.day = day

    def out_date(self):
        return f"输入的时间为{self.year}年，{self.month}月，{self.day}日"


def json_format(json_data):
    year, month, day = json_data["year"], json_data["month"], json_data["day"]
    print(year, month, day)
    return year, month, day


year, month, day = json_format({"year": 2017, "month": 7, "day": 1})
demo = DateFormat(year, month, day)
print(demo.out_date())
