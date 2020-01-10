import random


def main():
    while True:
        print('-' * 20)  # *를 활용한 반복 출력
        print('대리님 까짓꺼 묻고 더블루 가십쇼^^')
        print('-' * 20)

        while True:  # while true
            n = input("로또 몇 판 하실 거에요?(정수로 부탁드립니당) : ")

            if (n.isdigit() == True and 0 < int(n) < 6):  # 조건 맞다면 진행할 것
                print('-' * 20)
                for i in range(0, int(n)):
                    lottonumber = random.sample(range(1, 46), 6)  # random.sample(a,b)
                    lottonumber.sort()  # 정렬하기
                    print(lottonumber)
                break  # 수행 후 빠져나가기

            else:  # 조건 안맞을 시 진행할 것
                print('-' * 20)
                print("1~5 사이의 숫자를 입력하셔야해요.")
                print('-' * 20)
                continue  # while문 재실행

        print('-' * 20)
        print('행운이 가득하시기를 빌어요!!!')
        print('-' * 20)
        continue


if __name__ == '__main__':
    main()