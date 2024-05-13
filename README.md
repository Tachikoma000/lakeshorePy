# LakeshorePy
LakeshorePy is a lightweight Python package for interfacing with and acquiring data from Lakeshore temperature monitors. It uses pyVISA to communicate with the instruments and provides a simple and cookie-cutter structure that can be extended for future models.

For questions or feature requests, please contact 0xtachi@gmail.com. As an independent researcher, I built this project purely for the joy of creating something both enjoyable and practical. If you love to tinker and build innovative control systems, feel free to email me!

## Table of Contents

- [LakeshorePy](#lakeshorepy)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Classes and Methods](#classes-and-methods)
    - [Lakeshore 218](#lakeshore-218)
    - [Lakeshore 224](#lakeshore-224)
    - [Lakeshore 336](#lakeshore-336)
  - [Contributing](#contributing)
  - [License](#license)

## Installation

1. Clone the LakeshorePy repository to your local machine.
2. Create a virtual environment for the project: `python3 -m venv env`
3. Activate the virtual environment: `source env/bin/activate`
4. Install the required libraries: `pip install -r requirements.txt`

## Usage

To use LakeshorePy, follow these steps:

1. Connect your Lakeshore device to your computer via GPIB or Ethernet.
2. Import the desired Lakeshore module: `from lakeshore_218 import Lakeshore218`
3. Initialize a new instance of the class: `ls = Lakeshore218("GPIB0::1::INSTR")`
4. Connect to the device: `ls.connect()`
5. Configure the measurement: `ls.configure_measurement()`
6. Acquire the desired measurement: `temperature = ls.get_temperature()`
7. Disconnect from the device: `ls.disconnect()`

## Classes and Methods

### Lakeshore 218

The `Lakeshore218` class includes the following methods:

- `__init__(self, address)` - Initializes the Lakeshore 218 instance.
- `connect(self)` - Connects to the Lakeshore 218 device.
- `disconnect(self)` - Disconnects from the Lakeshore 218 device.
- `configure_measurement(self)` - Configures the Lakeshore 218 for temperature measurement.
- `get_temperature(self)` - Acquires the temperature measurement from the Lakeshore 218.

### Lakeshore 224

The `Lakeshore224` class includes the following methods:

- `__init__(self, address)` - Initializes the Lakeshore 224 instance.
- `connect(self)` - Connects to the Lakeshore 224 device.
- `disconnect(self)` - Disconnects from the Lakeshore 224 device.
- `configure_measurement(self, channel)` - Configures the Lakeshore 224 for temperature measurement.
- `get_temperature(self, channel)` - Acquires the temperature measurement from the Lakeshore 224.

### Lakeshore 336

The `Lakeshore336` class includes the following methods:

- `__init__(self, address)` - Initializes the Lakeshore 336 instance.
- `connect(self)` - Connects to the Lakeshore 336 device.
- `disconnect(self)` - Disconnects from the Lakeshore 336 device.
- `set_input(self, input_number, sensor_type)` - Configures the input sensor type on the Lakeshore 336.
- `get_input(self, input_number)` - Acquires the temperature measurement from the specified input on the Lakeshore 336.

## Contributing

Contributions to LakeshorePy are welcome! If you find a bug or have a suggestion for a new feature, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
