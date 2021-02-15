## Link : https://codeup.kr/problem.php?id=3321

num_toping = int(input())
price_dough, price_toping = map(int,input().split(' '))
cal_dough = int(input())
cal_topings = []

for _ in range(num_toping):
  cal_topings.append(int(input()))

total = 0
price = 0
calory = 0

cal_topings.sort(reverse=True)

for cal_toping in cal_topings:
  price += price_toping
  calory += cal_toping

  temp = (cal_dough + calory)/(price_dough+price)
  
  if temp > total:
    total = temp
  else:
    break

print(int(total))
