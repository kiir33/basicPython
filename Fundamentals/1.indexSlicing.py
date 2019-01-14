#Accessing sub-strings
#Index Slicing [start:stop]
#String slicing returns a string section by addressing the start and stop indexes

# assign string to student_name

student_name = "Colette"
# addressing the 3rd, 4th and 5th characters
student_name[2:5]

#The slice starts at index 2 and ends at index 5 (but does not include index 5)

#Examples
# [ ] review and run example
# assign string to student_name
student_name = "Colette"

# addressing the 3rd, 4th and 5th characters using a slice
print("slice student_name[2:5]:",student_name[2:5])
# [ ] review and run example
# assign string to student_name
student_name = "Colette"

# addressing the 3rd, 4th and 5th characters individually
print("index 2, 3 & 4 of student_name:", student_name[2] + student_name[3] + student_name[4])
# [ ] review and run example
long_word = 'Acknowledgement'
print(long_word[2:11])
print(long_word[2:11], "is the 3rd char through the 11th char")
print(long_word[2:11], "is the index 2, \"" + long_word[2] + "\",", "through index 10, \"" + long_word[10] + "\"")

#Task 1
#slice a string
#start & stop index
# [ ] slice long_word to print "act" and to print "tic"
long_word = "characteristics"
# [ ] slice long_word to print "sequence"
long_word = "Consequences"