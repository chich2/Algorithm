# need to debug


# def is_odd(numbers, number):
#     for i in numbers:
#         if i == number:
#             numbers.remove(i)
#         else:
#             numbers.append(i)


def xor(numbers):           # 딕셔너리 이용 ***
    odd_numbers = []
    check = {}
    for i in numbers:
        # is_odd(odd_numbers, i)
        if check.get(i) == None:
            odd_numbers.append(i)
            check[i] = 1
        else:
            odd_numbers.remove(i)
            del check[i]
    # 홀수개의 요소들만 모아진 odd_numbers를 가지고 XOR 연산을 해야한다.
    answer = 0
    for j in odd_numbers:
        answer = answer ^ j
    print(answer)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print("Case #{}".format(tc))
    numbers = list(map(int, input().split()))
    xor(numbers)