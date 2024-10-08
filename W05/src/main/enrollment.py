class Enrollment:

    def __init__(self):
        self.students={}
        self.modules={}

    # A method to add students

    def add_students(self, student):
        self.students[student.student_id] = student
    # A method to add modules  

    def add_modules(self, modules):
        self.modules[modules.module_code] = modules
    # A method to check if a student can enroll in a module based on prerequisite completion

    def can_enroll(self, student_id, module_code):
        student = self.students.get(student_id)
        module = self.modules.get(module_code)
        if not student or not module:
            return False, "Student or module doesnt exist"
        
        prerequisites = [
            prereq for prereq in module.modules_done 
            if prereq not in student.completed_courses
        ]

        if prerequisites:
            return False, f"Cannot enroll, missing prerequisites: {', '.join(prerequisites)}"
        return True, f"Enrollment successful for module: {''.join (module_code)}"

    # A method to enroll a student in a module
    def enroll(self, student_id, course_code):
        can_enroll, message = self.can_enroll(student_id, course_code)
        if can_enroll:
            student = self.students[student_id]
            student.course_complete(course_code)
        return message

