# 볼링공의 개수 N, 공의 최대 무게 M 입력받기
n,m = map(int, input().split())
# 볼링공의 무게를 리스트에 저장
balls = list(map(int, input().split()))
# 가능한 경우의 수를 저장할 변수 0으로 초기화
count = 0

# 가능한 경우의 수 계산
for i in range(n-1):
    # i번째와 i+1번째 공의 무게를 비교하는 연산
    for j in range(i+1, n):
        # 인접한 공의 무게가 서로 다르다면 count 1 증가
        if balls[i] != balls[j]:
            count += 1

# 결과 출력        
print(count)