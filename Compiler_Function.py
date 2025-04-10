import re

def evaluate_logic_code(code_str, inputs, outputs):
    new_outputs = outputs.copy()
    lines = [line.strip() for line in code_str.strip().split(';') if line.strip()]

    for line in lines:
        if '=' not in line:
            continue

        lhs, rhs = line.split('=')
        output_index = int(lhs.strip()) - 13  # 13–24 maps to 0–11

        original_expression = rhs.strip()
        expression = original_expression

        # Replace NOT (!) with Python's `not`
        expression = re.sub(r'!', 'not ', expression)

        # Replace logical operators: * → and, + → or
        expression = expression.replace('*', ' and ')
        expression = expression.replace('+', ' or ')

        # Replace numbers 1–12 with inputs[x] safely
        def replace_input_refs(match):
            num = int(match.group())
            return f"inputs[{num - 1}]"

        expression = re.sub(r'\b([1-9]|1[0-2])\b', replace_input_refs, expression)

        try:
            result = bool(eval(expression, {'inputs': inputs}))
            new_outputs[output_index] = int(result)

            # Debug statements (uncomment to enable)
            # print(f"[DEBUG] Line: {line}")
            # print(f"        Raw expression: {original_expression}")
            # print(f"        Parsed expression: {expression}")
            # print(f"        Result: {int(result)} → Output {output_index + 13}")

        except Exception as e:
            print(f"[ERROR] Failed to evaluate line '{line}': {e}")

    return new_outputs


if __name__ == "__main__":
    inputs = [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    outputs = [0] * 12

    code = """
    13=1*12;
    14=!(1*12);
    15=1+4;
    16=!(5+6)*2;
    """

    updated_outputs = evaluate_logic_code(code, inputs, outputs)
    print("Final outputs:", updated_outputs)
