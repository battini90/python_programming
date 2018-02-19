#create 3 dict
lloyd = {
    "name": "Lloyd",
    "homework":[90.0,97.0,75.0,92.0],
    "quizzes":[88.0,40.0,94.0],
    "tests":[75.0,90.0]
}
alice = {
    "name": "Alice",
    "homework":[100.0, 92.0, 98.0, 100.0],
    "quizzes":[82.0, 83.0, 91.0],
    "tests":[89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework":[0.0, 87.0, 75.0, 22.0],
    "quizzes":[0.0, 75.0, 78.0],
    "tests":[100.0, 100.0]
}

#create a students list
students = [lloyd,alice,tyler]

for student in students:
    print(student["name"])
    print(student["homework"])
    print(student["quizzes"])
    print(student["tests"])


def average(numbers):
    length = len(numbers)
    total = sum(numbers)
    total = float(total)
    result = total/length
    return result

def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    homework_wt = homework*(10/100)
    quizzes_wt = quizzes*(30/100)
    tests_wt = tests*(60/100)
    avg_weight = homework_wt+quizzes_wt+tests_wt
    return avg_weight

def get_letter_grade(score):
        if score >= 90:
            return "A"
        elif score >=80:
            return "B"
        elif score >=70:
            return "C"
        elif score >=60:
            return "D"
        else:
            return "F"

score = get_average(lloyd)
grade = get_letter_grade(score)
print(grade)


def get_class_average(students):
    results = []
    for student in students:
        results.append(get_average(student))
    return average(results)


print(get_class_average(students))

print(get_letter_grade(get_class_average(students)))






