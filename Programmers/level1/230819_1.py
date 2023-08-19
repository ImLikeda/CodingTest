# 프로그래머스
# 코딩테스트 연습 > 연습문제 > 카드 뭉치
# https://school.programmers.co.kr/learn/courses/30/lessons/159994#

def solution(cards1, cards2, goal):
    for text in goal:
        if cards1 and cards1[0] == text:
            cards1.pop(0)
            continue
        elif cards2 and cards2[0] == text:
            cards2.pop(0)
            continue
        else:
            return "No"
    return "Yes"


q = solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"])
assert q == "Yes"
print(q)

q = solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"])
assert q == "No"
print(q)
