# 0과 1로 이루어진 문자열 S 입력받기
s = input()
# 0으로 바꾼 연산횟수 저장 변수
count0 = 0
# 1으로 바꾼 연산횟수 저장 변수
count1 = 0

# 문자열 S의 첫번째 값에 대한 초기화
if s[0] == '0':
    count1 += 1
else:
    count0 += 1

# 두번째 문자부터 끝까지 탐색
for i in range(len(s)-1):
    # 인접한 문자가 서로 같지 않을 경우
    if s[i] != s[i+1]:
        # 다음 문자가 0인 경우 1로 바꾸는 연산 수행
        if s[i+1] == '0':
            count1 += 1
        # 다음 문자가 1인 경우 0으로 바꾸는 연산 수행
        else:
            count0 += 1

# 두 연산 중 최소값 출력
print(min(count0,count1))