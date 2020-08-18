# N 입력받기
n = int(input())

# N명의 학생 정보 입력받아 리스트에 저장
array = []
for i in range(n):
    input_data = input().split()
    # 이름은 문자열 그대로, 성적은 정수로 받기
    array.append((input_data[0], int(input_data[1])))

# 람다식을 사용하여 key값을 기준으로 정렬(오름차순)
array = sorted(array, key=lambda student:student[1])

# 정렬된 결과 출력
for student in array:
    print(student[0], end = ' ')