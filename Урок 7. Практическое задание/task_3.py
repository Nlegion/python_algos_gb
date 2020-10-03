"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, ...

arr[m]
from statistics import median
"""

import timeit
import random
import numpy as np
from statistics import median

a, b = None, None


def Partition(arr, l, r):
    lst = arr[r]
    i = l
    j = l
    while (j < r):
        if (arr[j] < lst):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        j += 1

    arr[i], arr[r] = arr[r], arr[i]
    return i


def randomPartition(arr, l, r):
    n = r - l + 1
    pivot = random.randrange(1, 100) % n
    arr[l + pivot], arr[r] = arr[r], arr[l + pivot]
    return Partition(arr, l, r)


def MedianUtil(arr, l, r, k, a1, b1):
    global a, b
    if (l <= r):
        partitionIndex = randomPartition(arr, l, r)
        if (partitionIndex == k):
            b = arr[partitionIndex]
            if (a1 != -1):
                return
        elif (partitionIndex == k - 1):
            a = arr[partitionIndex]
            if (b1 != -1):
                return
        if (partitionIndex >= k):
            return MedianUtil(arr, l, partitionIndex - 1, k, a, b)
        else:
            return MedianUtil(arr, partitionIndex + 1, r, k, a, b)
    return


def findMedian(arr, n):
    global a
    global b
    a = -1
    b = -1

    if (n % 2 == 1):
        MedianUtil(arr, 0, n - 1, n // 2, a, b)
        ans = b

    else:
        MedianUtil(arr, 0, n - 1, n // 2, a, b)
        ans = (a + b) // 2

    return ans


def num(x):
    return np.median(x)


x = int(input('Введите число элементов:'))

orig_list = [random.uniform(0, 50) for _ in range(2 * x + 1)]

print('Массив:', orig_list)
print('Время импортированного алгоритма (statistics):',
      timeit.timeit("median(orig_list)", setup="from __main__ import median, orig_list", number=1), 'Медиана:',
      median(orig_list))
print('Время импортированного алгоритма (numpy):',
      timeit.timeit("num(orig_list)", setup="from __main__ import num, orig_list", number=1), 'Медиана:',
      num(orig_list))
print('Время предложенного алгоритма:',
      timeit.timeit("findMedian(orig_list, len(orig_list))", setup="from __main__ import findMedian, orig_list",
                    number=1), 'Медиана:', findMedian(orig_list, len(orig_list)))
