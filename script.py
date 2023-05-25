import pyautogui
import keyboard
import time

# Get rid of the fail safe your system has for automated mouse movement
pyautogui.FAILSAFE = False
# Change this to change the delay between each click in seconds
delay_seconds = 0.5
# Change this to change the delay between each click in seconds on the agent selection screen
delay_seconds_agent = 0.3

# Dictionary of agents and their pixel coordinates hard coded. Because the game updates this changes often.
# If I wrote a function to find the coordinates of the agents, it would be fruitless as the game updates the coordinates of the agents.
agent_dictionary = {
    "jett": [0,0],
    "raze": [0,0],
    "breach": [0,0],
    "omen": [0,0],
    "brimstone": [0,0],
    "phoenix": [0,0],
    "sage": [0,0],
    "sova": [0,0],
    "viper": [0,0],
    "cypher": [0,0],
    "reyna": [0,0],
    "killjoy": [0,0],
    "skye": [0,0],
    "yoru": [0,0],
    "astra": [0,0],
    "kayo": [0,0],
    "neon": [0,0],
    "harbor": [0,0],
    "chamber": [0,0],
    "fade": [0,0],
    "gekko": [0,0],
    }
# Change the name here for the agent you want to click
agent_x, agent_y = agent_dictionary["jett"]

def click_agent():
    # Move the mouse to the agent's coordinates
    pyautogui.moveTo(agent_x, agent_y, delay_seconds)
    # Perform a single click
    pyautogui.click()
    
while True:
    # Delay for 5 seconds
    time.sleep(delay_seconds)
    print("HOLD press space on the keyboard")
    # Check if the space key is pressed
    if keyboard.is_pressed('space'):
        click_agent()
        break

