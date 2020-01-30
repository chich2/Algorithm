

# 주어진 선분
def make_line():
    line = list(map(int, input().split()))
    return line


# 주어진 점들의 집합
def make_set_of_points():
    natural_number = int(input())
    set_of_points = []
    for i in range(natural_number):
        point = list(map(int, input().split()))
        set_of_points.append(point)
    return set_of_points


#
def compare_points_for_max_length(line):
    start_point = line[0]
    end_point = line[1]
    max_line = 0
    for point in range(start_point, end_point+1):
        for half_line in


# main
number_of_testcases = int(input())
for testcase in range(number_of_testcases):
    # 주어진 선분
    given_line = make_line()
    # 주어진 점들의 집합
    set_of_points = make_set_of_points()

    # 주어진 선분 위의 점들을 비교해서 가장 큰 사각형의 선분길이 구하기
    max_length_of_square = compare_points_for_max_length(given_line)