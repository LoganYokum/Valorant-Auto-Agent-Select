#Must have python3 installed! Read the README for python download link
# Get the operating system
os=$(uname)

# Check if the operating system is Linux
if [ "$os" == "Linux" ]; then
    yes | apt install python3-pip
    yes | apt-get install python3-tk python3-dev
    yes | pip install python-xlib
    yes | pip install pyautogui
    yes | pip install keyboard
    yes | pip install PyQt5
elif [ "$os" == "Windows" ]; then
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python get-pip.py
    pip install python-xlib
    pip install pyautogui
    pip install keyboard
    pip install PyQt5
else
    echo "Unsupported operating system: $os"
fi



