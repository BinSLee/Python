# 숫자로 이루어진 문자열 S 입력받기
s = str(input())
# 결과를 저장할 변수 문자열 S의 첫번째 값으로 초기화
result = int(s[0])

# 가장 큰 수를 반환하는 연산 수행
for i in range(len(s)-1):
    # 해당 자리의 숫자가 0 또는 1일 경우 + 연산을 하는 것이 더 큰 수를 만든다
    if s[i] == '0' or s[i] == '1':
        result += int(s[i+1])
    # 0과 1 이외의 숫자의 경우 x 연산을 하는 것이 더 큰 수를 만든다
    else:
        result *= int(s[i+1])

# 결과 출력
print(result)