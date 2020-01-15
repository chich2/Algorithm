# swea 2005

def make_pascal(scale):
    result = []
#    result.append([1])
    for i in range(1, scale+1):
        result_child = []
        for j in range(1, i+1):
            if j is 1 or i==j:
                result_child.append(1)
            else:
                temp = int(result[i-2][j-2])        # 리스트: 0<= < n 이라는 것 명심!
                temp += int(result[i-2][j-1])
                result_child.append(temp)
        result.append(result_child)
    print(result)


T = int(input())
for tc in range(T):
    N = int(input())
    make_pascal(N)
