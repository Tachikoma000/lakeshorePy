from lakeshore_224 import Lakeshore224

ls = Lakeshore224("GPIB0::1::INSTR")
ls.connect()
ls.configure_measurement()
temp = ls.get_temperature()
print(f"Temperature: {temp} K")


ls = Lakeshore224("TCPIP::192.168.1.1::INSTR")
ls.connect()
ls.configure_measurement()
temp = ls.get_temperature()
print(f"Temperature: {temp} K")
