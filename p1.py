#프로그래머스 과일 장수
# 시간 초과

def solution(k, m, score):
    answer = 0

    score.sort(reverse=True)

    while True:
        if len(score) >= m:
            answer += score[m - 1] * m
            del score[0:m]

        elif len(score) < m:
            return answer
