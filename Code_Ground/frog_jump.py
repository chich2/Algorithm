# code_ground "개구리 뛰기"


number_of_testcases = int(input())
for testcase in range(1, number_of_testcases +1):
    print("Case #{}".format(testcase))

    number_of_rocks = int(input())
    set_of_rocks = list(map(int, input().split()))
    set_of_rocks.insert(0,0)
    max_jump_rock = 0
    index_of_rock = 1
    check_end_rock = len(set_of_rocks) - 1

    max_jump_length = int(input())

    number_of_jump = 0
    current_position = 0

    while True:
        rock = set_of_rocks[index_of_rock]
        length = rock - current_position
        if length <= max_jump_length:
            if index_of_rock == check_end_rock:
                number_of_jump += 1
                print(number_of_jump)
                break
            max_jump_rock = rock
            index_of_rock += 1
        elif length > max_jump_length and max_jump_rock == current_position:
            print("-1")
            break
        else:
            current_position = max_jump_rock
            number_of_jump += 1