


class KFIController:
    def __init__(self, gui, logic):
        self.gui = gui
        self.logic = logic
        print("Controller Initialized")

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