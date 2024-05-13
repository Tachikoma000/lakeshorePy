import pyvisa

class Lakeshore218:
    """
    A class for the Lakeshore 218 temperature monitor.

    This class handles connecting to the device, configuring measurements, and acquiring data.
    """

    def __init__(self, address):
        """
        Initializes the Lakeshore 218 instance.

        :param address: The GPIB address or IP address of the device.
        """
        self.address = address
        self.rm = pyvisa.ResourceManager()
        self.device = self.rm.open_resource(self.address)

    def connect(self):
        """
        Connects to the Lakeshore 218 device.
        """
        self.device.write("*RST")  # Reset the device
        self.device.write("KRDG?")  # Send a command to read the temperature
        response = self.device.read()  # Read the response from the device

        print(f"Connected to Lakeshore 218 at {self.address}. Temperature: {response}")

    def disconnect(self):
        """
        Disconnects from the Lakeshore 218 device.
        """
        self.device.close()

    def configure_measurement(self):
        """
        Configures the Lakeshore 218 for temperature measurement.
        """
        self.device.write("KRDGTYPE K")  # Set the temperature units to Kelvin

    def get_temperature(self):
        """
        Acquires the temperature measurement from the Lakeshore 218.

        :return: The temperature measurement in Kelvin.
        """
        self.device.write("KRDG?")  # Send a command to read the temperature
        response = self.device.read()  # Read the response from the device
        return float(response)

    # Add additional methods as needed for other measurements or device functionality

    # Add more methods as needed for your project.
    # To add a new method, define it in the class like the examples above.
    # Be sure to include a docstring that explains what the method does,
    # as well as any arguments it accepts and what it returns.
    # Then, use the instrument's SCPI commands to implement the functionality.
    # You can refer to the Lakeshore 218 manual for more information on the SCPI commands.

    # For example:
    # def set_setpoint(self, setpoint):
    #     """
    #     Sets the temperature setpoint of the Lakeshore 218.
    #
    #     :param setpoint: The desired temperature setpoint in Kelvin.
    #     """
    #     self.device.write(f"SETP {setpoint}")
    #
    # def get_setpoint(self):
    #     """
    #     Acquires the temperature setpoint of the Lakeshore 218.
    #
    #     :return: The temperature setpoint in Kelvin.
    #     """
    #     self.device.write("SETP?")  # Send a command to read the setpoint
    #     response = self.device.read()  # Read the response from the device
    #     return float(response)
