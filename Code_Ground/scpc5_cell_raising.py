

# 주어진 선분
def make_line():
    line = input().split()
    return line


# 주어진 점들의 집합
def make_set_of_points():
    natural_number = int(input())
    set_of_points = []
    for i in range(natural_number):
        point = int, input().split()
        set_of_points.append(point)
    return set_of_points


def max_length_from_point(point, set_of_points):
    x_point = int(point[0])
    y_point = int(point[1])
    half_length = 0

    while True:
        for i in range(x_point - half_length, x_point + half_length +1):
            for j in range(y_point - half_length, y_point + half_length +1):
                if set_of_points.get([i,j]) != None:
                    return half_length * 2
        half_length += 1




def compare_points_for_max_length(line, set_of_points):
    start_point = int(line[0])
    end_point = int(line[1])
    max_line = 0
    for point in range(start_point, end_point + 1):
        temp_line = max_length_from_point(point, set_of_points)
        if max_line < temp_line:
            max_line = temp_line
    return max_line


# main
number_of_testcases = int(input())
for testcase in range(number_of_testcases):
    # 주어진 선분
    given_line = make_line()
    # 주어진 점들의 집합
    set_of_points = make_set_of_points()

    # 주어진 선분 위의 점들을 비교해서 가장 큰 사각형의 선분길이 구하기
    max_length_of_square = compare_points_for_max_length(given_line, set_of_points)
    print(max_length_of_square)