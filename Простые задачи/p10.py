# Дана строка.
# Определите, какой символ в ней встречается раньше: 'x' или 'w'.
# Если какого-то из символов нет, вывести сообщение об этом.
# Для проверки: "qwerty", "zxcvb", "qwertyzxcvb", "zxcvbqwerty"

# Решить с использованием цикла (нужно написать функцию поиска символа в строке)
# code...

def my_finder(s, p):
    k = 0
    for i in s:
        if (i == p):
            return k
        k += 1

    return -1

def y(s):
    x = my_finder(s, 'x')
    w = my_finder(s, 'w')

    if (x == -1):
        return 'x в строке не встречается'
    elif (w == -1):
        return 'w в строке не встречается'
    elif (x > w):
        return 'w встречается раньше'
    else:
        return 'x встречается раньше'

print(y("qwerty"))
print(y("zxcvb"))
print(y("qwertyzxcvb"))
print(y("zxcvbqwerty"))
print("---")

# Решить с использованием метода string.find(string)
# code...

def f(s):
    x = s.find('x')
    w = s.find('w')

    if (x == -1):
        return 'x в строке не встречается'
    elif (w == -1):
        return 'w в строке не встречается'
    elif (x > w):
        return 'w встречается раньше'
    else:
        return 'x встречается раньше'

print(f("qwerty"))
print(f("zxcvb"))
print(f("qwertyzxcvb"))
print(f("zxcvbqwerty"))
