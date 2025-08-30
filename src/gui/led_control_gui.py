# src/devices/led.py
try:
    import nidaqmx
    real_device = True
except ModuleNotFoundError:
    real_device = False

class LED:
    def __init__(self, channel="Dev1/ao2", max_voltage=5.0):
        self.channel = channel
        self.max_voltage = max_voltage

    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.max_voltage):
            raise ValueError(f"Voltage must be between 0 and {self.max_voltage} V.")
        if real_device:
            import nidaqmx
            with nidaqmx.Task() as task:
                task.ao_channels.add_ao_voltage_chan(self.channel)
                task.write(voltage, auto_start=True)
        print(f"[MOCK] Voltage set to {voltage} V")
