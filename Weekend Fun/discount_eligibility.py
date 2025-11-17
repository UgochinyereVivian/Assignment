total_bill = float(input('Hey Odili😋️, input your total bill: '))
is_member = input('Hey Odili, are you a member of cohort 28 (answer Yes or No): ')


if total_bill >= 1000 and is_member == "yes":
    print('you are eligible for a 10% discount, your bill now: $', total_bill * 0.10)

if total_bill >= 1000 and is_member == "no":
    print('you are eligible for a 5% discount, your bill now is: $', total_bill * 0.5)

else:
    print('you are not eligible for a discount and your total bill is: $', total_bill)

#if is_member != 'yes' and is_member != 'NO':
    #print ('invalid response, try again')
