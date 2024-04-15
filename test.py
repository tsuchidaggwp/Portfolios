number = 50

sum = 0
double_sum = 0

for i in range(number+1):
    sum += i
    double_sum += i*i

   
print(f'1から{number}までの和は{sum}です。')
print(f'1から{number}までの二乗和は{double_sum}です。')