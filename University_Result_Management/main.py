import marks_validator
import gpa_calculator
import marks_checker
import result_summarizer
print('..........University Result Management System........')
# inputs
subject=['Programing Fundamentel','Discrete structure','ICT','Marketing','Islamic Studies','English','Holy Quran']
cradit_hours=[4,3,3,3,3,3,1]
name=input('Enter your name: ')
roll_number=input('Enter your roll number: ')
marks=[]
for i in range(7):
    obt_marks=int(input(f'Enter marks of {subject[i]}: '))
    marks.append(obt_marks)
# validation
call_1=marks_validator.marks_validator(marks)
# calculation
call_2=gpa_calculator.gpa_calculator(marks,cradit_hours)
# checking pass or fail
call_3=marks_checker.marks_checker(call_2)
#outputs
print('.....Result.....')
result_summarizer.result_summarizer(marks,call_1,call_2,call_3,name,roll_number)
