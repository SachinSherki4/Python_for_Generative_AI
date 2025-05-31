
if __name__=='__main__':
    students_data=[]
    scores=[]
    for _ in range(int(input("Enter number of student wants to enter : "))):
        stud=input("Enter student name : ")
        score=float(input(("Enter student grade : ")))
        data=[stud,score]
        students_data.append(data)
        scores.append(score)

    second_min_score=sorted(set(scores))[1]
    student_name=sorted([student[0] for student in students_data if student[1]==second_min_score]) # conditio will take only name whose scores are same
    print(student_name)
    print("\n".join(student_name))
