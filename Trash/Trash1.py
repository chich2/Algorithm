# SW Expert Academy 2072번 문제


def main():
    T = int(input())        # int 형태로 입력받을때 필수
    for i in range(0, T):   # range 이상 미만       이미레인지
        num_temp = input().split()      # input 받은 문장을 바로 스플릿 해서 집어넣기
        print(num_temp)
        print(type(num_temp))


if __name__ == '__main__':
    main()