from PyQt5 import QtWidgets

class GUI:
    def __init__(self):
        self.app = QtWidgets.QApplication([])
        self.window = QtWidgets.QWidget()
        self.window.setWindowTitle("Valorant Auto Agent Select GUI")
        
        # Set the window size to 800 pixels wide by 600 pixels tall
        self.window.resize(300, 200)
        
        # Create a QLabel for static text
        self.label = QtWidgets.QLabel("Enter Agent:", self.window)
        self.label.setGeometry(50, 50, 200, 30)
        
        # Create a QLineEdit (input box)
        self.input_box = QtWidgets.QLineEdit(self.window)
        self.input_box.setGeometry(150, 50, 100, 30)

        # Create a QPushButton (button)
        self.button = QtWidgets.QPushButton("Lock in agent", self.window)
        self.button.setGeometry(50, 100, 200, 30)
        self.button.clicked.connect(self.on_button_clicked_agent)
        self.agent_input = ""
                
        # Create a QPushButton (button)
        self.button = QtWidgets.QPushButton("Run script", self.window)
        self.button.setGeometry(50, 150, 200, 30)
        self.button.clicked.connect(self.on_button_clicked_script)
        self.response_value = False # dont run script until button is clicked
        
        self.window.show()
        self.app.exec_()

    def on_button_clicked_agent(self):
        # Retrieve the text entered by the user
        self.agent_input = self.input_box.text()
        self.input_box.clear()
        print("User input:", self.agent_input)
    def on_button_clicked_script(self):
        self.response_value = True
        self.window.close()
        self.app.quit()
    def on_success(self):
        # Create and display a QMessageBox as the response window
        response_box = QtWidgets.QMessageBox()
        response_box.setWindowTitle("Response")
        response_box.setText("Agent successfully locked in")
        response_box.setIcon(QtWidgets.QMessageBox.Information)
        response_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
        response_box.exec_()
    def on_fail(self):
        # Create and display a QMessageBox as the response window
        response_box = QtWidgets.QMessageBox()
        response_box.setWindowTitle("Response")
        response_box.setText("Agent not found. Please try again or type exit to quit the program")
        response_box.setIcon(QtWidgets.QMessageBox.Information)
        response_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
        response_box.exec_()

