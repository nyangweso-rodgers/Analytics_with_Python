fruits = ['apple', 'banana', 'mango']

for i in fruits:
    print(i)

for i in range(3):
    print(fruits[i])

for i in range(len(fruits)):
    print(fruits[i])
    
# print each element twice:
fruits = ['apple', 'banana', 'mango']
for i in range(len(fruits)):
    for j in range(i + 1):
        # i = 0 -> j = 0
        # i = 1 -> j = 0, 1
        # i = 2 -> j = 0, 1, 2
        print(fruits[i])    
        
        
# Challenge Question 1
## compute the sum of all multiples of 3 and 5 that are less than 5
print(list(range(1, 100)))

# SOLUTION

total = 0
for i in range(1, 100):
    if i % 3 == 0:
        total += i
    elif i % 5 == 0:
        total += i
        
print(total) # 2318

# alternatively:
total = 0
for i in range(1, 100):
    if i % 3 == 0 or i % 5 == 0:
        total += i
print(total) # 2318


# Challenge Question 2
## find the sum of the negative numbers
given_list = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7]
total = 0
j = len(given_list) - 1
while given_list[j] < 0:
    total += given_list[j]
    j -= 1
print(total) # -17