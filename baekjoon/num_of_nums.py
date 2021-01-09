# 2577

# 입력
mul = 1
for i in range(3):
    mul *= int(input())
mul = list(str(mul))

# 출력
for num in range(10):
    print(mul.count(str(num)))      # count는 str 형태만 가능