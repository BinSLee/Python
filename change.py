# 거슬러 줘야할 돈 n 입력받기
n = int(input())

# 거스름돈 동전 종류 및 개수반환 변수 선언
coins = [500,100,50,10]
count = 0

# 거슬러줄 코인개수 계산
for coin in coins:
    count += n//coin
    n %= coin
        
print(count)