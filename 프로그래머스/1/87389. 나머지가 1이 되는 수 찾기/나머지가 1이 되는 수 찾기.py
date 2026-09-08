def solution(n):
    answer = 2
    n -= 1
    while n % answer:
        answer += 1
    return answer