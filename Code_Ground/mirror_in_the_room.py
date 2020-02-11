import sys

# inf = open('input.txt');
inf = sys.stdin                 # sys.stdin.readline()

T = inf.readline();


def select_dir(mirror, dir):
    if mirror == "2":
        if dir < 2:
            return dir + 2
        else:
            return dir - 2
    elif mirror == "1":
        return 3 - dir


move_col = [-1, 1, 0, 0]
move_row = [0, 0, -1, 1]

for t in range(0, int(T)):
    N = int(inf.readline());
    mirror = []
    for i in range(N):
        mirror.append(inf.readline().strip("\n"))

    Answer = 0;
    scoreList = [[0] * N for i in range(N)]
    row, col = 0, 0
    dir = 1
    while -1 < row < N and -1 < col < N:
        if mirror[row][col] != "0":
            scoreList[row][col] = 1
            dir = select_dir(mirror[row][col], dir)
            row += move_row[dir]
            col += move_col[dir]

        else:
            row += move_row[dir]
            col += move_col[dir]

    for i in range(N):
        Answer += scoreList[i].count(1)

    # Print the answer to standard output(screen).
    print('Case #%d' % (int(t) + 1))
    print(Answer)
inf.close()