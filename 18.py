
def calculate_grade(written_test, lab_exams, assignments):
   
    weight_written_test = 70
    weight_lab_exams = 20
    weight_assignments = 10

    grade = (written_test * weight_written_test / 100) + \
            (lab_exams * weight_lab_exams / 100) + \
            (assignments * weight_assignments / 100)
    return grade


print("Enter the marks scored by the student:")
written_test = float(input("Written test: "))
lab_exams = float(input("Lab exams: "))
assignments = float(input("Assignments: "))


grade = calculate_grade(written_test, lab_exams, assignments)


print(f"Grade of the student is {grade:.1f}")
