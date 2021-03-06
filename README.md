<h1 align="center"> 
  <p>Raspberry Pi Pico CircuitPython projects</p>
  <img src="https://user-images.githubusercontent.com/44366184/145348534-7f5bd0f3-933b-49c3-9c08-f3fa1c076dc0.png" height="500"/>
</h1>

## Setup for all projects to work

1. Download [CircuitPython for the Raspberry Pi Pico](https://circuitpython.org/board/raspberry_pi_pico/). Or use `adafruit-circuitpython-raspberry_pi_pico-en_US-7.0.0.uf2` file from uf2 folder.

2. Plug the device into a USB port while holding the boot button. It will show up as a removable media device named `RPI-RP2`.

3. Copy the `.uf2` file to the root of the Pico (`RPI-RP2`). The device will reboot and after a second or so, it will reconnect as `CIRCUITPY`.

4. Download `adafruit-circuitpython-bundle-7.x-mpy-YYYYMMDD.zip` [here](https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/latest) and extract it outside the device. `Option 2`, use lib folder files.

5. Navigate to `lib` and copy `adafruit_hid` to the `lib` folder in your Raspberry Pi Pico.

## Extras
To restore your pico, use `flash_nuke.uf2` from uf2 folder. To be able to put uf2, hold `boot button` while connecting pico.
