final = []
board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]

answer=0
for i in moves:
    for j in range(0, 5):
        if board[j][i - 1] == 0:
            continue;
        else:
            final.append(board[j][i - 1]);
            board[j][i - 1] = 0;
            break;





def solution(board, moves):
    answer = 0
    for i in moves:
        for j in range(0, 5):
            if board[j][i - 1] == 0:
                continue;
            else:
                final.append(board[j][i - 1]);
                board[j][i - 1] = 0;

    while True:
        restart = False
        for i in range(0, len(final)):
            if final[i] != final[i + 1]:
                continue
            elif final[i] == final[i + 1]:
                del final[i:i + 2]
                answer = answer + 2
            if not restart:
                break


    return answer


print(final)
