import pyautogui
import keyboard
import time

# Get rid of the fail safe your system has for automated mouse movement
pyautogui.FAILSAFE = False
# Change this to change the delay between each click in seconds
delay_seconds = 0.5
# Change this to change the delay between each click in seconds on the agent selection screen
delay_seconds_agent = 0.1

# Dictionary of agents and their pixel coordinates hard coded. Because the game updates this changes often.
# If I wrote a function to find the coordinates of the agents, it would be fruitless as the game updates the coordinates of the agents.
agent_dictionary = {
    "astra": [537,931],
    "breach": [621,931],
    "brimstone": [705,931],
    "chamber": [789,931],
    "cypher": [873,931],
    "fade": [957,931],
    "jett": [1041,931],
    "kayo": [1125,931],
    "killjoy": [1209,931],
    "neon": [1293,931],
    "omen": [1377,931],
    "phoenix": [537,1010],
    "raze": [621,1010],
    "reyna": [705,1010],
    "sage": [789,1010],
    "skye": [873,1010],
    "sova": [957,1010],
    "viper": [1041,1010],
    "yoru": [1125,1010],
    "gekko": [1209,1010],
    "harbor": [1293,1010],
    }
# Change the name here for the agent you want to click
agent_x, agent_y = agent_dictionary["jett"]

def click_agent():
    # Move the mouse to the agent's coordinates
    pyautogui.moveTo(agent_x, agent_y, delay_seconds_agent)
    # Perform a single click
    pyautogui.click()
    
def click_lock_in():
    # Move the mouse to the lock in button's coordinates
    pyautogui.moveTo(1000, 875, delay_seconds_agent  )
    # Perform a single click
    pyautogui.click()
    
while True:
    # Delay for 5 seconds
    time.sleep(delay_seconds)
    print("HOLD press space on the keyboard")
    # Check if the space key is pressed
    if keyboard.is_pressed('space'):
        click_agent()
        click_lock_in()
        break

