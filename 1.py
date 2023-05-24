game_filed = [[None] * 3] * 3


def input_game_field():
    return [input().split(sep=' ') for i in range(3)]


def print_game_field(game_filed):
    for i in game_filed:
        print(i)


def get_elements(a: list, indexes: tuple[int, int]):
    i, j = indexes
    return a[i][j]


def check_victory(game_field, player_a, player_b):
    # Все выйгрышные позиции
    '''
           [(0, 0), (0, 1), (0, 2)],
           [(1, 0), (1, 1), (1, 2)],
           [(2, 0), (2, 1), (2, 2)],
           [(0, 0), (1, 0), (2, 0)],
           [(0, 1), (1, 1), (2, 1)],
           [(0, 2), (1, 2), (2, 2)],
           '''
    vin_pos = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]
    for i in vin_pos:
        if all([get_elements(game_field, j) == player_a for j in i]):
            return f'player {player_a} won'
        if all([get_elements(game_field, j) == player_b for j in i]):
            return f'player {player_b} won'

    return 'DRAW!!!'


if __name__ == '__main__':
    player_a = input('First player name: ')
    player_b = input('Second player name: ')
    game_filed = input_game_field()
    print(check_victory(game_filed, player_a, player_b))
