def make_pascal(scale):
    result = []
    result.append([1])
    for i in range(1, scale):
        result_child = []
        for j in range(i):
            if j is 0 or i-j is 1:
                result_child.append(1)
            else:
                temp = int(result[i-1][j-1])
                temp += int(result[i-1][j])
                result_child.append(temp)
        result.append(result_child)
    print(result)


T = int(input())
for tc in range(T):
    N = int(input())
    make_pascal(N)
