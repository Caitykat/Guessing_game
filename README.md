# Guessing_game
My guessing game! I made this game because I was curious what it would look like to make a computer guess a number without using AI (spoiler alert, its a lot of if statements). My code runs a complete guessing game where you the player can guess, or you can have the computer guess your number!

## AI use
I purposefully wanted no AI to be involved in the making of my code. The only AI I used during the process was chatgpt when I got super stuck on debugging.

## Dependencies (if running code directly)
numpy
guizero
pillow

## Start screen
Only shown once in the game, press the start button to get started with the actual game

## Game mode select screen
Two buttons, one for computer guesses and one for Player guesses. Self explanitory, in the computer guesses the computer guesses your number, in player guesses you guess the computers randomly generated number.

## Computer guesses
This is a program I built based on enitrely if statments. I drew out the flow chart of how the numbers should be called for the most logical deduction (for example, guessing 50 first to cut the 100 pool in half) and from there typed out every if statement. The computer can accurately guess any number 0-100.

Higher button - Press when your number is higher than the number displayed

Lower button - Press when your number is lower than the number displayed

Correct button - Press when the number is correct

## Computer win screen
This is the screen that displays after the computer guesses the correct number.

It displays:
What your number was
How many guesses it took
A button that when pressed will take you back to game mode select

## Player guesses 
This program has the player guess the computers number and see how many tries it takes them. 

TextBox - This is where you enter your guess. Please type in a number. If you do not type in a number 0-100, nothing will happen.

Submit - Press this button to submit your guess. If incorrect, the computer will say higher or lower. If correct, it will take you to a screen that says you won and how many tries it took.

## Player win screen
This is the screen that displays after the player guesses the correct number.

It displays:
How many guesses it took
A button that when pressed will take you back to game mode select

# Thank you so much for playing my game! I hope you enjoy!
