# Сформировать массив длинны n из элементов арифметической прогрессии
# с заданным первым элементом x и разностью d.
# Для проверки a) n =  10, x = 3, d = 3; b) n = 20, x = 105, d = -5;
# Надо использовать: "".join(), str(), append(), range()

def prog(n, x, d):
    result = []

    for i in range(n):
        result.append(str(x + d * i))

    return ", ".join(result)

print(prog(10, 3, 3))
print(prog(20, 105, -5))
