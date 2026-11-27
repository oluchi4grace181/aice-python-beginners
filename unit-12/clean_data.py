# Creating strings with extra whitespace and inconsistent capitalisation
name = "  oLUchi gRACE oNWUKA  "
course = "  SOFTWARE engineering FOUNDATIONS  "

# printing original values
print("Original name:", repr(name))
print("Original course:", repr(course))

#Cleaning the strings
clean_name = name.strip().title()
clean_course = course.strip().lower()

# Using replace()
clean_course = clean_course.replace("foundatiins","basics")

# Printing cleaned values
print("Cleaned name:",clean_name)
print("Cleaned course:",clean_course)
