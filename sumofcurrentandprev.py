#Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.

num = int(input())

print('Printing current and previous number sum in a range(',num,')') 

temp = 0
for i in range(num):
    print('Current Number', i ,'Previous Number', temp, 'Sum:', i + temp)
    temp = i

#Another Method
print("Printing current and previous number and their sum in a range(10)")
prev_num = 0


#loop from 1 to 10
for i in range(1,11):
    sum = prev_num + i 
    print('Current Number', i, 'Previous Number', prev_num, 'Sum:', sum)
    
    #set prev num to current number
    prev_num = i 

'''
Printing current and previous number and their sum in a range(10)
Current Number 1 Previous Number 0 Sum: 1
Current Number 2 Previous Number 1 Sum: 3
Current Number 3 Previous Number 2 Sum: 5
Current Number 4 Previous Number 3 Sum: 7
Current Number 5 Previous Number 4 Sum: 9
Current Number 6 Previous Number 5 Sum: 11
Current Number 7 Previous Number 6 Sum: 13
Current Number 8 Previous Number 7 Sum: 15
Current Number 9 Previous Number 8 Sum: 17
Current Number 10 Previous Number 9 Sum: 19
'''
