import sys
input = sys.stdin.readline
# 무한값 설정
INF = int(1e9)

# 노드의 개수 N, 간선의 개수 M 입력받기
n,m = map(int, input().split())
# 시작노드 입력받기
start = int(input())
# 각 노드에 연결되어 있는 정보를 저장할 리스트 생성
graph = [[] for _ in range(n+1)]
# 각 노드 방문한 적 있는지 확인하는 리스트 생성
visited = [False] * (n+1)
# 최단 거리 리스트 무한값 초기화
distance = [INF]*(n+1)

# 간선에 대한 정보 입력받기
for _ in range(m):
    a,b,c = map(int, input().split())
    # a 노드에서 b 노드로 가는데 c 비용만큼 든다는 얘기
    graph[a].append((b,c))

# 방문하지 않은 노드 중에서 최소 값 인덱스 반환
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distane[i]
            index = i
    return index

def dijkstra(start):
    # 시작 노드에 대해 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서 방문처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우 최단거리 리스트 갱신
            if cost < distance[j[0]]:
                distance[j[0]] = cost

# 다익스트라 알고리즘 시작
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])