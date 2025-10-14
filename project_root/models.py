from utils import mean, letter_grade

# 학생 클래스 정의
class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def average(self):
        return mean(self.scores)

    def grade(self):
        return letter_grade(self.average())

# 성적부 클래스 정의
class GradeBook:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def class_average(self):
        total = 0
        for s in self.students:
            total += s.average()
        return total / len(self.students)