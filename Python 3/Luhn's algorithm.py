credit_card_number = list(input("Enter your credit card number: "))
first_digit = []  ## numbers in the position of 0,2,4,6...
second_digit = [] ## numbers in the position of 1,3,5,...
for i in range(0, 15):
    if i % 2 != 0:
        # print(2 * credit_card_number[i])
        second_digit.append(credit_card_number[i])
    else:
        first_digit.append(credit_card_number[i])

second_digit = [int(i) * 2 for i in second_digit]

sum1 = 0
for i in second_digit:
    if i < 10:
        sum1 = sum1 + i % 10
    else:
        sum1 = sum1 + int(1) + i % 10
sum2 = 0
for i in first_digit:
    sum2 = sum2 + int(i)

sum = sum1 + sum2
print(f'Here the sum is = {sum}')
if sum%10 ==0:
    print("Valid Credit Card Number")
else:
    print("Not Valid")
