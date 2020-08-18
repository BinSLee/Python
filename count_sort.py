# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [4,5,7,9,3,4,2,6,7,9,3]
# 모든 범위를 포함하는 리스트 선언(0으로 초기화)
count = [0]*(max(array)+1)

# 각 데이터에 해당하는 인덱스 값 증가
for i in range(len(array)):
    count[array[i]] += 1

# 리스트에 기록된 정렬 정보 확인
for i in range(len(count)):
    for j in range(count[i]):
        print(i, end = ' ')