def student_details_decorator(func):
    def wrapper(student_name):
        print("Student Details:")
        func(student_name)
        print("Additional Information: Grade A")
    return wrapper

@student_details_decorator
def print_student_name(name):
    print("Name:", name)

print_student_name("John Doe")
