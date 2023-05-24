from functools import reduce
from matplotlib import pyplot as plt

import random

exponential_filter = lambda data, alpha: reduce(lambda filtered, x: filtered + [alpha * x + (1 - alpha) * filtered[-1]],
                                                data[1:], [data[0]])

data = [i**2 + random.randint(1, 1000) for i in range(10**2)]
scale = [i for i in range(10**2)]

data_filter = exponential_filter(data, 0.4)

plt.plot(scale, data, label='Функция x^2 с шумами')
plt.plot(scale, data_filter, label='Функция x^2 с применением экспоненциального фильтра')

plt.ylabel('y')
plt.xlabel('x')

plt.show()