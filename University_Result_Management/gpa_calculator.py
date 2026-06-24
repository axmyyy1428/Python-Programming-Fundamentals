def gpa_calculator(marks,cradit_hours):
    grade_points=[]
    for i in range(len(marks)):
        if marks[i]<=100 and marks[i]>=90:
            points=4.0
        elif marks[i]<=89 and marks[i]>=80:
            points=3.0
        elif marks[i]<=79 and marks[i]>=70:
            points=2.0
        elif marks[i]<=69 and marks[i]>=60:
            points=1.0
        elif marks[i]<=60:
            points=0.0
        else:
            points=0.0
        a=points*cradit_hours[i]
        grade_points.append(a)
    total_grade_points=sum(grade_points)
    total_cradit_hours=sum(cradit_hours)
    gpa=total_grade_points/total_cradit_hours
    return gpa
