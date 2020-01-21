# sw 3752


def main():
    tc = int(input())
    for t in range(1, tc + 1):          # 전체 테스트 반복
        score = [0]
        vi = [0] * (100 * 100 + 1)
        n = input()
        nums = list(map(int, input().split()))
        for i in nums:
            for j in range(0, len(score)):
                tmp = i + score[j]
                if not vi[tmp]:
                    vi[tmp] = True
                    score.append(tmp)

        print("#%d %d" % (t, len(score)))


if __name__ == '__main__':
    main()