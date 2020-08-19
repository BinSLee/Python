# N 입력받기
n = int(input())
# 가게에 있는 전체 부품 번호를 입력받아 집합(set) 자료형에 기록
array = set(map(int, input().split()))

# M 입력받기
m = int(input())
want = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in want:
    # 해당 부품이 존재한다면
    if i in array:
        print('yes', end=' ')
    # 해당 부품이 존재하지 않는다면
    else:
        print('no', end=' ')