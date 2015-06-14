"""Having trouble with large values of 'dig'"""

def beast(dig):
    maximum = -1
    for a in range(1, dig + 1):
        if a % 3 == 0 and (dig - a) % 5 == 0:
            if int('5' * a + '3' * (dig - a)) > maximum:
                maximum = int('5' * a + '3' * (dig - a))
        elif a % 5 == 0 and (dig - a) % 3 == 0:
            if int('3' * a + '5' * (dig - a)) > maximum:
                maximum = int('3' * a + '5' * (dig - a))
    return maximum
                
test_cases = int(raw_input().strip())

for _ in range(test_cases):
    digits = int(raw_input().strip())
    print beast(digits)
