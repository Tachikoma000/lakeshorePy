import pytest
from lakeshore_218 import Lakeshore218

class TestLakeshore218:
    def setup_class(self):
        # Create an instance of the Lakeshore218 class for testing
        self.ls = Lakeshore218("GPIB0::1::INSTR")

    def teardown_class(self):
        # Disconnect from the device after testing
        self.ls.disconnect()

    def test_connect(self):
        # Test the connection to the device
        self.ls.connect()
        assert self.ls.device.query("*IDN?") == "LSCI,MODEL218,12345,01.02.03\r\n"

    def test_get_temperature(self):
        # Test acquiring temperature measurement from the device
        temperature = self.ls.get_temperature()
        assert isinstance(temperature, float)

    def test_configure_measurement(self):
        # Test configuring the device for temperature measurement
        self.ls.configure_measurement()
        assert self.ls.device.query("KRDGTYPE?") == "K"

    # Add additional tests as needed for other methods or device functionality
