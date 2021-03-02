def last_digit(lst):
    print(*lst)
    n_max, k_max = 40, 10
    cycles = dict()
    for k in range(k_max):
        cycles[k] = [k ** i % n_max for i in range(1, n_max)]

    if not lst:
        return 1

    def multiplication(n1, n2):
        if n2 == 0:
            return 1
        else:
            # if n1 // k_max > 100 and n1 % k_max == 0:
            #     n1 = 1000
            n1_last_digit = n1 % k_max
            cycle = cycles[n1_last_digit]
            return cycle[(n2 % n_max) - 1]

    def last_dgt(n1, n2):
        if n2 == 0:
            return 1

        cycle = [n1 % 10]
        while True:
            nxt = (cycle[-1] * n1) % 10
            if nxt == cycle[0]:
                break
            cycle.append(nxt)
        return cycle[(n2 - 1) % len(cycle)]

    result = lst[-1]
    for i in range(len(lst) - 2, -1, -1):
        a = lst[i] % 1000
        b = result % n_max
        result = last_dgt(lst[i], result)
        print(f'lst[{i}] = {lst[i]}, {a} ** {b} = {result}')
    return result % 10


test_data = [
    ([2, 2, 101, 2], 6),
    ([12, 30, 21], 6),
    # ([], 1),
    # ([0, 0], 1),
    # ([0, 0, 0], 0),
    # ([0, 0, 0, 0], 1),
    # ([1, 2], 1),
    # ([3, 4, 5], 1),
    # ([4, 3, 6], 4),
    # ([7, 6, 21], 1),
    # ([2, 2, 2, 0], 4),
    # ([937640, 767456, 981242], 0),
    # ([123232, 694022, 140249], 6),
    # ([499942, 898102, 846073], 6)
]
errors, all_test = 0, 0
for test_input, test_output in test_data:
    all_test += 1
    rst = last_digit(test_input)
    try:
        assert rst == test_output
        print(f'{test_input} completed : Should be: {test_output}, really : {rst}')
    except AssertionError:
        print(f'{test_input} \033[91m failed\033[0m : Should be: {test_output}, really : {rst}')
        errors += 1
print(f'\033[91mКоличество ошибок: {errors} из {all_test}\033[0m')

print(f'\033[91m==============================\033[0m')
print(30 ** 21)
print(30 ** 1)
print(30 ** 21 % 4)
print(12 ** ((30 ** 21) % 40000))
print(12 ** ((30 ** 1) % 40000))
print(f'\033[91m==============================\033[0m')

print(2 ** (((101 % 40) ** 2) % 100))
print(2 ** ((2 ** (((101 % 40) ** 2) % 100)) % 100) % 10)

print(2 ** 0 % 10)
print(2 ** 10 % 10)
print(2 ** 100 % 10)
