# Дана строка.
# Если она начинается на "abc", то заменить их на "www",
# иначе добавить в конец строки "zzz".
# Для проверки: "abc.google.com", "qwe"
# Надо воспользоваться конструкцией arr/string[start:end:step]

def f(s):
    if (s[:3] == 'abc'):
        return 'www' + s[3:]
    else:
        return s + 'zzz'

print(f('abc.google.com'))
print(f('qwe'))
