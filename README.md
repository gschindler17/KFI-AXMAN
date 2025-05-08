# KFI Axman - Relay/Breaker Status and Control Simulator

Developed by **KFI Engineers** and **Bethel University**  
Created: 04/29/2025 | Updated: 05/06/2025

---

## 📘 Overview

The **KFI Axman** is a real-time Relay/Breaker Status and Control Simulator designed to:
- Interface with external protective relays
- Simulate virtual circuit breakers
- Visually reflect real-time system changes in a GUI

It serves as a feedback loop between a **relay controller** and a **Raspberry Pi GUI**, processing 12 discrete inputs and 12 outputs.

---

## ⚙️ Hardware Specifications

- **Inputs (Right side)**
  - 12 discrete input screw terminals
  - 120V DC logic high, ground = logic low
  - Max input current: 6A per relay

- **Outputs (Left side)**
  - 12 discrete output screw terminals
  - 120V DC output
  - Max total output current: 3A

- **Raspberry Pi Interface**
  - HDMI-out, 4x USB, USB-C (power), Ethernet
  - First USB port is for serial connection to Arduino Mega

---

## 🔧 Internal Architecture

1. Inputs feed into 115V relays → converted to 5V signals for Arduino.
2. Arduino sends digital input values to Raspberry Pi via USB-Serial.
3. Raspberry Pi runs the GUI, processes logic, and sends output commands back.
4. Arduino drives 5V relays to switch 115V output signals to external devices.

---

## 💻 Software Installation

### Raspberry Pi Setup

```bash
git clone https://github.com/gschindler17/KFI-AXMAN.git
sudo apt update
sudo apt upgrade
sudo apt install python3-pyqt6
sudo apt install pyqt6-dev-tools
```

### Arduino Setup

```bash
sudo apt install arduino
cd KFI-AXMAN
arduino ARDUINO_V1.ino
```

**Flash Arduino via Arduino IDE:**
- Board: Arduino Mega
- Port: Match your connected device (default: `/dev/ttyACM0`)
- Upload using the top-left arrow in the IDE

---

## ▶️ Running the KFI Axman Program

From the Raspberry Pi terminal:

```bash
python3 Main_KFI.py
```

This launches the GUI for real-time monitoring and control.

---

## 🖱️ Manual Control Panel

- **"IN" Buttons** → Reflect input pins 1–12
- **"OUT" Buttons** → Reflect output pins 13–24 (offset by 12)
- Default color: Green (de-energized), Red (energized)
- Persistent state updates based on real-time values

---

## 🔢 Boolean Logic Programming

The "Input Logic" box accepts Boolean expressions for outputs 13–24 using pins 1–24.

**Syntax Requirements:**
```
<output pin> = <boolean expression>;
```

- Each line must end with `;` and contain exactly one `=`
- Only output pins (13–24) allowed on the left
- Logical Operators:

| Symbol | Meaning  | Example     |
|--------|----------|-------------|
| `T`    | True     | `T`         |
| `F`    | False    | `F`         |
| `!`    | NOT      | `!2`        |
| `*`    | AND      | `1 * 2`     |
| `+`    | OR       | `1 + 2`     |
| `()`   | Grouping | `(1*2)+3`   |

### ✅ Valid Examples:
- `13 = 1 * 2;`
- `14 = !5 + 6;`
- `15 = T * 3;`
- `16 = 13 + 14;`

### ❌ Invalid Examples:
- `12 = 1 * 2;` → LHS must be 13–24
- `17 == 3 + 4;` → Use `=`, not `==`
- `18 = 1 * ;` → Incomplete
- `19 = 1 && 2;` → Use `*`, not `&&`
- `13=1` → Missing semicolon

---

## 📁 Importing Text Files

1. Place your logic file in the `settings_config/` directory.
2. Enter the filename (e.g., `mylogic.txt`) in the “Import Text File” box.
3. Press **Import** to load contents into the logic field.
4. Press **Confirm** to apply logic.

⚠️ Filenames must not include blank spaces.

---

## ⚡ Breaker Panel

Simulates 3 circuit breakers with:

- **Open/Close control** mapped to input pins 7–12
- **Status feedback** mapped to outputs 22–24
  - Red = energized (closed), Green = de-energized (open)
  - If both Open and Close are high, breaker defaults to Open

### ⚙ Breaker Override Logic

Each breaker appends hidden logic expressions like:

```text
22 = 8 * !7;
```

This overrides manual Boolean code for outputs 22–24.

---

## 📎 Repository

GitHub: [https://github.com/gschindler17/KFI-AXMAN](https://github.com/gschindler17/KFI-AXMAN)

---

## 🧑‍💻 Contributors

Developed by KFI Engineers and students at Bethel University.
