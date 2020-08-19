# 이진 탐색 구현 소스코드(반복)
def search(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        # 찾은 경우 True 반환
        if array[mid] == target:
            return True
        # target이 중간점보다 큰 경우 오른쪽 탐색
        elif array[mid] < target:
            start = mid + 1
        # target이 중간점보다 작은 경우 왼쪽 탐색
        else:
            end = mid - 1
    return False

# N 입력받기
n = int(input())
# N개의 리스트 입력받기
array = list(map(int, input().split()))
# 이진 탐색을 위한 정렬
array.sort()

# 손님이 원하는 M 입력받기
m = int(input())
# M개의 리스트 입력받기
want = list(map(int, input().split()))

# 손님이 원하는 리스트 내에서 이진탐색 수행
for i in want:
    result = search(array, i, 0, n-1)
    if result == True:
        print('yes', end=' ')
    else:
        print('no', end=' ')