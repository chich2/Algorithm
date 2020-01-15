N = int(input())
print("{}".format(N))

numbers = sorted(map(int, input().split()))
mid_number = numbers[len(numbers)//2]
print(mid_number)