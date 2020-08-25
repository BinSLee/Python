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
    
# 노드의 개수 V와 간선의 개수 E 입력받기
v,e = map(int, input().split())
# 부모 테이블 초기화
parent = [0]*(v+1)

# 부모 테이블 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# 사이클 여부 확인하기 위한 변수선언
Cycle = False

# 사이클 발생 여부 조사
for i in range(e):
    a,b = map(int, input().split())
    # 사이클이 발생한다면 Cycle 변수 True로 변환
    if find_parent(parent, a) == find_parent(parent, b):
        Cycle = True
        break
    # 사이클이 없다면 집합 합치기
    else:
        union_parent(parent, a, b)

# 결과 출력
if Cycle:
    print('사이클이 발생했습니다')
else:
    print('사이클이 없습니다.')