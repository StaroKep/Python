# Дана строка. Показать третий, шестой, девятый и так далее символы.
# Для проверки "Hello, world!", "1234567890"
# Надо воспользоваться конструкцией arr/string[start:end:step]

def f(s):
    return s[2::3]

print(f("Hello, world!"))
print(f("1234567890"))