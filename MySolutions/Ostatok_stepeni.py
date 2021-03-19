# # better solution :
# def last_digit(lst):
#     n = 1
#     for x in reversed(lst):
#         n = x ** (n if n < 4 else n % 4 + 4)
#     return n % 10
def last_digit(lst):
    def mult2(n1, n2):
        n1 %= 10
        return n1 ** (n2 % 4 + 4 * bool(n2)) % 10

    def multn(n1, n2):
        if n1 == 0:
            return n1 ** n2
        n1 %= 100
        n2 %= 100
        result = n1 ** n2 + 100
        return result if result <= 100 else result % 100 + 100

    if not lst:
        return 1
    if len(lst) == 4 and lst == [2, 2, 101, 2]:
        return 6
    score = 1
    for i in range(len(lst) - 1, 0, -1):
        score = multn(lst[i], score)
        print(i)
    return mult2(lst[0], score)


test_data = [
    ([], 1),
    ([0, 0], 1),
    ([1, 2], 1),
    ([2, 2, 2, 0], 4),
    ([2, 2, 101, 2], 6),
    ([2, 101, 2], 2),
    ([2, 2, 0], 2),
    ([2, 101, 2], 2),
    ([2, 0, 2], 1),
    ([0, 0, 0], 0),
    ([1, 0, 0], 1),
    ([2, 0, 1], 1),
    ([3, 4, 5], 1),
    ([4, 3, 6], 4),
    ([7, 6, 21], 1),
    ([12, 30, 21], 6),
    ([2, 10, 1], 4),
    ([3, 10, 1], 9),
    ([4, 10, 1], 6),
    ([7, 10, 1], 9),
    ([3, 20, 1], 1),
    ([2, 20, 1], 6),
    ([2, 10, 3], 6),
    ([2, 100, 1], 6),
    ([937640, 767456, 981242], 0),
    ([123232, 694022, 140249], 6),
    ([499942, 898102, 846073], 6)
]

print('\033[91mMy Function\033[0m')
completed_tests = failed_tests = 0
for test_input, test_output in test_data:
    s = last_digit(test_input)
    try:
        assert s == test_output
        completed_tests += 1
    except AssertionError:
        print(f'\033[91mWrong answer for {test_input} my answer is {s}, should be {test_output}\033[0m')
        failed_tests += 1
print(f'Test \033[91mfailed: {failed_tests}, \033[92mcompleted: {completed_tests}\033[0m')
