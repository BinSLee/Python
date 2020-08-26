# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
 
# 두 원소가 속한 집합 합치기 
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수 n과 간선의 개수 m 입력받기
n,m = map(int, input().split())
# 부모테이블 초기화
parent = [0]*(n+1)

# 부모 테이블 자기 자신으로 초기화
for i in range(1, n+1):
    parent[i] = i

# 간선의 정보를 받을 리스트와 최종 비용을 담을 변수 선언
edges = []
result = 0

# 모든 간선에 대한 정보를 받기
for i in range(m):
    a,b,cost = map(int, input().split())
    # a 노드에서 b 노드로 가는 비용이 cost라는 의미
    edges.append((cost, a, b))

# 간선을 비용 순으로 정렬
edges.sort()
# 최소 신장 트리에 포함되는 간선 중에서 가장 비용이 큰 간선
last = 0

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost

print(result-last)