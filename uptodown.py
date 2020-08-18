# N 입력받기
n = int(input())

# N개의 정수를 입력받아 리스트에 저장
array = []
for i in range(n):
    array.append(int(input()))
# 입력받은 리스트 내림차순으로 정렬
array.sort(reverse=True)

# 정렬된 결과 출력
for i in range(len(array)):
    print(array[i], end = ' ')