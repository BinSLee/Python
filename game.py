n,m = map(int, input().split())
d = [[0]*m for _ in range(n)]

a,b,direction = map(int, input().split())
d[a][b] = 1

array = []
for i in range(n):
    array.append(list(map(int, input().split())))
    

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0
while True:
    turn_left()
    nx = a + dx[direction]
    ny = b + dy[direction]
    
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        a = nx
        b = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
        
    if turn_time == 4:
        nx = a - dx[direction]
        ny = b - dy[direction]
        
        if array[nx][ny] == 0:
            a = nx
            b = ny
        else:
            break
        turn_time = 0

print(count)
