# def output_students(name, gender, grade=1):
#     print(f"学生的姓名：{name},性别:{gender}，年级：{grade}年级")
#
#
# output_students("哈利", "男生", 2)
# output_students("罗恩", "男生", 2)
# output_students("赫敏", "女生", 2)


# def student_grade(grade):
#     def output_students(name, gender):
#         print(f"学生的姓名：{name},性别:{gender}，年级：{grade}")
#     return output_students
#
#
# stu_info = student_grade(2)
# print(stu_info) # 打印<function student_grade.<locals>.output_students at 0x7fdd12196a60>
# stu_info("哈利", "男生")
# stu_info("罗恩", "男生")
# stu_info("赫敏", "女生")

# 闭包无法修改外部函数的局部变量
def student_grade(grade):
    grade = 2
    print("外函数的年级为", grade)

    def output_students(name, gender):
        grade = 1
        print("内函数的年级为", grade)
        # print(f"学生的姓名：{name},性别:{gender}，年级：{grade}")

    return output_students


stu_info = student_grade(2)
print(stu_info)  # 打印<function student_grade.<locals>.output_students at 0x7fdd12196a60>
stu_info("哈利", "男生")
stu_info("罗恩", "男生")
stu_info("赫敏", "女生")
