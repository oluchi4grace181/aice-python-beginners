# Simulating messy student registration data
name = "  oLUchi gRACE oNWUKA  "
email = "  OLUCHI.GRACE@GMAIL.COM  "
telephone = "  +2347030138912  "

# Cleaning each field using method chaining
clean_name = name.strip().title()
clean_email = email.strip().lower()
clean_telephone = telephone.strip().replace(" ", "")

# Validating the registration details
name_valid = len(clean_name) > 0

email_valid = "@" in clean_email
telephone_valid = len(clean_telephone) >= 10

# printing the cleaned student profile
print("STUDENT REGISTRATION PROFILE")
print("------------------------------")
print("Name:", clean_name)
print("Email:", clean_email)
print("Telephone:", clean_telephone)

# printing validation results
print("\nVALIDATION RESULTS")
print("Name valid:", name_valid)
print("Email valid:", email_valid)
print("Telephone valid:", telephone_valid)
