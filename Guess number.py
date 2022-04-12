import random 

#Antoine Dupont: 1-3
print ('Hello welcome to the Number Game!')
name = input ('What is your name? ')
print ('Hey', name+', get ready to guess a number!')

#Raj Veera: 4-6, Antoine Dupont: 7-9
numGuessed = []
correctNum= random.randint(1,100)
numGuess = 1
guess = int(input('Please guess a number from 1-100: '))

while correctNum != guess:  
  numGuessed.append(guess)
  if correctNum > guess:
    print('The correct number is higher, try again!')    
    numGuess += 1
    guess = int(input('Please guess a number from 1-100: '))
  else: 
    print('The correct number is lower, try again!')
    numGuess += 1
    guess = int(input('Please guess a number from 1-100: '))
  if guess in numGuessed:
    guess = int(input('Please enter an number you have not already chosen: '))

print('Congrats! You guessed the correct number!')
print('It took you', numGuess , 'to find the correct number! Great work!')

  
    
    
