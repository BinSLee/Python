# n,m을 공백으로 구분하여 입력받기
n,m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 list comprehension을 사용하여 0으로 초기화
d = [[0]*m for _ in range(n)]
# 현재 캐릭터의 a,b좌표, 방향 입력받기
a,b,direction = map(int, input().split())
# 현재 좌표 방문처리
d[a][b] = 1

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))
    
# 북,동,남,서 순 방향 정의
dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 왼쪽으로 90도 회전하는 함수
def turn_left():
    # global 사용하여 direction 전역변수 선언
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = a + dx[direction]
    ny = b + dy[direction]
    
    # 왼쪽으로 회전 후 방문할 곳이 있는 경우 한칸 전진
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        a = nx
        b = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 후 갈 곳이 없는 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = a - dx[direction]
        ny = b - dy[direction]
        # 뒤로 갈 수 있는 지 확인
        if array[nx][ny] == 0:
            a = nx
            b = ny
        # 뒷 공간이 바다 일 경우 중단
        else:
            break
        turn_time = 0

# 결과 출력
print(count)
