# 8958
# str 을 list 처럼 다루면 자동으로 list로 사용된다.

# 입력
num_test = int(input())

# scr = 0
# cnt_o = 1

for tc in range(num_test):
    str = input()

    scr = 0
    cnt_o = 1
    for char in str:
        if(char == 'O'):
            scr += cnt_o
            cnt_o += 1
        else:
            cnt_o = 1
    print(scr)



