import multiprocessing # use for this lab race conditions

class Enrollment:

    def __init__(self, slots):
        self.students = {}
        self.modules = {}
        self.manager = multiprocessing.Manager()  # Manager for shared state across processes
        self.slots = self.manager.Value('i', slots)  # https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Manager
        self.lock = multiprocessing.Lock() # https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Lock

    # A method to add students
    def add_students(self, student):
        self.students[student.student_id] = student

    # A method to add modules  
    def add_modules(self, module):
        self.modules[module.module_code] = module

    # A method to check if a student can enroll in a module based on prerequisite completion
    def can_enroll(self, student_id, module_code):
        student = self.students.get(student_id)
        module = self.modules.get(module_code)
        if not student or not module:
            return False, "Student or module doesn't exist"

        prerequisites = [
            prereq for prereq in module.modules_done 
            if prereq not in student.completed_courses
        ]

        if prerequisites:
            return False, f"Cannot enroll, missing prerequisites: {', '.join(prerequisites)}"

        return True, f"Enrollment successful for module: {module_code}"

    # A method to enroll a student in a module with multiprocessing handling
    def enroll(self, student_id, module_code):
        with self.lock:  # ensures that only one proess can access this part of code at a time
            if self.slots.value > 0:  # Check if slots are available for enrollment i.e. space in course
                can_enroll, message = self.can_enroll(student_id, module_code)
                if can_enroll:
                    self.slots.value -= 1  # if student can enroll, reduce slot count by 1 and enroll
                    student = self.students[student_id]
                    student.course_complete(module_code)
                    return f"Student {student_id} enrolled in {module_code}. Remaining slots: {self.slots.value}"
                else:
                    return message
            else:
                return f"Cannot enroll, no slots available for module: {module_code}"
