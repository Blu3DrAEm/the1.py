# The Matrix
# Josh Anderson

import time
import board
import busio
import adafruit_character_lcd.character_lcd_rgb_i2c as character_lcd

# Initialize LCD and Start Game
i2c = busio.I2C(board.SCL, board.SDA)
lcd = character_lcd.Character_LCD_RGB_I2C(i2c, 16, 2)
lcd.color = [0, 0, 100]
lcd.message = "Wake up, Neo..." 
time.sleep(3)
lcd.clear()
lcd.color = [100, 0, 0]
lcd.message = "Press Left Key\nfor Red Pill"
time.sleep(2)
lcd.clear()
lcd.color = [0, 0, 100]
lcd.message = "Press Right Key\nfor Blue Pill"
time.sleep(2)
lcd.clear()
lcd.color = [50, 0, 50]
lcd.message = "Knock, knock\nNeo..."

# Functions
def agent():
            lcd.clear()
            lcd.color = [0, 100, 0]
            lcd.message = "An Agent has\nappeared!"
            time.sleep(2)
            lcd.clear()
            lcd.message = "Hold Left to\nfight!"
            time.sleep(1)
            lcd.clear()
            lcd.message = "Hold Right to\nrun away!"
            time.sleep(1)
            lcd.clear()
            lcd.message = "Fight or\nrun away?" 
            time.sleep(5)
            lcd.clear()
            if lcd.left_button:
                lcd.clear()
                lcd.color = [0, 0, 100]
                lcd.message = "You dodged\na bullet!"
                time.sleep(2)
                lcd.clear()
                lcd.color = [50, 0, 50]
                lcd.message = "Try again! :)"
            if lcd.right_button:
                lcd.clear()
                lcd.color = [25, 25, 25]
                lcd.message = "You've been\ncaught!"
                time.sleep(1)
                lcd.clear()
                lcd.message = "The Matrix has\nyou..."
                time.sleep(2)
                lcd.clear()
                lcd.color = [50, 0, 50]
                lcd.message = "Try again! :("

def blue_pill():
                lcd.clear()
                lcd.color = [0, 0, 100]
                lcd.message = "You have chosen\nthe Blue Pill..."
                time.sleep(2)
                lcd.clear()
                lcd.message = "The story ends,"
                time.sleep(1)
                lcd.clear()
                lcd.message = "You wake up in\nyour bed."
                time.sleep(1)
                lcd.clear()
                lcd.color = [0, 100, 0]
                lcd.message = "The Matrix has\nyou..."  
           
def red_pill():
            lcd.clear()
            lcd.color = [100, 0, 0]
            lcd.message = "You have chosen\nthe Red Pill..."
            time.sleep(2)
            lcd.clear()
            lcd.color = [25, 0, 25]
            lcd.message = "You wake up from\nthe Matrix."
            time.sleep(2)
            lcd.clear()
            lcd.message = "Your eyes hurt.."
            time.sleep(2)
            lcd.clear()
            lcd.message = "You've never\nused them before" 
            time.sleep(2)
            lcd.clear()
            lcd.message = "Hold 'Select'\nto continue..."
            time.sleep(10)
            lcd.clear()
            if lcd.select_button:
                lcd.clear()
                lcd.color = [0, 0, 100]
                lcd.message = "You are the One!\nYesss!"
                time.sleep(3)
                lcd.clear()
                lcd.blink = True
                lcd.color = [50, 0, 50]
                lcd.message = "Follow the\nWhite Rabbit..."
                time.sleep(3)
                lcd.clear()
                lcd.blink = False
                lcd.color = [0, 0, 0]
                lcd.message = "The cake is\na lie..."
                time.sleep(5)
                lcd.clear()
                exit()

def oracle():
            lcd.clear()
            lcd.color = [0, 100, 0]
            lcd.message = "Talk to the\nOracle?"
            time.sleep(1)
            lcd.clear()
            lcd.message = "Left for 'Yes'\nRight for 'No'"
            time.sleep(5)
            lcd.clear()
            if lcd.left_button:
                lcd.clear()
                lcd.color = [0, 0, 100]
                lcd.message = "The Oracle says\nyou are..."
                time.sleep(1)
                lcd.clear()
                lcd.message = "not the One...\nSorry, kid."
                time.sleep(5)
                lcd.clear()
            if lcd.right_button:
                lcd.clear()
                lcd.message = "The Oracle does\nnot want"
                time.sleep(1)
                lcd.clear()
                lcd.message = "to talk to you\nanyways!"
                time.sleep(3)
                lcd.clear()
                lcd.color = [25, 25, 25]
                lcd.message = "Choose the Red\nor Blue Pill"
                time.sleep(5)
                lcd.clear()

# Pair button to function
while True:
    if lcd.up_button:
        agent()
    if lcd.right_button:
        blue_pill()
    if lcd.left_button:
        red_pill()
    if lcd.down_button:
        oracle()

# Additional choices
while agent() == True:
            if lcd.left_button:
                lcd.clear()
                lcd.color = [0, 0, 100]
                lcd.message = "Wow! You dodged\na bullet!"
                time.sleep(2)
                lcd.clear()
                lcd.color = [50, 0, 50]
                lcd.message = "Try again! :)"
            if lcd.right_button:
                lcd.clear()
                lcd.color = [25, 25, 25] 
                lcd.message = "You've been\ncaught!"
                time.sleep(1)
                lcd.clear()
                lcd.color = [0, 100, 0]
                lcd.message = "The Matrix has\nyou..."
                time.sleep(2)
                lcd.clear()
                lcd.color = [50, 0, 50]
                lcd.message = "Try again! :("

while red_pill() == True:
            if lcd.select_button:
                lcd.clear()
                lcd.color = [0, 0, 100]
                lcd.message = "You are the One!\nYesss!"
                time.sleep(3)
                lcd.clear()
                lcd.blink = True
                lcd.message = "Follow the\nWhite Rabbit..."
                time.sleep(5)
                lcd.clear()
                lcd.blink = False
                lcd.color = [0, 0, 0]
                lcd.message = "The cake is\na lie..."
                time.sleep(3)
                lcd.clear()
                exit()

while oracle() == True:
            if lcd.left_button:
                lcd.clear()
                lcd.color = [0, 0, 100]
                lcd.message = "The Oracle says\nyou are"
                time.sleep(1)
                lcd.clear()
                lcd.message = "not the One\nSorry, kid."
                time.sleep(5)
                lcd.clear()
            if lcd.right_button:
                lcd.clear()
                lcd.message = "The Oracle does\nnot want"
                time.sleep(1)
                lcd.clear()
                lcd.message = "to talk to you\nanyways!"
                time.sleep(3)
                lcd.clear()
                lcd.color = [25, 25, 25]
                lcd.message = "Choose the Red or\nBlue Pill"
                time.sleep(5)
                lcd.clear()
                lcd.color = [0, 0, 0]
