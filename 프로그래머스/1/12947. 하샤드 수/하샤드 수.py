def solution(n):
    
    harshad = sum(map(int, str(n)))
    if n%harshad:
        return False
    return True