# Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

num1 = int(input('number1 = '))
num2 = int(input('number2 = '))

product = num1 * num2 
sum = num1 + num2

if product <= 1000:
    print('The result is',product)
else: 
    print('The result is', sum) 
    
    
# Another Method
def mul_or_sum(num1,num2):
    #calculate product of two number
    product = num1 * num2
    #check if product is less than 1000
    if product <= 1000:
        return product
    else:
    # if product is greater than 1000 calculate sum
        return num1 + num2

#first condition
result = mul_or_sum(20,30)
print("The result is", result)

#second condition
result = mul_or_sum(40,30)  
print("The result is", result)    



""" output : 
(base) shrutisidharthmandaokar@Shrutis-MacBook-Air Python Revision % python Multiplicationof2num.py
number1 : 20
number2 : 30
The result is 600
(base) shrutisidharthmandaokar@Shrutis-MacBook-Air Python Revision % python Multiplicationof2num.py
number1 = 40
number2 = 30
The result is 70

"""
