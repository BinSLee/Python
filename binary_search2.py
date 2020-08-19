# 반복을 통한 이진탐색 구현 소스코드
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        # target 찾은 경우 mid값 반환
        if array[mid] == target:
            return mid
        # target이 중간점보다 큰 경우 오른쪽 탐색을 위해 start를 mid+1로 설정
        elif array[mid] < target:
            start = mid + 1
        # target이 중간점보다 작은 경우 왼쪽 탐색을 위해 end를 mid-1로 설정
        else:
            end = mid - 1
    return None

# N(원소의 개수)과 target 입력받기
n, target = list(map(int, input().split()))
# 전체 원소 입력받기
array = list(map(int, input().split()))

# 이진탐색 수행 결과 출력
result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result+1)