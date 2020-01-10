T = int(input())            # 테스트 케이스 개수 T 입력받기
print(T)
for i in range(0, T):
    while True:
        cnt = 0                 # 10자리 셀 count 생성
        list_temp = []          # 빈 리스트 생성
        numberString = input()      # 10자리 한번에 입력받기
        numberList_string = numberString.split()       # 나누어서 리스트 형태로 저장
        # print(numberList_string)       # numberList 테스트용
        if len(numberList_string) is not 10:        # 10자리가 아니면 while문 재시작
            print("10자리를 입력하셔야해요.")


            # while문 재시작하게 설정하는 방법을 몰라서 막힘 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


        for i in numberList_string:         # 리스트 요소 하나씩 숫자 범위 체크 후에 타당하면 빈 리스트에 추가하기
            if 0 <= int(i) <= 10000:
                list_temp.append(i)
                cnt += 1                    # 하나씩 추가될 때마다 cnt++
                if cnt is 10:               # 10개 되는 순간 break
                    break
            else:
                print("0 이상 10000 이하의 정수만으로 10자리 다시 입력해주세요.")           # 숫자 제한 범위 초과시 cnt =0으로 만들어서
                cnt = 0                                                                  # break 불가하게 해서 while문 재시작하게 만들기
    print(list_temp)




    #     if 0 <= n and n <= 10000:
    #         li.append(n)
    #         cnt += 1
    #     else:
    #         print("0 이상 10000 이하의 정수를 입력해주세요")
    #         continue
    #     if cnt is 10:
    #         break
    # print(li)