
def max_score(scores, number_of_choosing):
    sorted_scores = sorted(scores)
    sorted_scores.reverse()

    sliced_scores = sorted_scores[:number_of_choosing]
    # 슬라이싱 후
    return sum(sliced_scores)



number_of_testcase = int(input())
for testcase in range(1, number_of_testcase + 1):
    print("Case #{}".format(testcase))
    allSubject_chosenSubject = list(map(int, input().split()))
    number_of_choosing = allSubject_chosenSubject[1]
    scores = list(map(int, input().split()))
    answer = max_score(scores, number_of_choosing)
    print(answer)