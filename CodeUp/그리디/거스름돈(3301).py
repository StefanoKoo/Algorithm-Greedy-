money = int(input())
count = 0

money_list = [50000,10000,5000,1000,500,100,50,10]

for coin in money_list:
  count += money//coin
  money = money%coin

print(count)
