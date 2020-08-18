# 순차 탐색 소스코드 구현
def sequential_search(n, target, array):
    # 각 원소를 하나씩 확인하며
    for i in range(n):
        if array[i] == target:  # 현재 원소가 찾는 값이라면
            return i + 1        # 인덱스 + 1 값 반환 (시작 인덱스가 0이기 때문)

print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")
input_data = input().split()
n = int(input_data[0])  # 원소 개수
target = input_data[1]  # 찾는 문자열

print("앞서 적은 원소의 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
array = input().split()

# 순차 탐색 결과 출력
print(sequential_search(n,target,array))