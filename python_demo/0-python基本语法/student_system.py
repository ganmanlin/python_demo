#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
=================================
@File ：student_system.py
@Desc ：None
@Author ：Jenny
@Date ：2023/4/27 14:46 
=================================
"""


class Student:
    def __init__(self, student_id, name, gender):
        self.student_id = student_id
        self.name = name
        self.gender = gender


class StudentList:
    def __init__(self, student_list):
        self.student_list = student_list

    def get_student(self, student_id):
        return [student for student in self.student_list if student_id == student.student_id][0]

    def del_student(self, student_id):
        for i in range(len(self.student_list) - 1):
            if self.student_list[i].student_id == student_id:
                self.student_list.pop(i)


if __name__ == '__main__':
    stu1 = Student(1, "Adam", "Male")
    stu2 = Student(2, "Jenny", "Female")
    stu3 = Student(3, "Hana", "Female")
    student_list = StudentList([stu1, stu2, stu3])

    # 获取学号为1的学生信息
    student = student_list.get_student(1)
    print(student_list.get_student(1).gender)
    print(student_list.get_student(1).name)
    print(student_list.get_student(1).student_id)

    # 删除学号为1的学生信息
    student_list.del_student(1)
    print(student_list)
