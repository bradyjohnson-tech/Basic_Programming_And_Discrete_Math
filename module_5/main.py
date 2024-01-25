def get_input():
    lines = int(input("Please enter between a number between 4 and 8 of lines of the pascal "
                      "triangle you would like to see: "))

    if 4 <= lines <= 8:
        return lines
    else:
        print("That was not between 4 and 8")
        return get_input()


def triangle(n):
    for i in range(1, n + 1):
        for j in range(0, n - i + 1):
            print('  ', end='')

        c = 1
        for j in range(1, i + 1):

            # print(' ', c, sep='', end='')
            print('  ', "{0:^2}".format(c), sep='', end='')

            c = c * (i - j) // j
        print()


triangle(get_input())
