from lakeshore_336 import Lakeshore336

ls = Lakeshore336("GPIB0::1::INSTR")
ls = Lakeshore336("TCPIP::192.168.1.1::INSTR")
ls.connect()
ls.configure_measurement()

temperature = ls.get_temperature()
print(f"Temperature: {temperature} K")

ls.set_setpoint(273.15)
setpoint = ls.get_setpoint()
print(f"Setpoint: {setpoint} K")

ls
