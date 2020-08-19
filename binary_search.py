# 재귀적으로 구현한 이진탐색 소스코드
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end) // 2
    # target 찾은 경우 중간점 반환
    if array[mid] == target:
        return mid
    # target이 중간점보다 큰 경우 오른쪽 탐색
    if array[mid] < target:
        return binary_search(array, target, mid+1, end)
    # target이 중간점보다 작은 경우 왼쪽 탐색
    else:
        return binary_search(array, target, start, mid-1)

# N(원소의 개수)과 target(찾고자 하는 문자열) 입력받기        
n, target = list(map(int, input().split()))
# 전체 원소 입력받기
array = list(map(int, input().split()))

# 이진탐색 결과 출력
result = binary_search(array, target, 0, n-1)
if result == None:
    print("찾는 문자열이 존재하지 않습니다.")
else:
    print(result+1)
