# 특정 원소가 속한 집합 찾기
def find_team(team, x):
    if team[x] != x:
        team[x] = find_team(team, team[x])
    return team[x]

# 두 원소가 속한 집합 합치기
def union_team(team, a, b):
    a = find_team(team, a)
    b = find_team(team, b)
    
    if a < b:
        team[b] = a
    else:
        team[a] = b

n,m = map(int, input().split())
# 부모 테이블 초기화
team = [0]*(n+1)

# 자기 자신으로 부모 테이블 초기화
for i in range(0, n+1):
    team[i] = i

# 각 연산을 하나씩 확인
for i in range(m):
    cal, a, b = map(int, input().split())
    # 합집합 연산인 경우
    if cal == 0:
        union_team(team, a, b)
    # find 연산인 경우
    elif cal == 1:
        if find_team(team, a) == find_team(team, b):
            print('Yes')
        else:
            print('No')