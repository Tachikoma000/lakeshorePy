import pyvisa

class Lakeshore336:
    """
    A class for the Lakeshore 336 temperature controller.

    This class handles connecting to the device, configuring measurements, and acquiring data.
    """

    def __init__(self, address):
        """
        Initializes the Lakeshore 336 instance.

        :param address: The GPIB address or IP address of the device.
        """
        self.address = address
        self.rm = pyvisa.ResourceManager()
        self.device = self.rm.open_resource(self.address)

    def connect(self):
        """
        Connects to the Lakeshore 336 device.
        """
        self.device.write("*RST")  # Reset the device
        self.device.write("KRDG? A")  # Send a command to read the temperature
        response = self.device.read()  # Read the response from the device

        print(f"Connected to Lakeshore 336 at {self.address}. Temperature: {response}")

    def configure_measurement(self):
        """
        Configures the Lakeshore 336 for temperature measurement.
        """
        self.device.write("KRDGTYPE K")  # Set the temperature units to Kelvin

    def get_temperature(self):
        """
        Acquires the temperature measurement from the Lakeshore 336.

        :return: The temperature measurement in Kelvin.
        """
        self.device.write("KRDG? A")  # Send a command to read the temperature
        response = self.device.read()  # Read the response from the device
        return float(response)

    # Add additional methods as needed for other measurements or device functionality

    def set_setpoint(self, setpoint):
        """
        Sets the temperature setpoint of the Lakeshore 336.

        :param setpoint: The desired temperature setpoint in Kelvin.
        """
        self.device.write(f"SETP 1,{setpoint}")

    def get_setpoint(self):
        """
        Acquires the temperature setpoint of the Lakeshore 336.

        :return: The temperature setpoint in Kelvin.
        """
        self.device.write("SETP? 1")  # Send a command to read the setpoint
        response = self.device.read()  # Read the response from the device
        return float(response)

    def set_output_range(self, output_range):
        """
        Sets the output range of the Lakeshore 336.

        :param output_range: The desired output range in Kelvin.
        """
        self.device.write(f"RANGE 1,{output_range}")

    def get_output_range(self):
        """
        Acquires the output range of the Lakeshore 336.

        :return: The output range in Kelvin.
        """
        self.device.write("RANGE? 1")  # Send a command to read the output range
        response = self.device.read()  # Read the response from the device
        return float(response)

    def disconnect(self):
        """
        Disconnects from the Lakeshore 336 device.
        """
        self.device.close()
        print(f"Disconnected from Lakeshore 336 at {self.address}")


if __name__ == '__main__':
    # Example usage
    ls336 = Lakeshore336("GPIB0::1::INSTR")
    temp = ls336.get_temperature()
    print(f"Temperature: {temp} K")
    
    # Add more methods as needed for your project.
    # To add a new method, define it in the class like the examples above.
    # Be sure to include a docstring that explains what the method does,
    # as well as any arguments it accepts and what it returns.
    # Then, use the instrument's SCPI commands to implement the functionality.
    # You can refer to the Lakeshore 336 manual for more information on the SCPI commands.
    
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
