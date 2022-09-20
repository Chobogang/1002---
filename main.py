import math

n = int(input())
result = []

for _ in range(n) :
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    # 두 점의 거리 
    distance = math.sqrt((x1 - x2)**2  + (y1 - y2)**2)

    if distance == 0 :
        if r1 == r2 :
            result.append(-1)
        else : result.append(0)
    else :  # 중심이 다를 때
        # 1번 조건, 외접원이며 한 점 접함, 2번 조건, 내접원 한 점 접합
        if r1 + r2 == distance or abs(r2 - r1) == distance :
            result.append(1)
        # 두 반지름 뺄셈이 작으며, 덧셈이 크다면 두점에서 만나게 된다.
        elif ((abs(r2-r1) < distance) and (distance < r1+r2)) :
            result.append(2)
        else : 
            result.append(0)

for i in result :
    print(i)