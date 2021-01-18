# 4673

def make_not_self_num(num):
    pre_num = num
    list_num = list(map(int, str(num).split()))
    sum_num = int(pre_num) + sum(list_num)
    return sum_num


not_self_nums = []
for cnt in range(10001):
    not_self_nums.append(make_not_self_num(cnt))

for num in range(10001):
    if num not in not_self_nums:
        print(num)