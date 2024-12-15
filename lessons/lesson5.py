# Пример 1: O(1) — Константная сложность
# Доступ к элементу списка по индексу
def get_element(lst, index):
    return lst[index]

lst = [1, 2, 3, 4, 5]
print(get_element(lst, 2))  # O(1)


# Пример 2: O(n) — Линейная сложность
# Сумма всех элементов списка
def sum_of_numbers(list):
    total = 0
    for i in list:
        total += i
    return total

# lst = [1,2,3,4,5,6,7,8,9,10,11,22,43]
#
# print(sum_of_numbers(lst))


# Пример 3: O(n²) — Квадратичная сложность
# Поиск всех пар в списке
lst = [1,2,3]
def find_pairs(lst):
    pairs = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            pairs.append((lst[i], lst[j]))
    return pairs

# print(find_pairs(lst))

# Пример 4: O(log n) — Логарифмическая сложность
# Бинарный поиск
def binary_search(lst, target):
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# lst = [1, 2, 3, 4, 5, 6, 7, 8]
# print(binary_search(lst, 5))  # O(log n)


# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)
#
#     def __str__(self):
#         return f"Vector({self.x}, {self.y})"
#
#
# v1 = Vector(1, 2)
# v2 = Vector(3, 4)
# v3 = v1 + v2
# print(v3)  # Vector(4, 6)


class CustomList:
    def __init__(self):
        self.data = []

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

    def __str__(self):
        return str(self.data)
#
lst = CustomList()
lst.data = [1, 2, 3]
# print(lst[1])  # 2
# print(lst)  # 2
# lst[1] = 42
# print(lst)     # [1, 42, 3]


# class Greeter:
#     def __init__(self, greeting):
#         self.greeting = greeting
#
#     def __call__(self, name):
#         return f"{self.greeting}, {name}!"
#
# hello = Greeter("Привет")
# print(hello("Мир"))  # Привет, Мир!