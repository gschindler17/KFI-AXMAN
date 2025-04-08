import threading
import time


class KFI_Controller:
    def __init__(self, gui, logic):
        self.gui = gui
        self.logic = logic
        print("Controller Initialized")

        # Passive thread to handle updating the voltage
        self.taking_input_bool = True
        self.input_delay = 0.1
        thread = threading.Thread(target= lambda: self.READ_ALL_INPUTS(), daemon=True)
        thread.daemon = True
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

    def toggle_output_pin(self, pin):
        self.logic.toggle_output_pin(pin)

    def handle_out_click(self, out_id):
        result =  self.logic.process_out_action(out_id)
        self.toggle_output_pin(out_id)
        self.gui.out_button_color(out_id, result)
        print("Controller: out_{} clicked".format(out_id))

    def handle_in_click(self, in_id, line_id):
        result = self.logic.get_input_data(in_id)
        self.gui_in_button(in_id, result)
        self.gui.update_line(line_id, result)
        print('Controller: in_{} clicked'.format(in_id))


    def READ_ALL_INPUTS(self):
        while(self.taking_input_bool):
            self.logic.READ_ALL_INPUTS()
            time.sleep(self.input_delay)
