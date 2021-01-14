# 4344

def is_bigger_than_avg(list_scr):
    bigger_list = []
    avg_scr = float(sum(list_scr)) / len(list_scr)
    for scr in list_scr:
        if scr > avg_scr:
            bigger_list.append(scr)
    return bigger_list


num_test = int(input())
for test in range(num_test):
    list0 = list(map(int, input().split()))
    num_pp = list0.pop(0)
    answer = float(len(is_bigger_than_avg(list0))) / num_pp * 100
    f_answer = format(answer, '.3f')
    print("{}%".format(f_answer))
    # print("{%0.3f}%".format(answer))
