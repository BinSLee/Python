# N,M 입력받기
n,m = map(int, input().split())

# 연산횟수 저장 변수 선언 및 초기화
count = 0

while True:
    # n이 m으로 나눠지는 경우 수행
    if n % m == 0:
        n = n/m
    # 그 외의 경우 n-1 연산 수행
    else:
        n -= 1
    count += 1
    
    # n이 1에 도달했을때 반복문 중단
    if n == 1:
        break

# 결과 출력
print(count)