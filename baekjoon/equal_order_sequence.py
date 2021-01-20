# 1065

def is_equal_order(nums):
    if nums < 100:
        return True
    else:
        cnt = 1         # 숫자 자릿수
        differ = 0
        pre = 0
        for num in list(str(nums)):
            if cnt == 1:                # 첫째 자리
                pre = int(num)
                cnt += 1
            elif cnt == 2:              # 둘째 자리
                differ = int(num) - pre
                pre = int(num)
                cnt += 1
            elif cnt == 3:              # 셋째 이상 자리
                if differ != (int(num) - pre):
                    return False
                else:
                    pre = int(num)
        return True


cnt = 0
for nums in range(1, int(input()) + 1):
    if is_equal_order(nums):
        cnt += 1
print(cnt)