def bubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def binary_search(row, num, low, high):
    mid = len(row) // 2
    while row[mid] != num and low <= high:
        if num > row[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2
    if low > high:
        return mid + 1
    else:
        return mid

try:
    row = list(map(int, input('Введите последовательность чисел через пробел: ').split()))
except ValueError:
    print("Вы ввели не целые чсла, попробуйте снова.")
    exit(0)


row = bubbleSort(row)
print(*(row))

low = 0
high = len(row) - 1

num = int(input(f'Введите любое число в диапазоне от {row[0]} до {row[-1]}: '))
if row[0] > num or num > row[-1]:
    print(f"Вы ввели число выходящее за диапазон последовательности, ведите любое число в диапазоне от {row[0]} до {row[-1]}")
    exit(1)
else:
    print('Номер позиции элемента, который меньше введенного числа, а следующий за ним больше или равен этому числу: ', binary_search(row, num, low, high))
