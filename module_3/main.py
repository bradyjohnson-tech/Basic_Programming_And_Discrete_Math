scale_factor = input("Please enter a scale factor: a = ")
ratio = input("Please enter a ratio: r = ")

a = float(scale_factor)
r = float(ratio)

if r > 1:
    number_of_progressions = input("This GP does not converge to a finite number with infinite elements. Please enter "
                                   "a number of progressions to sum: n = ")
    n = int(number_of_progressions)
    S_n = (a * ((r ** n) - 1) / (r - 1))
    print(f"This GP sum with {n} elements is equal to {S_n}")
else:
    S = a / (1 - r)
    print(f"This GP converges with infinite elements to {S}")

gp_array = []
i = 1
while i <= 3:
    nth_term = a * (r ** (i - 1))
    gp_array.append(nth_term)
    i += 1

print(f"The first elements are {str(gp_array[0])}, {str(gp_array[1])}, and {str(gp_array[2])}")
