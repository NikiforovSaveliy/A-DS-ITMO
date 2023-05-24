def find_hole(a):
    """Поиск пропущенного числа. set() - выполняется за O(1) Так что решение линейное"""

    s = set(a)
    for i in range(1, len(s) + 1):
        if not(i in s):
            return i

