import time

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

# 점 하나당 세포 최대 크기
def max_length_from_point(point, set_of_points):
    x_point = point
    y_point = 0
    half_length = 0

    while True:
        for i in range(x_point - half_length, x_point + half_length +1):
            for j in range(y_point - half_length, y_point + half_length +1):
                if [i,j] in set_of_points:
                    return half_length * 2

        half_length += 1


# 선분 위 점들을 기반으로 모든 점을 비교하여 세포 최대 크기 한 변 길이 구하기
def compare_points_for_max_length(line, set_of_points):
    start_point = line[0]
    end_point = line[1] +1
    max_line = 0
    for point in range(start_point, end_point):
        temp_line = max_length_from_point(point, set_of_points)
        if max_line < temp_line:
            max_line = temp_line
    return max_line


# main
number_of_testcases = int(input())
for testcase in range(1, number_of_testcases +1):

    start_time = time.time()

    # 주어진 선분
    given_line = make_line()
    # 주어진 점들의 집합
    set_of_points = make_set_of_points()

    end_time = time.time()
    print("WorkingTime : {} sec".format(end_time - start_time))

    # 주어진 선분 위의 점들을 비교해서 가장 큰 사각형의 선분길이 구하기
    max_length_of_square = compare_points_for_max_length(given_line, set_of_points)
    print("Case #{}".format(testcase))
    print(max_length_of_square)