# Дано число.
# Если оно меньше 7, то вывести Yes,
# если больше 10, то вывести No,
# если равно 9, то вывести Error.

n = int(input())

if (n < 7):
    print("Yes")
elif (n > 10):
    print("No")
elif (n == 9):
    print("Error")