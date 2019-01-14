# assign string to student_name
student_name = "Alton"
# first character is at index 0
print(student_name[0])

#Examples
# [ ] review and run example - note the first element is always index = 0
student_name = "Alton"
print(student_name[0], "<-- first character at index 0")
print(student_name[1])
print(student_name[2])
print(student_name[3])
print(student_name[4])
# [ ] review and run example
student_name = "Jay"
if student_name[0].lower() == "a":
    print('Winner! Name starts with A:', student_name)
elif student_name[0].lower() == "j":
    print('Winner! Name starts with J:', student_name)
else:
    print('Not a match, try again tomorrow:', student_name)
# [ ] review and run ERROR example
# cannot index out of range
student_name = "Tobias"
print(student_name[6])

#Task 1
#Work with individual string characters
#Remember: the first character in a string is at index 0
# [ ] assign a string 5 or more letters long to the variable: street_name
# [ ] print the 1st, 3rd and 5th characters
# [ ] Create an input variable: team_name - ask that second letter = "i", "o", or "u"
# [ ] Test if team_name 2nd character = "i", "o", or "u" and print a message
# note: use if, elif and else