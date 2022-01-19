# Fun Raspberry Pi Pico Scripts
1. Drop `boot.py` into Pico main directory.
2. Drop `*.py` script and rename it to `code.py` for execution.
___

## Setup mode and mount as USB
To edit the `code.py`, enter setup mode by connecting the pin 1 (`GP0`) to pin 3 (`GND`), this will stop the pico from injecting the code in your own machine.
The easiest way to so is by using a jumper wire between those pins.

