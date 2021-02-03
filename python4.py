
#3진법 뒤집기
n = 45
def solution(n):

    answer = ''

    while n >= 1:
        n, rest = divmod(n, 3)
        print(rest)
        answer += str(rest)

    answer = int(answer, 3)

    return answer

print(solution(n))