# SW Expert Academy 2072번 문제


# 테스트 케이스 갯수 입력받기
def input_t_case():
    t = int(input())
    return t


# 10개의 수 입력받기
def input_numbers():
    n = input()
    list_n = n.split(" ")       # int 형태는 split 함수적용 불가할 수 있음 에러나면 input_tcase 확인
    if chk_10(list_n):
        if chk_rng(list_n):
            return list_n


# 리스트 요소 갯수가 10개 맞는지 체크
def chk_10(l):
    if len(l)==10:
        return True
    else:
        return False


# 리스트 각 요소들이 0~10000 범위인지 체크
def chk_rng(l):
    for n in l:
        if n<0 or n>10000:
            return False
    return True


#홀수 골라내기
def sort_odd(l):
    for n in l:
        if n%2 == 0:
            l[n-1] = 0


# 리스트 요소들 전부 더하기
def add_all(l):
    sum = 0
    for n in l:
        sum += n
    return sum


def main():
    print("start")


if __name__ == '__main__':
    main()