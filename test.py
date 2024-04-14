number = input("Please enter an integer: ")

number = int(number)
sum = 0

for i in range(number):
    sum += i

   
print(f'1から{number}までの和は{sum}です。')