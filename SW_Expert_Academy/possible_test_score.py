# sw 3752


def main():
    tc = int(input())
    for t in range(1, tc + 1):          # 전체 테스트 반복, t가 1부터 tc까지 보기좋게 만듬 => 겟
        score = [0]
        vi = [0] * (100 * 100 + 1)      # 조합이 최대 만개가 될 수 있다는 것인가?????
        n = input()
        nums = list(map(int, input().split()))      # nums : 받은 자연수
        for i in nums:
            for j in range(0, len(score)):
                tmp = i + score[j]
                if not vi[tmp]:
                    vi[tmp] = True
                    score.append(tmp)

        print("#%d %d" % (t, len(score)))


if __name__ == '__main__':
    main()