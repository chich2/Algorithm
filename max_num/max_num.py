T = int(input())
print(T)
for i in range(0, T):
    while True:
        list_temp = []
        numberString = input()
        numberList_string = numberString.split()       # 나누어서 리스트 형태로 저장
        # print(numberList_string)       # numberList 테스트
        for i in numberList_string:
            if 0 <= int(i) <= 10000:
                list_temp.append(i)

            else:
                print("0 이상 10000 이하의 정수만으로 10자리 다시 입력해주세요.")
                continue
        break
    print(list_temp)

    # !!!!! 틀렸을때 오류 안내문 나오고 다시 입력하도록 되어야 하는데 그냥 넘어가버린다.





    #     if 0 <= n and n <= 10000:
    #         li.append(n)
    #         cnt += 1
    #     else:
    #         print("0 이상 10000 이하의 정수를 입력해주세요")
    #         continue
    #     if cnt is 10:
    #         break
    # print(li)