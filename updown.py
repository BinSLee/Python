# 공간의 크기 N 입력받기
n = int(input())
# 시작좌표 x,y를 1로 초기화
x,y = 1,1
plans = input().split()
# 이동계획 리스트 선언
move = ['L','R','U','D']
# 이동계획에 따른 x,y좌표의 이동범위
dy = [-1,1,0,0]
dx = [0,0,-1,1]
# 여행가의 이동계획에 따른 좌표변화 계산
for plan in plans:
    for i in range(len(move)):
        if plan == move[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 이동범위 벗어난 경우 무시처리
    if nx < 1 or nx > n or ny < 1 or ny > n:
            continue
    # 이동한 좌표 반영
    x,y = nx, ny

# 결과 출력   
print(x,y)