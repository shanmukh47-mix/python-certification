# write a function which takes a number as input and finds out weither it is even or odd.

# definition of the function 'odd_even' which takes 'n' as parameter and returns nothing
def odd_even(n):
    if n % 2 == 0:
        print('Even') 
    else:
        print('odd')

# function call with argument 45
odd_even(45)
# function call with argument 78
odd_even(78)

# def <name_of_the_function>(<parameters>):
#     body of the function

# definition of the function 'is_even' which takes 'n' as parameter and returns true or false 
def is_even(m):
    if m % 2 == 0:
        return True
    else:
        return False

# function call with argument 'number'
number = int(input("enter the number to be checked"))
resp = is_even(number)
if resp:
    print(f'{number} is even')
else:
    print(f'{number} is odd')
