from random import choice, sample
comb = [(i, j) for i in range(2, 10) for j in range(2, 10) if i <= j]
while comb:
    pair = choice(comb)
    x, y = sample(pair, 2)
    while int(input(f'{x} * {y} = ')) != x * y:
        print('\033[91mНеправильно\033[0m')
    print('\033[92mПравильно\033[0m')
    comb.remove(pair)
