# 10809

# -1로된 리스트 생성
list_alpha = []
for i in range(26):
    list_alpha.append(-1)


# 단어 받아서 변환시키기
word = list(input())
for idx_word in range(0, len(word)):
    idx_alpha = ord(word[idx_word]) - 97
    if list_alpha[idx_alpha] == -1:
      list_alpha[idx_alpha] = idx_word

# print
for i in list_alpha:
    print(i, end=' ')