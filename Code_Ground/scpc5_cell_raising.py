

# 주어진 점들의 집합
def make_set_of_points():
    natural_number = int(input())

    set_of_points = []

    for i in range(natural_number):
        point = list(map(int, input().split()))
        set_of_points.append(point)

    return set_of_points

# main
number_of_testcases = int(input())
for testcase in range(number_of_testcases):

    line = list(map(int, input().split()))
    l = line[0]
    r = line[1]

    make_set_of_points()

