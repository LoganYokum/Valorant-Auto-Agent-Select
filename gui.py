from PyQt5 import QtWidgets
import time
class GUI:
    def __init__(self):
        self.app = QtWidgets.QApplication([])
        self.window = QtWidgets.QWidget()
        self.window.setWindowTitle("Valorant Auto Agent Select GUI")
        
        # Set the window size to 800 pixels wide by 600 pixels tall
        self.window.resize(300, 200)
        
        # Create a QLabel for static text
        self.label = QtWidgets.QLabel("Select Agent:", self.window)
        self.label.setGeometry(50, 50, 200, 30)
        
        # Create a QComboBox for agent selection
        self.agent_combobox = QtWidgets.QComboBox(self.window)
        self.agent_combobox.setGeometry(150, 50, 100, 30)
        
        # Add agent options to the combobox
        self.agent_combobox.addItem("Astra")
        self.agent_combobox.addItem("Breach")
        self.agent_combobox.addItem("Brimstone")
        self.agent_combobox.addItem("Chamber")
        self.agent_combobox.addItem("Cypher")
        self.agent_combobox.addItem("Fade")
        self.agent_combobox.addItem("Jett")
        self.agent_combobox.addItem("Kayo")
        self.agent_combobox.addItem("Killjoy")
        self.agent_combobox.addItem("Neon")
        self.agent_combobox.addItem("Omen")
        self.agent_combobox.addItem("Phoenix")
        self.agent_combobox.addItem("Raze")
        self.agent_combobox.addItem("Reyna")
        self.agent_combobox.addItem("Sage")
        self.agent_combobox.addItem("Skye")
        self.agent_combobox.addItem("Sova")
        self.agent_combobox.addItem("Viper")
        self.agent_combobox.addItem("Yoru")
        self.agent_combobox.addItem("Gekko")
        self.agent_combobox.addItem("Harbor")

        # Create a QLabel for static text
        self.label = QtWidgets.QLabel("Select keybind:", self.window)
        self.label.setGeometry(50, 100, 200, 30)
        
        # Create a QComboBox for agent selection
        self.keybind_combobox = QtWidgets.QComboBox(self.window)
        self.keybind_combobox.setGeometry(150, 100, 100, 30)
        
        # Add agent options to the combobox
        self.keybind_combobox.addItem("space")
        self.keybind_combobox.addItem("enter")
        self.keybind_combobox.addItem("tab")
        self.keybind_combobox.addItem("shift")        
        
        # Create a QPushButton (button)
        self.button = QtWidgets.QPushButton("Run script", self.window)
        self.button.setGeometry(50, 150, 200, 30)
        self.button.clicked.connect(self.on_button_clicked_agent_and_script)
        self.agent_input = "Astra" # default agent
        self.response_value = False  # don't run script until button is clicked
        
        self.window.show()
        self.app.exec_()
        
    def on_button_clicked_agent_and_script(self):
        # Retrieve the selected agent from the combobox
        self.agent_input = self.agent_combobox.currentText()
        # Retrieve the selected keybind from the combobox
        self.keybind_input = self.keybind_combobox.currentText()
        # Set the response value to True to run the script
        self.response_value = True
        self.on_success()
        self.window.close()
        self.app.quit()
        
    def on_success(self):
        # Create and display a QMessageBox as the response window
        response_box = QtWidgets.QMessageBox()
        response_box.setWindowTitle("Response")
        response_box.setText("Hold the key specified to begin the auto select process: ")
        response_box.setInformativeText(self.keybind_input)
        response_box.setIcon(QtWidgets.QMessageBox.Information)
        response_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
        response_box.show()
        response_box.exec_()
        
