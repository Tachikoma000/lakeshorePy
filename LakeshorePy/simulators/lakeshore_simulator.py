import random
import time

class Lakeshore218Simulator:
    """
    A class for simulating the Lakeshore 218 temperature monitor.

    This class generates simulated temperature readings.
    """

    def __init__(self, min_temp=0, max_temp=100, delay=1):
        """
        Initializes the Lakeshore 218 simulator instance.

        :param min_temp: The minimum simulated temperature.
        :param max_temp: The maximum simulated temperature.
        :param delay: The delay between simulated temperature readings, in seconds.
        """
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.delay = delay

    def connect(self):
        """
        Connects to the Lakeshore 218 simulator.
        """
        print("Connected to Lakeshore 218 simulator.")

    def configure_measurement(self):
        """
        Configures the Lakeshore 218 simulator for temperature measurement.
        """
        pass

    def get_temperature(self):
        """
        Acquires a simulated temperature measurement from the Lakeshore 218 simulator.

        :return: A simulated temperature measurement in Kelvin.
        """
        temp = random.uniform(self.min_temp, self.max_temp)
        time.sleep(self.delay)
        return temp

    def disconnect(self):
        """
        Disconnects from the Lakeshore 218 simulator.
        """
        print("Disconnected from Lakeshore 218 simulator.")
