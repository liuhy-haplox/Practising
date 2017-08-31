>>> items = [0, 1, 2, 3, 4, 5, 6]
>>> a = slice(2, 4)
>>> items[2:4]
[2, 3]
>>> items[a] = [8, 9]
>>> items
[0, 1, 8, 9, 4, 5, 6]
>>> del items[a]
>>> items
[0, 1, 4, 5, 6]
