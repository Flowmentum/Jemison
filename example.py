student_0 = [1, 'joe', 89]
student_1 = [2, 'arsene', 87]
student_2 = [3, 'kayla', 88]

student_0_grades = [89, 90]
student_1_grades = [87, 88, 89, 90, 91]
student_2_grades = [88, 89]

student_0 = {
    'id':1,
    'name':'joe',
    'grades':student_0_grades
    }

student_1 = {
    'id':2,
    'name':'arsene',
    'grades': [87, 88, 89, 90, 91]
}

student_2 = {
    'id':3,
    'name':'kayla',
    'grades':[88, 89]
}

list_of_students = [student_0, student_1, student_2]

#easy_grade_sum = sum_of_student_0_and_1+ list_of_students[2]['grade']


for student in list_of_students:
    print(student['name'])
    print(student['grades'])
    sum_of_grades_for_student = 0
    for grade in student['grades']:
        sum_of_grades_for_student = sum_of_grades_for_student + grade
    num_of_grades_for_student = len(student['grades'])
    avg_for_student = sum_of_grades_for_student/num_of_grades_for_student
    print(avg_for_student)