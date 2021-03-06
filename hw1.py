# 1. Даны 2 строки long_phrase и short_phrase. Напишите код, который проверяет действительно ли длинная фраза long_phrase длиннее короткой short_phrase. И выводит True или False в зависимости от результата сравнения.

long_phrase = 'Насколько проще было бы писать программы, если бы не заказчики'
short_phrase = '640Кб должно хватить для любых задач. Билл Гейтс (по легенде)'
len(long_phrase) >  len(short_phrase)

# 2. Дана строка text. Определите какая из двух букв встречается в нем чаще - 'а' или 'и'.

text = 'Если программист в 9-00 утра на работе, значит, он там и ночевал'
if text.count('а') > text.count('и'):
    print('а встречается чаще')
else:
    print('и встречается чаще')

# 3. Дано значение объема файла в байтах. Напишите перевод этого значения в мегабайты в формате: 'Объем файла равен 213.68Mb'

size = 224059719
size_Mb = 224059719 / 1048576
result = 'Объем файла равен {:.2f}Mb'.format(size_Mb)
result

# 4. Выведите на экран значение синуса 30 градусов с помощью метода math.sin.

result = 'Синус 30 градусов = {:.1f}'.format(math.sin(math.pi/6))
result

# 5. В прошлом задании у вас скорее всего не получилось точного значения 0.5 из-за конечной точности вычисления синуса. Но почему некоторые простые операции также могут давать неточный результат? Попробуйте вывести на экран результат операции 0.1 + 0.2. Почему результат неточен?
""" ОТВЕТ: Это особенности вычислений на бинарных числах с плавающей точкой. В большинстве языков программирования они основаны на стандарте IEEE 754. 
Числа в JavaScript, double в C++, C# и Java используют 64-битное представление. Источник проблемы кроется в том, что числа выражены через степени двойки. 
В результате рациональные числа (такие как 0.1, то есть 1∕10), знаменатель которых не является степенью двойки, не могут быть выражены точно. """


# 6. В переменных a и b записаны 2 различных числа. Вам необходимо написать код, который меняет значения a и b местами без использования третьей переменной.

a = 513
b = 6782
result = 'a = {:.0f} b = {:.0f}'.format(float((str(b)+str(a))[:len(str(b))]), float((str(a)+str(b))[:len(str(a))]))
result

# 7. Дано число в двоичной системе счисления: num=10011. Напишите алгоритм перевода этого числа в привычную нам десятичную систему счисления.

# Вариант решения: 
int(0b10011)

# Решение с циклом:
for n in range(0, 100):
    if str(bin(n)) == '0b10011':
        print(n)