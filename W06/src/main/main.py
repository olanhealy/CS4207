from module import Module
from student import Student
from enrollment import Enrollment
import multiprocessing

def simulate_enrollment(enrollment_system, student_id, module_code):
    result = enrollment_system.enroll(student_id, module_code)
    print(result)

if __name__ == "__main__":
    # Create an Enrollment system with one shared slot for the module
    cs101 = Module("CS101", [])
    cs201 = Module("CS201", ["CS101"])
    cs202 = Module("CS202", ["CS101"])
    cs301 = Module("CS301", ["CS201", "CS202"])
    system = Enrollment(slots=6)

    # Adding a module (you need to create a Module object)
    system.add_modules(cs101)
    system.add_modules(cs201)
    system.add_modules(cs202)
    system.add_modules(cs301)

    # Adding students
    student_1 = Student("21318204")
    student_2 = Student("21318205")
    student_3 = Student("21318206")
    student_4 = Student("21318207")
    student_5 = Student("21318208")
    student_6 = Student("21318209")
    student_7 = Student("21318210")


    system.add_students(student_1)
    system.add_students(student_2)
    system.add_students(student_3)
    system.add_students(student_4)
    system.add_students(student_5)
    system.add_students(student_6)
    system.add_students(student_7)


    # TASK1: Stimulate Race condition
    process_1 = multiprocessing.Process(target=simulate_enrollment, args=(system, '21318204', 'CS101'))
    process_2 = multiprocessing.Process(target=simulate_enrollment, args=(system, '21318205', 'CS101'))
    process_3 = multiprocessing.Process(target=simulate_enrollment, args=(system, '21318206', 'CS101'))
    process_4 = multiprocessing.Process(target=simulate_enrollment, args=(system, '21318207', 'CS101'))
    process_5 = multiprocessing.Process(target=simulate_enrollment, args=(system, '21318208', 'CS101'))
    process_6 = multiprocessing.Process(target=simulate_enrollment, args=(system, '21318209', 'CS101'))
    process_7 = multiprocessing.Process(target=simulate_enrollment, args=(system, '21318210', 'CS101'))

    # Start both processes
    process_1.start()
    process_2.start()
    process_3.start()
    process_4.start()
    process_5.start()
    process_6.start()
    process_7.start()


    # Wait for both processes to finish
    process_1.join()
    process_2.join()
    process_3.join()
    process_4.join()
    process_5.join()
    process_6.join()
    process_7.join()