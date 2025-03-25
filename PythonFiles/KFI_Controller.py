import threading
import time


class KFIController:
    def __init__(self, gui, logic):
        self.gui = gui
        self.logic = logic
        print("Controller Initialized")

        # Passive thread to handle updating the voltage
        self.passive_volts_bool = True
        self.passive_volts_speed = 0.5
        thread = threading.Thread(target= lambda: self.passive_update_volts(), daemon=True)
        thread.start()


    def handle_button_click(self, button_id):
        result = self.logic.process_button_action(button_id)  # Call Logic function
        print(f"Button {button_id} clicked! Result: {result}")  # Replace with UI update if needed
        

    def handle_text_input(self, button_id, line_edit_widget):
        text = line_edit_widget.text()
        result = self.logic.process_text_input(button_id, text)  # Call Logic function
        print(f"Button {button_id} clicked! Processed text: {result}")  # Replace with UI update if needed


    def handle_relay_click(self, relay_id):
        result = self.logic.process_relay_action(relay_id)

        self.gui.line_relay_color(relay_id, result)
        print("Controller: Relay {} clicked; sent to processing".format(relay_id))

    def submit_volts(self, relay_id, text):
        result = self.logic.submit_volts(relay_id, text)

    def get_voltage_pin(self, pin):
        result = self.logic.read_voltage(pin)
        return result

    def toggle_voltage_read(self, pin):
        self.logic.toggle_voltage_read(pin)

    def toggle_output_pin(self, pin):
        self.logic.toggle_output_pin(pin)


    def passive_update_volts(self):
        while(self.passive_volts_bool):
            relay_volts = self.logic.get_relay_volts()
            self.gui.update_volts_boxes(relay_volts)
            # print("KFI_Controller: passive update...")
            time.sleep(self.passive_volts_speed)
