# Дан список повторяющихся элементов. Вернуть список
# с дублирующимися элементами. В результирующем списке
# не должно быть дубликатов.
from array import array

list = [1, 1, 1, 2, 2, 3, 3, 4, 5, 6, 7]
print(list)

res = set()
for i in list:
    spam = list.count(i)
    if spam > 1:
        res.add(i)
print(res)







