total_mark = float(input("Enter the total mark percentage: "))
if total_mark >90:
    grade = "A"
elif 80 <= total_mark <=89:
    grade ="B"
elif 70 <= total_mark <=79:
    grade ="C"
elif 60 <= total_mark <=69:
    grade ="D"
elif 50 <= total_mark <=59:
    grade ="E"
else: 
    grade = "Failed"

print(f"The grade is: {grade}")