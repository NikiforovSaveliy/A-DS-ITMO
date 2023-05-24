# В данной задаче действовать жадным алгоритмом не верное решение. Например: Существует три вещи 10, 2, 3кг, которые
# стоят 100, 60, 70 соответственно. То жадный алгоритм выберет первый предмет, несмотря на то, что существует
#  возможность взять последние две вещи, которые весят по 2 и 3 кг, имея стоимость 130.

def greedy(jewelery: list[tuple], num_of_repeats: int, num_of_jewelery: int, weight: int):
    def get_item(items):
        for i in items:
            yield i

    jewelery.sort(key=lambda d: d[1], reverse=True)  # Сортируем по больше ценности
    item = get_item(jewelery)
    curr_item = next(item)
    res = []
    for i in range(num_of_repeats):
        curr_weight = weight
        time_res = []
        while curr_weight - curr_item[0] >= 0 and num_of_jewelery != 0:
            curr_weight -= curr_item[0]
            num_of_jewelery -= 1
            time_res.append(curr_item)
            curr_item = next(item)
        res.append(time_res)
    return res if num_of_jewelery == 0 else BaseExceptionGroup


test = [(3, 60), (2, 70), (10, 120)]

print(greedy(test, 2, 2, 10))