def solution(n):
    import math
    if math.sqrt(n) == int(math.sqrt(n)):
        return int((math.sqrt(n) + 1)**2)
    else: return -1