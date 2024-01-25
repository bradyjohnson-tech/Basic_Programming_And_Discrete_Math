def get_input():
    n = int(input("Please enter the size of the number pool n: "))
    k = int(input("Please enter how numbers you would like to guess k: "))
    return k, n


def factorial(num):
    acc = 1
    for i in range(2, num + 1):
        acc *= i
    return acc


values = get_input()  # [k, n] is this order.
k = values[0]
n = values[1]
total_combinations_possible = factorial(n) // (factorial(k) * factorial(n - k))

print("Winning Big: The probability a player hits all 5 drawn numbers is 1/{}".format(total_combinations_possible))
print("Winning Small: The probability a player hits {} drawn numbers is {}/{}".format((k-1), k, total_combinations_possible))

