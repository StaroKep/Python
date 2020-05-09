# Дана строка.
# Вывести первые три символа и последний три символа, если длина строки больше 5.
# Иначе вывести первый символ столько раз, какова длина строки.
# Для проверки: "Hello, how are you?" и "Good"
# Надо воспользоваться конструкцией arr/string[start:end:step]

def f(s):
    if (len(s) > 5):
        return s[:3] + "\n" + s[-3:]
    else:
        return s[0] * len(s)

print(f("Hello, how are you?"))
print(f("Good"))