# 떡의 개수(N)와 요청한 떡의 길이(M)을 입력받기
n, m = map(int, input().split())
# 각 떡의 개별 높이 정보를 입력받기
array = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

# 이진 탐색 수행(반복)
result = 0
while (start <= end):
    total = 0
    mid = (start + end) // 2
    for i in array:
        # 잘랐을 때 떡의 양 계산
        if i > mid:
            total += i - mid
    # 자른 떡의 양이 목표에 모자를 때
    if total < m:
        # 왼쪽 탐색
        end = mid - 1
    # 자른 떡의 양이 목표 이상일 경우
    else:
        # 높이의 최대값이므로 여기에서 result 기록
        result = mid
        # 오른쪽 탐색
        start = mid + 1

# 결과 출력
print(result)