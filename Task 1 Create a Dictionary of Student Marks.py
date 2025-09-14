'''Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.'''

students_records = {
    "Aarav": 85,
    "Priya": 92,
    "Rahul": 78,
    "Sneha": 90,
    "Karthik": 88
}

name = input("Enter the student's name: ")

if name in students_records:
    print(" Marks of students is :",students_records[name])
else:
    print("student not found")

