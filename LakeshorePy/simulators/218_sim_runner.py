from lakeshore_simulator import Lakeshore218Simulator

# Instantiate the simulator with a sample temperature of 300 K
simulator = Lakeshore218Simulator(300)

# Connect to the simulator and configure measurement settings
simulator.connect()
simulator.configure_measurement()

# Acquire the temperature measurement and print it
temperature = simulator.get_temperature()
print(f"Temperature: {temperature} K")

# Disconnect from the simulator
simulator.disconnect()
