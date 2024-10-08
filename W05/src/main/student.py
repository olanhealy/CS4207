class Student:
    def __init__(self, student_id):
        self.student_id = student_id
        self.completed_courses = []


    def course_complete(self, module_code):
        self.completed_courses.append(module_code)
        
