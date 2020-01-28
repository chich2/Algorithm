
def is_odd(numbers, number):
    for i in numbers:
        if i == number:
            numbers.remove(i)
        else:
            numbers.append(i)


def xor(numbers):
    odd_numbers = []
    for i in numbers:
        is_odd(odd_numbers, i)

    # 홀수개의 요소들만 모아진 odd_numbers를 가지고 XOR 연산을 해야한다.



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print("Case #{}".format(tc))
    numbers = list(map(int, input().split()))
    xor(numbers)