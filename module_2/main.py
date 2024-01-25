
number = input("Please enter a number: ")
base = input("What is the base of this number?: ")

base_10_value = int(number, int(base))
base_2_value = bin(base_10_value)[2:]

print(f"{number} in base {base} is: {base_10_value} in base 10 and {base_2_value} in base 2")
