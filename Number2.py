n,m,k = map(int, input().split())

datas = list(map(int,input().split()))
datas.sort()

first = datas[n-1]
second = datas[n-2]

# 큰 수 더하는 횟수 세기
count = (m//(k+1))*k
count += m%(k+1)

result = 0
result += count*first # 큰 수 더하기
result += (m-count)*second # 두 번째 큰 수 더하기

print(result)
