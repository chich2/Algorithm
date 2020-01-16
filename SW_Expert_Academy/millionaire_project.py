# swea 1859


def max_num(numbers):           # 가장 큰 수의 인덱스와 그 값을 찾아줌
    temp = [0, 0]
    for element in range(len(numbers)):
        if int(numbers[element]) > int(temp[1]):
            temp[0] = element
            temp[1] = numbers[element]
    return temp


def aaa():
    sale_prices = input().split()
    king = max_num(sale_prices)
    sum = 0
    for element in range(int(king[0])):
        sum += (int(king[1]) - int(sale_prices[element]))
    print(sum)


T = int(input())
for tc in range(T):
    print('#{}'.format(tc), end=' ')
    aaa()

    # 가장 큰 수 뒤에 있는 수들도 활용해야한다. 추가해야함!!!!