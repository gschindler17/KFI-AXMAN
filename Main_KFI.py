import sys
from PyQt6.QtWidgets import QApplication
from PythonFiles.KFI_GUI import KFI_GUI
from PythonFiles.KFI_Controller import KFI_Controller
from PythonFiles.KFI_Logic import KFI_Logic

if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)

        logic = KFI_Logic()  # Instantiate Model (Logic)
        gui = KFI_GUI()  # Instantiate View (GUI)
        controller = KFI_Controller(gui, logic)  # Pass GUI and Logic to Controller

        gui.set_controller(controller)  # Pass controller to GUI
        gui.show()
        
        sys.exit(app.exec())
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt detected. Exiting gracefully...")
        sys.exit(0)
