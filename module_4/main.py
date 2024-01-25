def get_input():
    j = validate_subsets(int(input("Please enter a number of subsets no smaller than 3 and no larger than 8: j = ")))
    m_values = get_m(j)
    t = sum_of_m(m_values)
    k = validate_number_of_arrangements(t, int(input("Please enter the total number of arrangements. (This "
                                                     "number must be smaller than the sum of the sizes of the"
                                                     " subsets - n): k= ")))
    return j, m_values, k


def validate_subsets(subsets):
    if 3 <= subsets <= 8:
        return int(subsets)
    else:
        subsets = input("The number you entered is not valid because it is smaller than 3 or larger than 8 please "
                        "submit a number no smaller than 3 and no larger than 8: j = ")
        return validate_subsets(int(subsets))


def get_m(n):
    arr = []
    for i in range(n):
        subset_size = input("Please enter the size of m{} within the range of 1 to 5: m = ".format(i + 1))
        string_m = validate_subset_size(int(subset_size))
        arr.append(int(string_m))
    return arr


def validate_subset_size(subset_size):
    if 1 <= subset_size <= 5:
        return subset_size
    else:
        subset_size = input("The subset size you entered is not valid because it is smaller than 1 or larger than 5. "
                            "Please submit the size of each subset within the range of 1 to 5: m = ")
        return validate_subset_size(int(subset_size))


def validate_number_of_arrangements(t, total_number_of_arrangements):
    if t > total_number_of_arrangements:
        return total_number_of_arrangements
    else:
        total_number_of_arrangements = int(input("The total number of arrangements is not smaller than the size of "
                                                 "the subsets - n. Please enter a number smaller than {}, "
                                                 "k = ".format(t)))
        return validate_number_of_arrangements(t, total_number_of_arrangements)


def factorial(n):
    acc = 1
    for i in range(2, n + 1):
        acc *= i
    return acc


def calculate_m(m):
    acc = 1
    for i in m:
        acc = acc * factorial(i)
    return acc


def sum_of_m(m):
    acc = 0
    for i in m:
        acc = acc + i
    return acc


inputs = get_input()  # [n, m, k] is the order
n = inputs[0]
m_values = inputs[1]
k = inputs[2]

m_items_factorial_total = calculate_m(m_values)

sum_of_m = sum_of_m(m_values)

a = factorial(sum_of_m) // (factorial(sum_of_m - k) * m_items_factorial_total)

print("given your inputs, the number of arrangements is {}".format(a))


