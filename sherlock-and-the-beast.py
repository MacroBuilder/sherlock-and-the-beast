def beast(dig):
    maximum = -1
    if dig % 3 == 0:
        maximum = int('5' * dig)
    else:
        test_num = dig
        count = 0
        while test_num % 3:
            test_num -= 5
            count += 5
        if test_num < 0:
            return maximum
        else:
            maximum = int(test_num * '5' + count * '3')
    return maximum

test_cases = int(raw_input().strip())
for _ in xrange(test_cases):
    digits = int(raw_input().strip())
    print beast(digits)
