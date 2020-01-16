import math

def rounding(number):
    sub = number - math.floor(number)
    if sub >= 0.5:
        return math.ceil(number)
    else:
        return math.floor(number)

def finding_avg():
    sum = 0
    numbers = input().split()
    for element in range(len(numbers)):
        sum += int(numbers[element])
    print(rounding(sum / 10))


T = int(input())
for tc in range(T):
    print("#{}".format(tc + 1), end=' ')
    finding_avg()
