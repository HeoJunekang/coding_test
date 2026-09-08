def solution(arr, divisor):
    answer = []

    for i in arr:
        if i % divisor:
            continue
        answer.append(i)

    if len(answer):
        return sorted(answer)
    else:
        return [-1]
        
    