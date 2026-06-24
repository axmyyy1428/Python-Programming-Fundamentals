def marks_validator(marks):
    for i in range(len(marks)):
        if marks[i]<=100 and marks[i]>=0:
            validator='Marks is valid!'
        else:
            validator='Marks is not valid!'
        return validator
