INF = int(1e9)
# 전체 회사 개수 M, 경로의 개수 N 입력받기
print("전체 회사 개수 M, 경로의 개수 N 입력")
n,m = map(int, input().split())

# 2차원 리스트 생성 및 무한으로 초기화
graph = [[INF]*(n+1) for _ in range(n+1)]
# 자기 자신으로의 비용 0으로 초기화
for a in range(n):
    for b in range(n):
        if a == b:
            graph[a][b] = 0

print("연결된 회사 정보 입력받기")
for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

print("물건을 판매할 회사 X, 중간에 방문할 회사 K 입력받기")
x,k = map(int, input().split())

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 계산 결과 받기
distance = graph[1][k]+graph[k][x]

# 도달할 수 없는 경우 -1 출력
if distance >= INF:
    print("-1")
# 도달할 수 있는 경우 거리 출력
else:
    print(distance)