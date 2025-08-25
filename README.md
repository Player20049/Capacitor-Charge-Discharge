🧠 Capacitor Charge & Discharge Monitor (Raspberry Pi)

This project reads and visualizes the charging and discharging curves of a capacitor using a Raspberry Pi, an MCP3008 ADC, and GPIO-controlled discharge logic.

<p align="center"> <img src="Work/Capacitor_Charge_Discharge_Visual_Plot.png" width="600"/> </p>
📦 Components Used
Component	Purpose
Raspberry Pi (any model)	Main controller
MCP3008	10-bit ADC to read analog voltages
Capacitor (e.g., 1000μF)	Component under test
NPN Transistor	Discharge control (via GPIO)
Resistors	Limiting current to base/circuit
GPIO Pin (e.g., GPIO 18)	Discharge switching
Breadboard & Wires	Circuit assembly
🔧 Circuit Schematic
<p align="center"> <img src="Work/Capacitor_Charge_Discharge_Schematic.png" width="650"/> </p>
🚀 Features

📊 Real-time voltage sampling via MCP3008

⚡ Controlled discharge using GPIO & NPN transistor

📈 Saves and plots voltage vs time

🔁 Continuous cycle logging

💾 Automatically saves plot to desktop

🛠️ Installation
🔹 1. Enable SPI on your Raspberry Pi
sudo raspi-config
# Navigate to Interface Options -> SPI -> Enable


Then reboot.

🔹 2. Install System Dependencies
sudo apt update
sudo apt install python3-pip
sudo apt install python3-spidev
sudo apt install python3-gpiozero
sudo apt install python3-matplotlib


Alternatively, install via pip:

pip3 install matplotlib

📄 Python Script Overview
import time
import spidev
from gpiozero import OutputDevice
import matplotlib.pyplot as plt


spidev: Communicates with MCP3008 ADC

gpiozero: Activates transistor to discharge capacitor

matplotlib: Plots the charge/discharge curves

📂 Project Structure
Capacitor-Charge-Discharge/
│
├── capacitor_logger.py               # Main Python script
├── Capacitor_Charge_Discharge_Schematic.png  # Schematic image
├── Capacitor_Charge_Discharge_Visual_Plot.png  # Output plot sample
├── README.md                         # This file
└── requirements.txt                  # Minimal pip dependencies

🧪 Example Output
(Charging) Time: 3.59s | Voltage: 3.17 V
(Charging) Time: 3.60s | Voltage: 3.20 V
(Discharging) Time: 3.61s | Voltage: 0.01 V
...
✅ Plot saved to your Desktop as capacitor_plot5.png

⚠️ Known Limitations

Discharge may seem abrupt if:

The base resistor is too small (saturation)

The capacitor value is small (fast decay)

Discharge resistor path is too low in resistance

Real-world factors like temperature and noise may affect readings

🧠 Ideas for Expansion

Add OLED/serial display for live readings

Add capacitor value detection

Detect ESR or leakage

Log data to a CSV file

Compare different capacitor types (electrolytic vs ceramic)

📜 License

MIT License. Feel free to build on this work with attribution.
