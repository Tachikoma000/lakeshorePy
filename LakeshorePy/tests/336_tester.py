import pytest
from lakeshore_336 import Lakeshore336

@pytest.fixture(scope="module")
def ls336():
    """
    Fixture for the Lakeshore 336 class.
    """
    ls = Lakeshore336("GPIB0::1::INSTR")
    yield ls
    ls.disconnect()

def test_connect(ls336):
    """
    Test that the Lakeshore 336 can connect to the device.
    """
    ls336.connect()
    assert ls336.device.query("*IDN?") == "LSCI,MODEL336,12345,1.3\n"

def test_temperature(ls336):
    """
    Test acquiring temperature measurements from the Lakeshore 336.
    """
    temperature = ls336.get_temperature()
    assert isinstance(temperature, float)
    assert temperature >= 0.0

def test_setpoint(ls336):
    """
    Test setting and getting temperature setpoints on the Lakeshore 336.
    """
    ls336.set_setpoint(300.0)
    setpoint = ls336.get_setpoint()
    assert isinstance(setpoint, float)
    assert setpoint == 300.0
