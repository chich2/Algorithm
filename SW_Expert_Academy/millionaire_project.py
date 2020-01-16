# swea 1859


def max_num(numbers):           # 가장 큰 수의 인덱스와 그 값을 찾아줌
    temp = [0, 0]
    for element in range(len(numbers)):
        if int(numbers[element]) > int(temp[1]):
            temp[0] = element
            temp[1] = numbers[element]
    return temp


def aaa(N):
    sale_prices = input().split()
    while True:
        king = max_num(sale_prices)
        sum = 0
        for element in range(int(king[0])):
            sum += (int(king[1]) - int(sale_prices[element]))
        print(sum)
        if king[0] is (N-1):
            break
        else:
            sale_prices = sale_prices[int(king[0])+1:]
            N = N - int(king[0]) + 1


T = int(input())
for tc in range(T):
    print('#{}'.format(tc+1))
    N = int(input())
    aaa(N)

    # 가장 큰 수 뒤에 있는 수들도 활용해야한다. 추가해야함!!!!