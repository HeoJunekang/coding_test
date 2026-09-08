def solution(x):
    answer = True
    arr = []
    is_hashad = x
    while x != 0:
        arr.append(x%10)
        x = x//10

    if is_hashad % sum(arr):
        return False
    return True

