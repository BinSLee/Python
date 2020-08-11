# 현재 나이트 위치 입력받기
place = input()
# row에 해당하는 입력받은 값 int로 변환
row = int(place[1])
# column에 해당하는 입력받은 값 ord 함수를 통해 int형으로 변환
column = int(ord(place[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 모든 경우
steps = [(-2,1),(-2,-1),(2,1),(2,-1),(-1,2),(-1,-2),(1,2),(1,-2)]

# 이동횟수 초기화
count = 0
# 나이트가 이동할 수 있는 경우 계산
for step in steps:
    next_row = row + step[0]
    next_colmn = column + step[1]
    # 이동 범위 초과할 경우 무시
    if next_row < 1 or next_row > 8 or next_column < 1 or next_column > 8:
        continue
    count += 1

# 결과 출력
print(count)