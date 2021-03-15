# Control Structure in Python

Algorithms require two important control structures: __iteration__ and __selection__.

For __iteration__, Python provides a standard __while__ statement and a very powerful __for__ statement. 
A __while__ statement repeats a body of code as long as a condition is true.

## For example:
```py
# here, the phrase "hello world!" is printed five times

counter = 1
while counter <=5:
    print('hello world!')
    counter += 1
```

Another __iterative__ structure, the __for__ statement, can be used in conjuction with many of the Python collections. The __for__ statement can be used to iterate over the members of a collection, so long as the collection is a sequence:

## For example:
```py
for item in [1, 4, 7, 9]:
    # The code assign the variable item to each successive value in the list [1, 4, 7, 9]. The body of the iteration is then executed.
    # Note: This works for any collection that is a sequence (list, tuples, strings)
    print(item)
```

A common use of the __for__ statement is to implement definite iteration over a range of values.
## For example:
```py
for item in range(5):
    print(item**2)
```

The other very useful version of this iteration structure is used to process each character of a string.
```py
word_list = ['cat', 'dog', 'rabbit']
letter_list = []
for word in word_list:
    for letter in word:
        letter_list.append(letter)
print(letter_list); # ['c', 'a', 't', 'd', 'o', 'g', 'r', 'a', 'b', 'b', 'i', 't']
# The above code fragment iterates over a list of strings and for each string process each character by appending it to a list. 
# The result is a list of all letters in all of the words:  
```

__Selection__ statements allow programmers to ask questions and then, based on the result, perform different actions.
```py
scores = [19, 89, 45, 23, 90, 27, 30]

for score in scores:
    if score >= 90:
        print('A')
    else:
        if score >= 80:
            print('B')
        else:
            if score >= 70:
                print('C')
            else:
                if score >= 60:
                    print('D')
                else:
                    print('F')
```
## Alternatively,
```py
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')
```

Python also has a single way selection construct, the __if__ statement. With this statement, if the condition is true, an action is performed. In the case where the condition is false, processing simply continues on to the next statement after the __if__ statement.

_For example:_ The following fragment will first check to see if the value of a variable _n_ is negative. If it is, then it's modified by the __absolute__ value function. Regardless, the next action is to compute the square root.

```py
import math
n = -9
if n < 0:
    n = abs(n)
print(math.sqrt(n))
```

There is an alternative method for creating a list that uses __iteration__ and __selection__ constructs known as __list comprehension__ - it allows you to easily create a list based on some processing or selection criteria.

_For example:_ creating a list of the first 10 perfect squares, we could use the __for__ statement

```py
# perfect squares
square_list = []
for x in range(1, 11):
    square_list.append(x*x)
print(square_list)
```

Using a list comprehension, we can do this in one step:
```py
square_list = [x*x for x in range(1, 11)]
print(square_list)
```

__Remark:__ The general synatx for a _list comprehension_ also allows a selection criteria be added so that only certain items are added:

### For example:
```py
# a sequence of odd numbers

square_list = [x*x for x in range(1, 11) if x%2 !=0]
print(square_list)
```

Any sequence that supports iteration can be used within a list comprehension to construct a new list:

### For example:
```py
[ch.upper() for ch in 'comprehension' if ch not in 'aeiou']
```