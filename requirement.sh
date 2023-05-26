#Must have python3 installed! Read the README for python download link
# Get the operating system
os=$(uname)

# Check if the operating system is Linux
if [ "$os" == "Linux" ]; then
    yes | apt install python3-pip
    yes | apt-get install python3-tk python3-dev
elif [ "$os" == "Windows" ]; then
    yes | curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    yes | python get-pip.py
else
    echo "Unsupported operating system: $os"
fi

yes | pip install python-xlib
yes | pip install pyautogui
yes | pip install keyboard

