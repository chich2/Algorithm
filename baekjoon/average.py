# 1546
# 정수를 나누어서 실수형으로 출력하는 방법
# sum(), max()

# 입력
num_score = int(input())
list_score = list(map(int, input().split()))

# 계산    총합 * 100 / max / num_score
ans = float(sum(list_score)) * 100 / max(list_score) / num_score
print(ans)