#1. Manuel Salgado 

# for student in students:
#     print("Name: " + student['Combo,Name'])
#     print("Email 1: " + student['Email'][0])
#     print("Email 2 : " + student['Email'][1])
#     print('-' *25)

#2. Search for students in a specific homeroom LILLY 
# HMR_code = int(input("What is your homeroom? "))
# HR_code = input("What is your homeroom? ")
# found = False
# for student in students:
#     if HR_code == student["HR"]:
#         print(student["Combo,Name"])
#         print(student["Email"][0])
#         print(student["Email"][1])
#         break
#     elif not found:
#             print("No students found in homeroom. ")
        

# #3 Check if a student is in a list DANIEL 
# first_name = input("What is your first name? *make sure to capatalize the first letter of your first/last name: ")
# for student in students: 
#     if first_name == student['Combo,Name']:
#         print("Name: " + student["Combo,Name"] + " " +  student["HR"])



# #4 Filter Students by Grade Level Manuel Salgado 

# for student in students:
#     if student['GL'] == 10:
#         print("Student Name: " + student["Combo,Name"])
#         print("Student ID : " + str(student["CPSID"]))
#         print('-' * 25)
      



# # 5. Format email list newsletter Forma Email List Lilly 
# for student in students:
#     print(student["Email"][0], end=", ")
#     print(student["Email"][1], end=", ")
#     if student["Email"][-1]:
#         print(student["Email"][1], end=" ")



# #6 Daniel

# frequency_list = len(students("Combo, Name"))
# # if len(students) = 
# # for student in students:  
# #     if last_name == student[LN]:
# #         print("["LN"] Occurs most frequently" + frequency_list))
# print(frequency_list)




# #7 Manuel
# student_count = 0
# for student in students:
#     if student['HR']:
#         print(student["HR"])
#         print(len(student["HR"][0]))
#         student_count = student_count + 1    


# 8. Validate email patterns Lilly
# for student in students: 
#     if "@" not in student["Email"][0]: 
#         print(student["Email"][0])
#         if "@" not in student["Email"][1]: 
#             print(student["Email"][1])
