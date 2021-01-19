# 4673

def make_not_self_num(num):
    pre_num = num
    # list_num = list(map(int, str(num).split()))
    # sum_num = int(pre_num) + sum(list_num)

    for i in list(str(num)):
        pre_num += int(i)
    return pre_num


not_self_nums = []
for cnt in range(1, 10001):
    not_self_num = make_not_self_num(cnt)
    not_self_nums.append(not_self_num)

for num in range(1, 10001):
    if num not in not_self_nums:
        print("{0}".format(num))