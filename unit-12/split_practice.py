# Creating a comma-separated string of African countries
countries = "Nigeria,Ghana,Kenya,South Africa,Rwanda"

#Creating a date in DD/MM/YYYY format
date = "27/11/2026"

#Splitting the countries
country_list = countries.split(",")

# Splitting the date
date_parts = date.split("/")

# Printing individual countries
print("African Countries:")
print(country_list[0])
print(country_list[1])
print(country_list[2])
print(country_list[3])
print(country_list[4])

# printing individual date components using indexes
print("Date:", date)
print("Day:", date_parts[0])
print("Month:", date_parts[1])
print("Year:", date_parts[2])
