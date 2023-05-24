# Каждая строка и столбец отсортированы
matrix = [
    [1, 4, 7, 11, 15, 16],
    [2, 5, 8, 12, 19, 22],
    [3, 6, 9, 16, 22, 24],
    [10, 13, 14, 17, 24, 27],
    [18, 21, 23, 26, 30, 36],
]


# сложность O(m + n)
def find_num(nums, target):
    m, n = len(nums), len(nums[0])
    i, j = 0, n - 1
    while i < m and j >= 0:
        # Будем проверять с левого верхнего, так как он отсортирован
        if nums[i][j] == target:
            # Выводим i,j если нашелся искомый элемент
            return i, j
        if matrix[i][j] > target:
            # Если больше, чем искомый, то переходим на следующий столбец
            j -= 1
        else:
            # Иначе идем вглубь
            i += 1
    return None

print(find_num(matrix, 14))