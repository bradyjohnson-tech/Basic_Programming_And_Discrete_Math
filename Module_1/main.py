
name = input("What is your name? ")
age = input("How old are you? ")
current_year = input("What is the current year? ")

age = int(age)
current_year = int(current_year)

year_option_1 = current_year - age
year_option_2 = year_option_1 - 1

print("Dear " + name + " you were born either in year " + str(year_option_1) + " or " + str(year_option_2))
