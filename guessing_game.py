#imports
import guizero
from guizero import App, Text, PushButton, Box

#variables 
#how many guesses it took to guess the correct number
guess_number = 1

#App setup
my_app = App(title="Guessing Game", width=600, height=800,
              layout = "grid", bg = "pink")

#Functions!!!!!!!

#what happens when you click higher
def higher_click():
    #variable that counts how many guesses it took
    global guess_number
    #if current guess is 0, increases guess to 12
    if guess_display.value == "0":
        guess_number += 1
        guess_display.value = 12
    #if current guess is 3, increases guess to 4
    elif guess_display.value == "3":
        guess_number += 1
        guess_display.value = 4
    #if current guess is 4, increases guess to 5
    elif guess_display.value == "4":
        guess_number += 1
        guess_display.value = 5
    #if current guess is 6, increases guess to 9
    elif guess_display.value == "6":
        guess_number += 1
        guess_display.value = 9
    #if current guess is 9, increases guess to 10
    elif guess_display.value == "9":
        guess_number += 1
        guess_display.value = 10
    #if current guess is 10, increases guess to 11
    elif guess_display.value == "10":
        guess_number += 1
        guess_display.value = 11
    #if current guess is 12, increases guess to 18
    elif guess_display.value == "12":
        guess_number += 1
        guess_display.value = 18
    #if current guess is 15, increases guess to 16
    elif guess_display.value == "15":
        guess_number += 1
        guess_display.value = 16
    #if current guess is 16, increases guess to 17
    elif guess_display.value == "16":
        guess_number += 1
        guess_display.value = 17
    #if current guess is 18, increases guess to 21
    elif guess_display.value == "18":
        guess_number += 1
        guess_display.value = 21
    #if current guess is 21, increases guess to 23
    elif guess_display.value == "21":
        guess_number += 1
        guess_display.value = 23
    #if current guess is 23, increases guess to 24
    elif guess_display.value == "23":
        guess_number += 1
        guess_display.value = 24
    #if current guess is 25, increases guess to 37 
    elif guess_display.value == "25":
        guess_number += 1
        guess_display.value = 37
    #if current guess is 27, increases guess to 28
    elif guess_display.value == "27":
        guess_number += 1
        guess_display.value = 28
    #if current guess is 29, increases guess to 30
    elif guess_display.value == "29":
        guess_number += 1
        guess_display.value = 30
    #if current guess is 31, increases guess to 34
    elif guess_display.value == "31":
        guess_number += 1
        guess_display.value = 34
    #if current guess is 34, increases guess to 35
    elif guess_display.value == "34":
        guess_number += 1
        guess_display.value = 35
    #if current guess is 35, increases guess to 36
    elif guess_display.value == "35":
        guess_number += 1
        guess_display.value = 36
    #if current guess is 37, increases guess to 43
    elif guess_display.value == "37":
        guess_number += 1
        guess_display.value = 43
    #if current guess is 40, increases guess to 41
    elif guess_display.value == "40":
        guess_number += 1
        guess_display.value = 41
    #if current guess is 41, increases guess to 42
    elif guess_display.value == "41":
        guess_number += 1
        guess_display.value = 42
    #if current guess is 43, increases guess to 46
    elif guess_display.value == "43":
        guess_number += 1
        guess_display.value = 46
    #if current guess is 46, increases guess to 48
    elif guess_display.value == "46":
        guess_number += 1
        guess_display.value = 48
    #if current guess is 48, increases guess to 49
    elif guess_display.value == "48":
        guess_number += 1
        guess_display.value = 49
    #if current guess is 50, increases guess to 75
    elif guess_display.value == "50":
        guess_number += 1
        guess_display.value = 75
    #if current guess is 53, increases guess to 54
    elif guess_display.value == "53":
        guess_number += 1
        guess_display.value = 54
    #if current guess is 54, increases guess to 55
    elif guess_display.value == "54":
        guess_number += 1
        guess_display.value = 55
    #if current guess is 56, increases guess to 59
    elif guess_display.value == "56":
        guess_number += 1
        guess_display.value = 59
    #if current guess is 59, increases guess to 60
    elif guess_display.value == "59":
        guess_number += 1
        guess_display.value = 60
    #if current guess is 60, increases guess to 61
    elif guess_display.value == "60":
        guess_number += 1
        guess_display.value = 61
    #if current guess is 62, increases guess to 68
    elif guess_display.value == "62":
        guess_number += 1
        guess_display.value = 68
    #if current guess is 65, increases guess to 67
    elif guess_display.value == "65":
        guess_number += 1
        guess_display.value = 67
    #if current guess is 68, increases guess to 71
    elif guess_display.value == "68":
        guess_number += 1
        guess_display.value = 71
    #if current guess is 71, increases guess to 73
    elif guess_display.value == "71":
        guess_number += 1
        guess_display.value = 73
    #if current guess is 73, increases guess to 74
    elif guess_display.value == "73":
        guess_number += 1
        guess_display.value = 74
    #if current guess is 75, increases guess to 100
    elif guess_display.value == "75":
        guess_number += 1
        guess_display.value = 100
    #if current guess is 78, increases guess to 79
    elif guess_display.value == "78":
        guess_number += 1
        guess_display.value = 79
    #if current guess is 79, increases guess to 80
    elif guess_display.value == "79":
        guess_number += 1
        guess_display.value = 80
    #if current guess is 81, increases guess to 84
    elif guess_display.value == "81":
        guess_number += 1
        guess_display.value = 84
    #if current guess is 84, increases guess to 85
    elif guess_display.value == "84":
        guess_number += 1
        guess_display.value = 85
    #if current guess is 85, increases guess to 86
    elif guess_display.value == "85":
        guess_number += 1
        guess_display.value = 86
    #if current guess is 87, increases guess to 93
    elif guess_display.value == "87":
        guess_number += 1
        guess_display.value = 93
    #if current guess is 90, increases guess to 91
    elif guess_display.value == "90":
        guess_number += 1
        guess_display.value = 91
    #if current guess is 91, increases guess to 92
    elif guess_display.value == "91":
        guess_number += 1
        guess_display.value = 92
    #if current guess is 93, increases guess to 96
    elif guess_display.value == "93":
        guess_number += 1
        guess_display.value = 96
    #if current guess is 96, increases guess to 98
    elif guess_display.value == "96":
        guess_number += 1
        guess_display.value = 98
    #if current guess is 98, increases guess to 99
    elif guess_display.value == "98":
        guess_number += 1
        guess_display.value = 99

#what happens when you click lower
def lower_click():
    #variable that counts how many guesses it took
    global guess_number
    #if current guess is 2, lowers guess to 1
    if guess_display.value == "2":
        guess_number += 1
        guess_display.value = 1
    #if current guess is 3, lowers guess to 2
    elif guess_display.value == "3":
        guess_number += 1
        guess_display.value = 2
    #if current guess is 6, lowers guess to 3
    elif guess_display.value == "6":
        guess_number += 1
        guess_display.value = 3
    #if current guess is 8, lowers guess to 7
    elif guess_display.value == "8":
        guess_number += 1
        guess_display.value = 7
    #if current guess is 9, lowers guess to 8
    elif guess_display.value == "9":
        guess_number += 1
        guess_display.value = 8
    #if current guess is 12, lowers guess to 6
    elif guess_display.value == "12":
        guess_number += 1
        guess_display.value = 6
    #if current guess is 14, lowers guess to 13
    elif guess_display.value == "14":
        guess_number += 1
        guess_display.value = 13
    #if current guess is 15, lowers guess to 14
    elif guess_display.value == "15":
        guess_number += 1
        guess_display.value = 14
    #if current guess is 18, lowers guess to 15
    elif guess_display.value == "18":
        guess_number += 1
        guess_display.value = 15
    #if current guess is 20, lowers guess to 19
    elif guess_display.value == "20":
        guess_number += 1
        guess_display.value = 19
    #if current guess is 21, lowers guess to 20
    elif guess_display.value == "21":
        guess_number += 1
        guess_display.value = 20
    #if current guess is 23, lowers guess to 22
    elif guess_display.value == "23":
        guess_number += 1
        guess_display.value = 22
    #if current guess is 25, lowers guess to 0
    elif guess_display.value == "25":
        guess_number += 1
        guess_display.value = 0
    #if current guess is 27, lowers guess to 26
    elif guess_display.value == "27":
        guess_number += 1
        guess_display.value = 26
    #if current guess is 29, lowers guess to 27
    elif guess_display.value == "29":
        guess_number += 1
        guess_display.value = 27
    #if current guess is 31, lowers guess to 29
    elif guess_display.value == "31":
        guess_number += 1
        guess_display.value = 29
    #if current guess is 33, lowers guess to 32
    elif guess_display.value == "33":
        guess_number += 1
        guess_display.value = 32
    #if current guess is 34, lowers guess to 33
    elif guess_display.value == "34":
        guess_number += 1
        guess_display.value = 33
    #if current guess is 37, lowers guess to 31
    elif guess_display.value == "37":
        guess_number += 1
        guess_display.value = 31
    #if current guess is 39, lowers guess to 38
    elif guess_display.value == "39":
        guess_number += 1
        guess_display.value = 38
    #if current guess is 40, lowers guess to 39
    elif guess_display.value == "40":
        guess_number += 1
        guess_display.value = 39
    #if current guess is 43, lowers guess to 40
    elif guess_display.value == "43":
        guess_number += 1
        guess_display.value = 40
    #if current guess is 45, lowers guess to 44
    elif guess_display.value == "45":
        guess_number += 1
        guess_display.value = 44
    #if current guess is 46, lowers guess to 45
    elif guess_display.value == "46":
        guess_number += 1
        guess_display.value = 45
    #if current guess is 48, lowers guess to 47
    elif guess_display.value == "48":
        guess_number += 1
        guess_display.value = 47
    #if current guess is 50, lowers guess to 25
    elif guess_display.value == "50":
        guess_number += 1
        guess_display.value = 25
    #if current guess is 52, lowers guess to 51
    elif guess_display.value == "52":
        guess_number += 1
        guess_display.value = 51
    #if current guess is 53, lowers guess to 52
    elif guess_display.value == "53":
        guess_number += 1
        guess_display.value = 52
    #if current guess is 56, lowers guess to 53
    elif guess_display.value == "56":
        guess_number += 1
        guess_display.value = 53
    #if current guess is 58, lowers guess to 57
    elif guess_display.value == "58":
        guess_number += 1
        guess_display.value = 57
    #if current guess is 59, lowers guess to 58
    elif guess_display.value == "59":
        guess_number += 1
        guess_display.value = 58
    #if current guess is 62, lowers guess to 56
    elif guess_display.value == "62":
        guess_number += 1
        guess_display.value = 56
    #if current guess is 64, lowers guess to 63
    elif guess_display.value == "64":
        guess_number += 1
        guess_display.value = 63
    #if current guess is 65, lowers guess to 64
    elif guess_display.value == "65":
        guess_number += 1
        guess_display.value = 64
    #if current guess is 67, lowers guess to 66
    elif guess_display.value == "67":
        guess_number += 1
        guess_display.value = 66
    #if current guess is 68, lowers guess to 65
    elif guess_display.value == "68":
        guess_number += 1
        guess_display.value = 65
    #if current guess is 70, lowers guess to 69
    elif guess_display.value == "70":
        guess_number += 1
        guess_display.value = 69
    #if current guess is 71, lowers guess to 70
    elif guess_display.value == "71":
        guess_number += 1
        guess_display.value = 70
    #if current guess is 73, lowers guess to 72
    elif guess_display.value == "73":
        guess_number += 1
        guess_display.value = 72
    #if current guess is 75, lowers guess to 62
    elif guess_display.value == "75":
        guess_number += 1
        guess_display.value = 62
    #if current guess is 77, lowers guess to 76
    elif guess_display.value == "77":
        guess_number += 1
        guess_display.value = 76
    #if current guess is 78, lowers guess to 77
    elif guess_display.value == "78":
        guess_number += 1
        guess_display.value = 77
    #if current guess is 81, lowers guess to 78
    elif guess_display.value == "81":
        guess_number += 1
        guess_display.value = 78
    #if current guess is 83, lowers guess to 82
    elif guess_display.value == "83":
        guess_number += 1
        guess_display.value = 82
    #if current guess is 84, lowers guess to 83
    elif guess_display.value == "84":
        guess_number += 1
        guess_display.value = 83
    #if current guess is 87, lowers guess to 81
    elif guess_display.value == "87":
        guess_number += 1
        guess_display.value = 81
    #if current guess is 89, lowers guess to 88
    elif guess_display.value == "89":
        guess_number += 1
        guess_display.value = 88
    #if current guess is 90, lowers guess to 89
    elif guess_display.value == "90":
        guess_number += 1
        guess_display.value = 89
    #if current guess is 93, lowers guess to 90
    elif guess_display.value == "93":
        guess_number += 1
        guess_display.value = 90
    #if current guess is 95, lowers guess to 94
    elif guess_display.value == "95":
        guess_number += 1
        guess_display.value = 94
    #if current guess is 96, lowers guess to 95
    elif guess_display.value == "96":
        guess_number += 1
        guess_display.value = 95
    #if current guess is 98, lowers guess to 97
    elif guess_display.value == "98":
        guess_number += 1
        guess_display.value = 97
    #if current guess is 100, lowers guess to 87
    elif guess_display.value == "100":
        guess_number += 1
        guess_display.value = 87

def correct_click():
    #sets screen to non visible
    title.visible = False
    sub_heading.visible = False
    my_guess.visible = False
    guess_display.visible = False
    button_box.visible = False
    higher_button.visible = False
    lower_button.visible = False
    correct_button.visible= False
    #sets win screen to visible
    win_text.visible = True
    number.visible = True
    #updates to display most recent data
    number.value = guess_display.value 
    it_took.visible = True
    guess.visible = True
    #updates to display most recent data
    guess.value = guess_number 
    guesses_it_took.visible = True

#centers the text
center = Box(my_app, width = 100, height = 50, grid = [0,0])

#the title
title = Text(my_app, text= "Guessing Game",
             size = 50, color = "red", grid = [1,0])

#sub heading
sub_heading = Text(my_app,text = "What number are you thinking?",
                   grid = [1,1], size = 25, color = "red")

#my guess text
my_guess = Text(my_app, text = "My guess is...", grid = [1,2],
                size = 50, color = "red")

#guess display
guess_display = Text(my_app, text = 50, grid = [1,3],
                     size = 100, color = "red")

#box for the buttons
button_box = Box(my_app, grid = [1,4], width = 300, height = 300)

#Button one, higher
higher_button = PushButton(button_box,grid = [0,0], width = 10, height = 5,
                           text = "Higher", command = higher_click)

#Button two, lower
lower_button = PushButton(button_box,grid = [0,1], width = 10, height = 5,
                           text = "Lower", command = lower_click)

#button three, correct
correct_button = PushButton(button_box, grid = [0,2], width = 10,
                            height = 5, text = "Correct", command = correct_click)

#text (only visible after guess is correct)
win_text = Text(my_app, text = "Your number was", grid = [1,0],
                size = 50, color = "red", visible = False)

#displays what their number was
number = Text(my_app, text = guess_display.value, grid = [1,1],
              size = 100, color = "red", visible = False)

#text on win #2
it_took = Text(my_app, text = "It took me", grid = [1,2],
               size = 50, color = "red", visible = False)

#number of guesses it took to get number
guess = Text(my_app, text = guess_number, grid = [1,3],
             size = 100, color = "red", visible = False)

#final text
guesses_it_took = Text(my_app, text = "guesses to guess your number", grid = [1,4],
                       size = 25, color = "red", visible = False)


#runs app!
my_app.display()