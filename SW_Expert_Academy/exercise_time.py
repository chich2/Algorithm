# swea 3431


def calculate_times(para_times):
    Low, Up, X_time = para_times[0], para_times[1], para_times[2]
    if X_time > Up:
        return -1
    elif X_time < Low:
        sub = Low - X_time
        return sub
    else:
        return 0


TestCase = int(input())
for test_case in range(TestCase):
    times = list(map(int,input().split()))
    print("#{} {}".format(test_case + 1, calculate_times(times)))       # format 함수 {} 안에 아무것도 안 넣어도 괜찮다.