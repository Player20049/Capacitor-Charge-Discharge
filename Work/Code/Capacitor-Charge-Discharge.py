#Line 79 address must be changed

import time
import spidev
from gpiozero import OutputDevice
import matplotlib.pyplot as plt

# ---------- MCP3008 SPI Setup ----------
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1350000

# ---------- Function to Read from ADC ----------
def read_channel(channel):
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data

# ---------- Function to Convert ADC to Voltage ----------
def convert_voltage(adc_value, vref=3.3):
    return round((adc_value * vref) / 1023.0, 2)

# ---------- Discharge Pin Using gpiozero ----------
DISCHARGE_PIN = 18
discharge = OutputDevice(DISCHARGE_PIN, active_high=True, initial_value=False)

# ---------- Measurement Loop ----------
try:
    timestamps = []
    voltage_log = []
    start_time = time.time()

    while True:
        # --- Discharge Phase (improved sampling) ---
        print("Discharging capacitor...")
        discharge.on()

        for _ in range(400):  # More samples for better resolution
            adc_value = read_channel(0)
            voltage = convert_voltage(adc_value)
            now = time.time() - start_time

            voltage_log.append(voltage)
            timestamps.append(now)

            print(f"(Discharging) Time: {now:.2f}s | Voltage: {voltage:.2f} V")
            time.sleep(0.01)  # Faster sampling

        discharge.off()

        # --- Charging Phase ---
        print("Charging...")
        for _ in range(400):  # Adjust range for more/fewer samples
            adc_value = read_channel(0)
            voltage = convert_voltage(adc_value)
            now = time.time() - start_time

            voltage_log.append(voltage)
            timestamps.append(now)

            print(f"(Charging) Time: {now:.2f}s | Voltage: {voltage:.2f} V")
            time.sleep(0.01)

        print("\nCycle complete. Restarting...\n")
        time.sleep(1)

except KeyboardInterrupt:
    print("Measurement stopped by user.")

    # Plot voltage vs. time
    plt.figure(figsize=(10, 4))
    plt.plot(timestamps, voltage_log, label='Capacitor Voltage (V)', color='blue')
    plt.xlabel('Time (s)')
    plt.ylabel('Voltage (V)')
    plt.title('Capacitor Charge & Discharge Curve')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("/home/Zeiad/Desktop/capacitor_plot.png")  # Change this depensding on the location of your folder you can write "ls" in the terminal and find out
    print("✅ Plot saved to your Desktop as capacitor_plot3.png")

finally:
    discharge.close()
    spi.close()
