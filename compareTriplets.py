def compareTriplets(a, b):
    answer = [0,0]
    alice, bob = 0, 0
    for x, y in zip(a, b):
        if x > y:
            answer[0] += 1
        if x < y:
            answer[1] += 1
    
    return answer  