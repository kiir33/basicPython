#Examples
#access the last character with the -1 index
#negative index counts back from the last character in a string

# [ ] review and run example

student_name = "Joana"

# get last letter
end_letter = student_name[-1]
print(student_name,"ends with", "'" + end_letter + "'")

# [ ] review and run example
# get second to last letter
second_last_letter = student_name[-2]
print(student_name,"has 2nd to last letter of", "'" + second_last_letter + "'")
# [ ] review and run example
# you can get to the same letter with index counting + or -
print("for", student_name)
print("index 3 =", "'" + student_name[3] + "'")
print("index -2 =","'" + student_name[-2] + "'")

#Task 2
# [ ] assign a string 5 or more letters long to the variable: street_name
# [ ] print the last 3 characters of street_name
# [ ] create and assign string variable: first_name
# [ ] print the first and last letters of name

#Task 3
#Fix the Errors
# [ ] Review, Run, Fix the error using string index
shoe = "tennis"
# print the last letter
print(shoe[-1])
