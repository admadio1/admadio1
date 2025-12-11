#greet user and ask to enter a number to be checked
print('Welcome to Fizz Buzz!')
print('Enter a number:')
number = int(input())

#check if number is divisible by 3 & 5, 3, and 5 to determine output
if (number % 3 == 0) and (number % 5 == 0):
    print('FizzBuzz!')
elif number % 3 == 0:
    print('Fizz!')
elif number % 5 == 0:
    print('Buzz!')
else:
    print(number)
