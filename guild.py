# 모험가 수 N 입력받기
n = int(input())

# 모험가의 공포도 입력받기
data = list(map(int, input().split()))
# 공포도 정렬
data.sort()

# 그룹의 수 , 그룹의 모험가 수 변수 선언
result = 0
count = 0

# 그룹 나누기
for i in data:
    # 그룹 구성원 수 증가
    count += 1
    # 공포도 이상의 수로 그룹이 구성되어 있다면
    if i <= count:
        # 그룹 수 증가 및 참여한 그룹원 수 초기화
        result += 1
        count = 0

# 결과 출력
print(result)