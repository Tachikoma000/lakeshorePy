from lakeshore_218 import Lakeshore218


# Example for GPIB connection:
ls = Lakeshore218("GPIB0::1::INSTR")
ls.connect()

# Example for Ethernet connection:
ls = Lakeshore218("TCPIP::192.168.1.1::INSTR")
ls.connect()


temperature = ls.get_temperature()
print(f"Temperature: {temperature} K")
