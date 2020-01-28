def moving(max, start, by, end):
    if max is 1:
        print("{} -> {}".format(start, end))
    else:
        moving(max-1, start, end, by)
        print("{} -> {}".format(start, end))
        moving(max-1, by, start, end)


T = int(input())            # T is number of test case
for tc in range(1, T+1):
    N = int(input())        # N is number of dish
    print("Case #{}".format(tc))
    moving(N, 1, 2, 3)