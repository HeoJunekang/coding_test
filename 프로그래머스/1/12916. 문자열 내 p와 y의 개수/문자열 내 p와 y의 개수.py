def solution(s):
    count =0
    s = s.lower()
    for i in s:
        if i =='p':
            count +=1
        elif i == 'y':
            count -= 1
    if count:
        return False
    return True
