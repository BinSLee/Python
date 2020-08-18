array = [5,2,7,1,3,9,0,4]

def quick_sort(array):
    # 배열의 원소가 1개 이하인 경우 종료
    if len(array) <= 1:
        return array
    # 피벗은 첫번째 원소
    pivot = array[0]
    # 피벗을 제외한 나머지 원소들
    tail = array[1:]
    
    # 피벗 기준 작은값 왼쪽 분할
    left_side = [x for x in tail if x <= pivot]
    # 피벗 기준 큰값 오른쪽 분할
    right_side = [x for x in tail if x > pivot]
    
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬하고 전체 리스트 리턴
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)
    
print(quick_sort(array))
