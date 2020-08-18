n, k = map(int, input().split())

a = list(map(int, input().split())) # 첫 번째 배열 공백 두고 입력받기
b = list(map(int, input().split())) # 두 번째 배열 공백 두고 입력받기

a.sort()                # 첫 번째 배열 오름차순 정렬
b.sort(reverse=True)    # 두 번째 배열 내림차수 정렬

# K번 연산 수행
for i in range(k):
    if a[i]<b[i]:   # 첫 번째 배열의 최소값이 두 번째 배열의 최대값보다 작은 경우 바꿔치기
        a[i],b[i] = b[i],a[i]
    else:           # 그 외의 경우 반복문 탈출
        break

# 배열 a의 모든 원소값 합산 출력
print(sum(a))