import sys
from PyQt6.QtWidgets import QApplication
import PythonFiles.KFI_GUI
import PythonFiles.KFI_Controller
import PythonFiles.KFI_Logic

if __name__ == "__main__":
    app = QApplication(sys.argv)

    logic = KFI_Logic.KFILogic()  # Instantiate Model (Logic)
    gui = KFI_GUI.MyApp()  # Instantiate View (GUI)
    controller = KFI_Controller.KFIController(gui, logic)  # Pass GUI and Logic to Controller

    gui.set_controller(controller)  # Pass controller to GUI
    gui.show()
    
    sys.exit(app.exec())
