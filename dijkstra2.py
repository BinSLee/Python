import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수(N)와 간선의 개수(M) 입력받기
n, m = map(int, input().split())
# 시작 노드값 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 저장하기 위한 리스트
graph = [[] for _ in range(n+1)]
# 최단 거리 테이블 무한값으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

# dijkstra 알고리즘
def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐로 삽입
    distance[start] = 0
    heapq.heappush(q,(0, start))
    
    # 큐가 빌때까지 반복
    while q:
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우 최단 거리 테이블 갱신
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
            

# dijkstra 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우 INFINITY 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우 최단거리 출력
    else:
        print(distance[i])