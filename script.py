import pyautogui
import keyboard
import time
from gui import GUI

# Get rid of the fail safe your system has for automated mouse movement
pyautogui.FAILSAFE = False
# Change this to change the delay between each click in seconds
DELAY_SECONDS = 0.5
# Change this to change the delay between each click in seconds on the agent selection screen
DELAY_SECONDS_AGENT = 0.05

def click_agent():
    # Move the mouse to the agent's coordinates
    pyautogui.moveTo(agent_x, agent_y, DELAY_SECONDS_AGENT)
    # Perform a single click
    pyautogui.click()
    
def click_lock_in():
    # Move the mouse to the lock in button's coordinates
    pyautogui.moveTo(1000, 875, DELAY_SECONDS_AGENT)
    # Perform a single click
    pyautogui.click()
    
# Dictionary of agents and their pixel coordinates hard coded. Because the game updates this changes often.
# If I wrote a function to find the coordinates of the agents, it would be fruitless as the game updates the coordinates of the agents.
agent_dictionary = {
    "astra": [580,931],
    "breach": [658,931],
    "brimstone": [732,931],
    "chamber": [789,931],
    "cypher": [805,931],
    "fade": [959,931],
    "jett": [1200,931],
    "kayo": [1265,931],
    "killjoy": [1346,931],
    "neon": [578,1009],
    "omen": [657,1009],
    "phoenix": [732,1010],
    "raze": [811,1010],
    "reyna": [886,1010],
    "sage": [962,1010],
    "skye": [1038,1010],
    "sova": [1113,1010],
    "viper": [1190,1010],
    "yoru": [1265,1010],
    "gekko": [1039,931],
    "harbor": [1113,931],
    }
gui = GUI() # create the GUI and call it

agent_x, agent_y = agent_dictionary[gui.agent_input.lower()]
            
if(gui.response_value):
    while True:
        # Delay for 5 seconds
        time.sleep(DELAY_SECONDS)
        # Check if the space key is pressed
        if keyboard.is_pressed(gui.keybind_input):
            click_agent()
            click_lock_in()
            break 

