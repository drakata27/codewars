def solution(number):
    total = 0
    for i in range(0, number):
        if i < 0:
            total = 0
            total = 0
        elif i%3==0 or i%5==0:
            total += i
    return total

print(solution(16))