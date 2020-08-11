# 정수 N 입력받기
n = int(input())
# 결과 저장할 변수 선언
count = 0
# 00시 00분 00초 ~ N시 59분 59초 사이에 숫자 3이 있는 시각을 계산하기 위한 3중 반복문
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            # 시각을 str로 붙여서 검사 진행
            if '3' in str(i)+str(j)+str(k):
                count += 1
                
print(count)