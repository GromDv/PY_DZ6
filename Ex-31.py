# Задача 31: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 5
# 15
# Вывод: [1, 9, 13, 14, 19]

a = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

st = input('Введите через пробел нижнюю и верхнюю границы диапазона: ')
st = list(map(int, st.split(' ')))
res = []
for ix,vl in enumerate(a):
    if vl > st[0] and vl < st[1]:
        res.append(ix)

print(res)