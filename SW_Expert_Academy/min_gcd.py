# 최대공약수 구하는 함수
def gcd(numbers):
    sorted_numbers = sorted(numbers)
    for gcd_number in range(sorted_numbers[0]+1, 1, -1):
        is_gcd_number = True
        for compared_number in sorted_numbers:
            if compared_number % gcd_number != 0:
                is_gcd_number = False
        if is_gcd_number:
            return gcd_number


# gcd 함수 테스트
# list = [6,9,12]
# print(gcd(list))


def devide_numbers(numbers):
    # sorted_numbers = sorted(numbers)
    tmp = [0]
    devided_numbers_1 = []
    devided_numbers_2 = []

    for number in numbers:
        sw = True
        for number_1 in devided_numbers_1:
            if