"""Bulls and Cows"""
import random

print('Welcome to the Bulls and Cows game'
      '\nB stands for numbers in correct place'
      '\nC stands for numbers in wrong place\n')
random_number = random.randint(11, 98).__str__()
first_random = int(random_number[0])
second_random = int(random_number[1])
if first_random == second_random:
    second_random += 1
    print('Your random number was ', random_number,
          ' But I know you do not want numbers like this,and I increment last number,and your number became ',
          first_random, second_random)
while True:
    guessing_number = input('Please enter your guess: ')
    int_guessing = int(guessing_number)
    if int_guessing < 10 or int_guessing > 100:
        print('You need to enter two level number')
        continue
    first_input = int(guessing_number[0])
    second_input = int(guessing_number[1])
    if first_input == first_random and second_input == second_random:
        print('Congratulations!')
        break
    elif first_input == first_random or second_input == second_random:
        print('1B,0C')
    elif first_input == second_random and second_input == first_random:
        print('0B,2C')
    elif first_input == second_random or second_input == first_random:
        print('0B,1C')
    else:
        print('0B,0C')
