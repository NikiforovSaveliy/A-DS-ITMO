# Необходимо дать сдачу в N рублей
# В распоряжении имеется 4 номинала по определенному количеству рублей
# Необходимой найти наименьшую комбинацию монет

def new_item(coins: dict) -> int:
    for i in coins:
        yield i

coins = {
    # Словарь содержащие заданные монеты и их содержание
    10: 10,
    5: 10,
    2: 10,
   # 1: 10,
}

change = int(input('Введите требуемую сдачу: '))
res = []
coins_generator = new_item(coins)
while change != 0 or change < min(coins):
    try:
        curr_coin = next(coins_generator)
    except StopIteration:
        print('Невозможно дать сдачу монетами :(')
        exit(0)

    while change >= curr_coin:
        change -= curr_coin
        coins[curr_coin] -= 1
        res.append(curr_coin)
    if change == 0:
        break
print(res)