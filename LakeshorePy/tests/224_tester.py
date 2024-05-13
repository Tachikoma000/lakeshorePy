import pytest
from lakeshore_224 import Lakeshore224

@pytest.fixture(scope="module")
def ls():
    # Initialize a Lakeshore 224 object for testing
    ls = Lakeshore224("GPIB0::1::INSTR")
    ls.connect()
    yield ls
    ls.disconnect()

def test_connect(ls):
    # Test that the device is connected and responding to commands
    response = ls.device.query("*IDN?")
    assert "LSCI" in response

def test_temperature(ls):
    # Test that the device is able to acquire temperature readings
    temperature = ls.get_temperature()
    assert isinstance(temperature, float)

def test_configure_measurement(ls):
    # Test that the device is able to be configured for temperature measurement
    ls.configure_measurement()
    response = ls.device.query("KRDGTYPE?")
    assert response.strip() == "K"

# Add more tests as needed for additional functionality
