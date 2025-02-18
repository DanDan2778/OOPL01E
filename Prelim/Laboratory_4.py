class Student:
    def __init__(self, student_id, name, course, year_level):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.year_level = year_level

    def display_info(self):
        print(f'Student: {self.student_id}, Name: {self.name}, Course: {self.course}, Year Level: {self.year_level}')

daniel = Student(2001, 'Daniel Agustin', 'BSCpE', 2)
aljin = Student(2002, 'Aljin Nadua', 'BSCpE', 2)
iyaya = Student(2003, 'Jederek Iyaya', 'BSArch', 2)

print('=' * 100)
print('Students Information: ')
print('=' * 100)
daniel.display_info()
aljin.display_info()
iyaya.display_info()
