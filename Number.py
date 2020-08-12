# N, M, K를 공백으로 구분하여 입력받기
n,m,k = map(int, input().split())

# 계산할 데이터 리스트에 저장
datas = list(map(int, input().split()))
# 오름차순으로 정렬
datas.sort()

# 결과값 저장변수 선언 및 초기화
result = 0

while True:
    # 가장 큰 수 k번 만큼 더하기
    for i in range(k):
        if m == 0:
            break
        result += datas[-1]
        m -= 1
    if m == 0:
        break
    # 두 번째로 큰 수 1번 더하기
    result += datas[-2]
    m -= 1
    
# 결과값 출력
print(result)