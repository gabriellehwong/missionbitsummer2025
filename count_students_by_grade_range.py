students = [
    ["Alice", 95],
    ["Bob", 82],
    ["Charlie", 77],
    ["Diana", 88],
    ["Eli", 91],
    ["Fiona", 67],
    ["George", 58],
    ["Hannah", 73],
    ["Ian", 60],
    ["Jane", 85]
]

def count_students(list):
    a = 0
    b = 0
    c = 0
    d = 0
    f = 0
    for student in students:
        if student[1] >= 90:
            a += 1
        elif student[1] >= 80:
            b += 1
        elif student[1] >= 70:
            c += 1
        elif student [1] >= 60:
            d += 1
        else:
            f += 1
    print("A:", str("*") * a)
    print("B:", str("*") * b)
    print("C:", str("*") * c)
    print("D:", str("*") * d)
    print("F:", str("*") * f)

count_students(students)