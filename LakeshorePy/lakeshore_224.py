import pyvisa

class Lakeshore224:
    """
    A class for the Lakeshore 224 temperature controller.

    This class handles connecting to the device, configuring measurements, and acquiring data.
    """

    def __init__(self, address):
        """
        Initializes the Lakeshore 224 instance.

        :param address: The GPIB address or IP address of the device.
        """
        self.address = address
        self.rm = pyvisa.ResourceManager()
        self.device = self.rm.open_resource(self.address)

    def connect(self):
        """
        Connects to the Lakeshore 224 device.
        """
        self.device.write("*RST")  # Reset the device
        self.device.write("INPUT A")  # Set input A as the primary input
        self.device.write("INTYPE K")  # Set the input type to K (thermocouple)
        self.device.write("RANGE 2")  # Set the input range to 2 (0-300 K)

        # Verify the configuration by querying the device
        response = self.device.query("INTYPE?")  # Read the input type setting
        if response.strip() != "K":
            raise Exception("Failed to configure input type.")

        response = self.device.query("RANGE?")  # Read the input range setting
        if response.strip() != "2":
            raise Exception("Failed to configure input range.")

        print(f"Connected to Lakeshore 224 at {self.address}")

    def configure_measurement(self, input_channel, temperature_range):
        """
        Configures the Lakeshore 224 for temperature measurement.

        :param input_channel: The input channel to configure (A, B, C, or D).
        :param temperature_range: The temperature range to use for the measurement.
        """
        self.device.write(f"INPUT {input_channel}")  # Set the input channel
        self.device.write("INTYPE K")  # Set the input type to K (thermocouple)
        self.device.write(f"RANGE {temperature_range}")  # Set the temperature range

        # Verify the configuration by querying the device
        response = self.device.query("INPUT?")  # Read the input channel setting
        if response.strip() != input_channel:
            raise Exception("Failed to configure input channel.")

        response = self.device.query("INTYPE?")  # Read the input type setting
        if response.strip() != "K":
            raise Exception("Failed to configure input type.")

        response = self.device.query("RANGE?")  # Read the temperature range setting
        if response.strip() != str(temperature_range):
            raise Exception("Failed to configure temperature range.")

    def get_temperature(self):
        """
        Acquires the temperature measurement from the Lakeshore 224.

        :return: The temperature measurement in Kelvin.
        """
        self.device.write("KRDG?")  # Send a command to read the temperature
        response = self.device.read()  # Read the response from the device
        return float(response)

    def disconnect(self):
        """
        Disconnects from the Lakeshore 224 device.
        """
        self.device.close()

    # Add additional methods as needed for other measurements or device functionality


if __name__ == '__main__':
    # Example usage
    tc = Lakeshore224(gpib_address=12)
    tc.connect()
    print(tc.get_temperature())
    tc.disconnect()


# Add more methods as needed for your project.
# To add a new method, define it in the class like the examples above.
# Be sure to include a docstring that explains what the method does,
# as well as any arguments it accepts and what it returns.
# Then, use the instrument's SCPI commands to implement the functionality.
# You can refer to the Lakeshore 224 manual for more information on the SCPI commands. 

# Users can add more methods as needed for other features or measurements.
# Here is an example template for a method that sets the temperature setpoint:
#
# def set_temperature_setpoint(self, temperature_setpoint):
#     """
#     Set the temperature setpoint.
#
#     Args:
#         temperature_setpoint (float): The desired temperature setpoint in Kelvin.
#     """
#     self.instrument.write(f"SETP {temperature_setpoint}")