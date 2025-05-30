
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    student =[]
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        students.append(name)
    query_name = input()

    avg= [sum(scores ) /len(student_marks) for scores in student for student in students]