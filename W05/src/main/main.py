from module import Module
from student import Student
from enrollment import Enrollment


# Declare modules from lab (Modules done in brackets for modules that need to be done, like 
# blockchain, cant break the link)
cs101 = Module("CS101", [])
cs201 = Module("CS201", ["CS101"])
cs202 = Module("CS202", ["CS101"])
cs301 = Module("CS301", ["CS201", "CS202"])

# setup system with enrollment class
system = Enrollment()

# Add modules
system.add_modules(cs101)
system.add_modules(cs201)
system.add_modules(cs202)
system.add_modules(cs301)

# Add students
student_1 = Student("21318204")
student_2 = Student("21318205")
student_3 = Student("21318206")


system.add_students(student_1)
system.add_students(student_2)
system.add_students(student_3)



# Student_1, we will have he can do all modules
print(system.enroll("21318204", "CS101"))
print(system.enroll("21318204", "CS201"))
print(system.enroll("21318204", "CS202"))
print(system.enroll("21318204", "CS301"))

print("=====================================")
print("")
print("")
print("=====================================")

#Student 2 we have him skip 1
print(system.enroll("21318205", "CS101"))
print(system.enroll("21318205", "CS201"))
# should give our prereq msg here
print(system.enroll("21318205", "CS301"))


print("=====================================")
print("")
print("")
print("=====================================")
#Student 3 we have him skip 1 after first 
print(system.enroll("21318206", "CS101"))
# should give our prereq msg here
print(system.enroll("21318206", "CS301"))

# Done 
# Doesnt say have to worry about anyhing about double enrolment or anything so should be g