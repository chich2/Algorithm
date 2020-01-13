# SW Expert 2068

T = int(input())            # 테스트 케이스 개수 T 입력받기
print(T)
for i in range(0, T):
    while True:         # 10자리 입력하는 구간
        cnt = 0
        tmp = 0
        numberString = input()      # 10자리 한 문장에 입력받기
        numberList_string = numberString.split()       # 나누어서 리스트 형태로 저장
        if len(numberList_string) is not 10:        # 10자리가 아니면 while문 재시작
            print("10자리를 입력하셔야해요.")
            continue
        for n in numberList_string:         # 리스트 요소 하나씩 숫자 범위 체크 후에 타당하면 빈 리스트에 추가하기
            if 0 <= int(n) <= 10000:
                if tmp < int(n):
                    tmp = int(n)
                cnt += 1
            else:
                print("0 이상 10000 이하의 정수만으로 10자리 다시 입력해주세요.")           # 숫자 제한 범위 초과시 cnt =0으로 만들어서
                continue                                                                # break 불가하게 해서 while문 재시작하게 만들기
        if cnt is 10:
            print('#' + str(i+1) + " " + str(tmp))
            break
