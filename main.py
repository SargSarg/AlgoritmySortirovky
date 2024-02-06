#Наивная сортировка. Постоянно перемешивает массив пока не поймает нужную последовательность
import random  # модуль, с помощью которого перемешиваем массив

# пусть имеем массив всего лишь из 9 элементов
array = [2, 3, 1, 4, 6, 5, 9, 8, 7]

is_sort = False  # станет True, если отсортирован
count = 0  # счетчик количества перестановок

while not is_sort:  # пока не отсортирован
    count += 1  # прибавляем 1 к счётчику

    random.shuffle(array)  # перемешиваем массив

    # проверяем, отсортирован ли
    is_sort = True
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            is_sort = False
            break

print(array)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(count)
# Кол-во сравнений


#Найти кол-во цифр в записи числа 100!(факториал 100)
import math
l = math.factorial(100)
print(len(str(l)))
#158

#Сортировка выбором. Суть это поиск минимального числа и переноса его влево и так далее
array = [2, 3, 1, 4, 6, 5, 9, 8, 7]

for i in range(len(array)):  # проходим по всему массиву
    idx_min = i  # сохраняем индекс предположительно минимального элемента
    for j in range(i, len(array)):
        if array[j] < array[idx_min]:
            idx_min = j
    if i != idx_min:  # если индекс не совпадает с минимальным, меняем
        array[i], array[idx_min] = array[idx_min], array[i]

print(array)


#Отсюда же посчитаем кол-во сравнений просто добавив счетчик
array = [2, 3, 1, 4, 6, 5, 9, 8, 7]

count = 0 #ДОБАВИЛИ с чего отсчитывать
for i in range(len(array)):  # проходим по всему массиву
    idx_min = i  # сохраняем индекс предположительно минимального элемента
    for j in range(i, len(array)):
        count += 1 #ДОБАВИЛИ сам счетчик
        if array[j] < array[idx_min]:
            idx_min = j
    if i != idx_min:  # если индекс не совпадает с минимальным, меняем
        array[i], array[idx_min] = array[idx_min], array[i]

print("Сравнения выбором: ", count) #ДОБАВИЛИ вывод счетчика


#Теперь понменяем код чтоб отсортировало от большего к меньшему
array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
for i in range(len(array)):
    idx_max = i
    for j in range(i, len(array)):
        if array[j] > array[idx_max]:
            idx_max = j
    if i != idx_max:
        array[i], array[idx_max] = array[idx_max], array[i]

print(array)
#[9, 8, 7, 6, 5, 4, 3, 2, 1]



#Сортировка пузырьком. Максимальные элементы уходят вправо при том что сравниваются лишь по два соседних элемента
array = [2, 3, 1, 4, 6, 5, 9, 8, 7]

for i in range(len(array)):
    for j in range(len(array) - i - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]

print(array)


#Сортировка вставками
array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
count = 0
for i in range(1, len(array)):
    x = array[i]
    idx = i
    while idx > 0 and array[idx-1] > x:
        count += 1 #Счетчик сравнений именно сюда
        array[idx] = array[idx-1]
        idx -= 1
    array[idx] = x
print("Сравнения вставками: ", count)

#Сортировка слиянием. Массив делится поплам, потом еще пополам и ещё. Сравниваются элементы, массив разширяется обратно
def merge_sort(L):  # "разделяй"
    if len(L) < 2:  # если кусок массива меньше 2,
        return L[:]  # выходим из рекурсии
    else:
        middle = len(L) // 2  # ищем середину
        left = merge_sort(L[:middle])  # рекурсивно делим левую часть
        right = merge_sort(L[middle:])  # и правую
        return merge(left, right)  # выполняем слияние


def merge(left, right):  # "властвуй"
    result = []  # результирующий массив
    i, j = 0, 0  # указатели на элементы

    # пока указатели не вышли за границы
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # добавляем хвосты
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

f = merge_sort([2, 3, 1, 4, 6, 5, 9, 8, 7])
print(f)


#Быстрая сортировка
def qsort(array, left, right):
    middle = (left + right) // 2

    p = array[middle]
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        qsort(array, left, j)
    if right > i:
        qsort(array, i, right)
    return array

array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
print(qsort(array, 0, len(array) - 1))
#Тут вместо left и right вставить индексы крайних значений
