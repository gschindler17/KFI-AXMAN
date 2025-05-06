import threading
import time


class KFI_Controller:
    def __init__(self, gui, logic):
        self.gui = gui
        self.logic = logic
        print("Controller Initialized")

        self.output_pins = [
            False, False, False, False, 
            False, False, False, False, 
            False, False, False, False
            ]
        
        self.bool_logic = ""
        self.breaker = []
        self.feedback = []
        self.breaker_commands = []
        self.arduino_crashed = False

        # Passive thread to handle updating the voltage
        self.taking_input_bool = True
        self.input_delay = 0.01
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
        self.output_pins[pin] = True
        # self.logic.toggle_output_pin(pin)

    def handle_out_click(self, out_id):
        result =  self.logic.process_out_action(out_id)
        self.toggle_output_pin(out_id)
        self.gui.out_button_color(out_id, result)
        print("Controller: out_{} clicked".format(out_id))

    def handle_in_click(self, in_id, line_id):
        # result = self.logic.get_input_data(in_id)
        # self.gui_in_button(in_id, result)
        # self.gui.update_line(line_id, result)
        print('Controller: in_{} clicked'.format(in_id))


    def check_if_output_toggle(self):
        for i, val in enumerate(self.output_pins):
            if self.output_pins[i]:
                print("KFI_Controller: Trying to toggle pin at index", i)
                self.logic.toggle_output_pin(i)
                self.output_pins[i] = False

    def READ_ALL_INPUTS(self):
        self.logic.setup_Arduino()
        counter = 15
        time.sleep(1)
        self.gui.update_line()
        while(self.taking_input_bool):
            self.check_if_output_toggle()
            input_states = self.logic.READ_ALL_INPUTS()
            self.gui.update_inputs(input_states)
            time.sleep(self.input_delay)
            counter = counter + 1
            if counter >= 15:
                self.submit_bool_logic(None)
                counter = 0
                self.update_breaker_feedback(self.breaker, self.feedback)
                if self.logic.get_arduino_crashed():
                    self.arduino_crashed = True
                    self.gui.arduino_crashed()
        pass
    
    def submit_bool_logic(self, expression):
        if expression is None:
            expression = self.bool_logic
        else:
            self.bool_logic = expression
        print(expression)
        temp = self.logic.evaluate_logic_code(expression)
        print(temp)
        self.logic.set_all_output_pins(temp)
        self.update_all_out_buttons(temp)
        
        

    def update_all_out_buttons(self, output_vals):
        for i, val in enumerate(output_vals): 
            if val:
                self.gui.out_button_color(i, "red")
            else:
                self.gui.out_button_color(i, "green")

    #TODO Put the guts of this into the logic function
    def pass_breaker_vals(self, breaker, open, close, feedback):
        print("Controller: breaker:", breaker, "open:", open, "close:", close, "feedback:", feedback)
        
        self.breaker_command_string = ""
        for i, val in enumerate(breaker):
            self.breaker_command_string = self.breaker_command_string + f"{feedback[i]}={close[i]}*!{open[i]};\n"
        # print("\nController: Command String:", self.breaker_command_string)
        # print("\nController: Annexed String:", self.bool_logic + self.breaker_command_string)
        self.submit_bool_logic(self.bool_logic + self.breaker_command_string)
        self.feedback = feedback
        self.breaker = breaker
        self.update_breaker_feedback(self.breaker, self.feedback)


    # def set_breaker_feedback(self, breaker, feedback):
    #     print("Controller: breaker:", breaker, "feedback:", feedback)

    def update_breaker_feedback(self, breaker, feedback):
        # feedback_vals is a list of true or false for the corresponding feedback location
        # feedback is just what output pin is mapped to the breaker
        feedback_vals = self.logic.get_breaker_feedback(breaker, feedback)
        self.gui.update_breaker_feedback(breaker, feedback_vals)


