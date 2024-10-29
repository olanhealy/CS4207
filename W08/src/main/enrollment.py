import multiprocessing
import random

class Enrollment:
    def __init__(self, slots):
        self.students = {}
        self.modules = {}
        self.manager = multiprocessing.Manager() # Manager for shared state across processes
        self.current_enrollment = self.manager.Value('i', 0) # https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Manager
        self.slots = slots  # Set base slots
        self.lock = multiprocessing.Lock() # https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Lock
        self.max_slots = int(slots * 1.2)  # 20% overbooking

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
            if self.current_enrollment.value < self.max_slots:  # Check if slots are within max capacity
                can_enroll, message = self.can_enroll(student_id, module_code)
                if can_enroll:
                    self.current_enrollment.value += 1  # Increase current enrollment
                    student = self.students[student_id]
                    student.course_complete(module_code)
                    return f"Student {student_id} enrolled in {module_code}. Total enrolled: {self.current_enrollment.value}"
                else:
                    return message
            else:
                return f"Cannot enroll, overbooking limit reached for module: {module_code}"

    def finalize_enrollment(self):
        with self.lock:
            # Stimulate Locking enrollment after one week and adjust back to original capacity
            if self.current_enrollment.value > self.slots:  # Check if overbooked
                excess = self.current_enrollment.value - self.slots
                print(f"Excess students to drop: {excess}")

                # Dropping students randomly until back to maximum capacity
                students_to_drop = random.sample(list(self.students.keys()), excess)
                for student_id in students_to_drop:
                    del self.students[student_id]
                    self.current_enrollment.value -= 1  # Reduce current enrollment accordingly
                    print(f"Dropped student {student_id} to maintain capacity.")
            print(f"Final enrollment complete. Total enrolled: {self.current_enrollment.value}")
