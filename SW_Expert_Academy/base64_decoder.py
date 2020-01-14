# 1928

def f(s):                               # 디코딩 함수
    for i in range(len(s) // 4):
        b64 = s[i * 4:(i + 1) * 4]
        b256 = 0
        for j in range(4):
            n = trans(b64[j])
            b256 = (b256 << 6) + n      # 디코딩해서 넣을 6자리 확보 후 삽입
                                        # n(trans(b64[j])가 아스키코드에서 어떻게 6자리의 수로 표현되는지 이해 X

        print(chr(b256 >> 16), end='')
        print(chr((b256 >> 8) & 0xff), end='')
        print(chr(b256 & 0xff), end='')


def trans(s):                       # 아스키 코드와 문제에서 주어진 표의 간극을 매꾸는 함수
    if ('A' <= s and s <= 'Z'):
        n = ord(s) - ord('A')
    elif ('a' <= s and s <= 'z'):
        n = ord(s) - ord('a') + 26
    elif ('0' <= s and s <= '9'):
        n = ord(s) - ord('0') + 52
    elif (s == '+'):
        n = 62
    elif (s == '/'):
        n = 63
    return n


T = int(input())
for tc in range(1, T + 1):
    s = input()
    print('#{}'.format(tc), end=' ')
    f(s)
    print()