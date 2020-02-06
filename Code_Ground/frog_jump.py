

number_of_testcases = int(input())
for testcase in range(1, number_of_testcases +1):
    print("Case #{}".format(testcase))
    number_of_rocks = int(input())
    set_of_rocks = input().split()
    set_of_rocks.insert(0,0)
    max_jumping_lengh = int(input())
    number_of_jumping = 0
    current_position = 0

    while True:
