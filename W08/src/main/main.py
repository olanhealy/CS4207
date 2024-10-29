from module import Module
from student import Student
from enrollment import Enrollment
import multiprocessing

def simulate_enrollment(enrollment_system, student_id, module_code):
    result = enrollment_system.enroll(student_id, module_code)
    print(result)

if __name__ == "__main__":
    cs101 = Module("CS101", [])
    cs201 = Module("CS201", ["CS101"])
    cs202 = Module("CS202", ["CS101"])
    cs301 = Module("CS301", ["CS201", "CS202"])
    system = Enrollment(slots=50)  

    system.add_modules(cs101)
    system.add_modules(cs201)
    system.add_modules(cs202)
    system.add_modules(cs301)

    # Add students
    student_ids = [f"21318{str(i).zfill(2)}" for i in range(4, 64)]  
    for student_id in student_ids:
        system.add_students(Student(student_id))

    processes = []
    for student_id in student_ids:
        process = multiprocessing.Process(target=simulate_enrollment, args=(system, student_id, 'CS101'))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    system.finalize_enrollment()
