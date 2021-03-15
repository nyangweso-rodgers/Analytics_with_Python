# While Loops

'''
The statement inside a while loop is repeatedly executed as long as the condition holds. 
Once it evaluates to False, the next section of the code is executed. 
The break statement is used to end a while loop prematurely.
'''

# printing even values using a while loop
## Printing Even Numbers between 0 and 20 inclusive
x = 0
while x<=20:
    print(x)
    x += 2

# Using the True key word and the break statement    
i = 5
while True:
    print(i)
    i -= 1
    if i <= 2:
        break

# Continue
## Unlike break, continue jumps back to the top of the loop, rather than stopping it.
i = 0
while True:
    i += 1
    if i == 2:
        print(".")
        continue
    if i == 5:
        print('Breaking!')
        break
        print(i)
print('Finished!')

list = [i for i in range(11)]

# summing numbers in a list using a for loop
list = [1, 2, 3]
list_sum = 0
for i in list:
    list_sum += i
print(list_sum) # 6


# summing numbers in a list with a while loop
list = [1, 2, 3]
sum_list = 0
k = 0
while k < len(list):
    sum_list += k
    k += 1
print(sum_list) # 3

    
    
# Challenge Question 1
## what is the last number printed after executing the following code?
a = 0
while a <= 10:
    a = a + 2
    if (a % 4 == 0):
        print(a) # 12
        
i = 0
while 1 == 1:
    print(i)
    i += 1
    if i >=5:
        print('go')
        break   

# Challenge Question 2
## find the sum of positive numbers in the above list using a while loop
given_list = [5, 4, 4, 3, 1, -2, -3, -5]
total3 = 0
i = 0
while given_list[i] > 0:
    total3 += given_list[i]
    i += 1
print(total3)     # 17

## find the sum of negative numbers
given_list3 = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7]
total = 0
for i in given_list3:
    if i < 0:
        total += i
print(total)