# Дан текст. Найти сумму имеющихся в нем цифр.
# Для проверки: 'qwe1rty2uio3pas4' и 'zxc7a8mn12asd000asdfgh55'
# Надо воспользоваться конструкцией '0' <= symbol <= '9'

def is_numeric(symbol):
    if '0' <= symbol <= '9':
        return True
    return False

def f(s):
    result = 0

    for i in s:
        if is_numeric(i):
            result += int(i)

    return result

print(f('qwe1rty2uio3pas4'))
print(f('zxc7a8mn12asd000asdfgh55'))