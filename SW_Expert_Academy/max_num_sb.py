t = int(input())
for i in range(t):      # 그냥 in rnage(t) 하면된다. 나같은경우는 range(0,T) 이렇게 했었는데..
                        # i는 0부터 t-1까지
    line = sorted(list(map(int, input().split())))
    print("#{idx} {data}".format(idx=i+1, data=line[9]))        # format 함수

    # 리스트에 sorted 함수 적용 후, 마지막 요소를 가져와서 가장 큰 수 가져오기
    # 0 이상 10000 이하 조건은 미포함된 듯