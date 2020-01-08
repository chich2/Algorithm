# SW Expert Academy 2072번 문제


def main():
    T = int(input())        # int 형태로 입력받을때 필수
    for i in range(0, T):   # range 이상 미만       이미레인지
        num_temp = input().split()      # input 받은 문장을 바로 스플릿 해서 집어넣기
        sum_temp = 0                    # split => list로 변경됨
        for j in num_temp:              # so, num_temp 는 list
            if int(j) % 2 is not 0:     # is not
                sum_temp += int(j)      # += 가능
        print("#" + str(i + 1) + " " + str(sum_temp))       # 이미레인지라 +1 해주는 모습


if __name__ == '__main__':
    main()