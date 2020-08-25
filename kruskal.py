# 각 원소가 속한 집합 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 각 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수 V와 간선의 개수 E 입력받기
v,e = map(int, input().split())
parent = [0]*(v+1)

# 자기 자신으로 부모리스트 초기화
for i in range(1, v+1):
    parent[i] = i

# 간선 정보를 받을 리스트 선언
edges = []
result = 0

# 간선에 대한 정보 입력받기
for _ in range(e):
    a,b,cost = map(int, input().split())
    # cost를 먼저 입력받아 sort를 통해 오름차순 정렬
    edges.append((cost,a,b))

edges.sort()

# 사이클이 없는 경우만 집합에 포함
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

# 결과 출력
print(result)