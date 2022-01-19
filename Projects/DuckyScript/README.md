
<h1 align="center"> 
  <p>Raspberry Pi Pico Ducky</p>
<img src="https://user-images.githubusercontent.com/44366184/145346110-89d29bc8-0b55-43d5-a325-478492ba117d.png" height="500" />
</h1>

## Install

1. Copy `boot.py` to the main directory.

2. Copy `code.py` to the main directory.

3. Create / copy payload file and make sure it's named `payload.dd`

___

## Setup mode

To edit the payload, enter setup mode by connecting the pin 1 (`GP0`) to pin 3 (`GND`), this will stop the pico from injecting the payload in your own machine.
The easiest way to so is by using a jumper wire between those pins as seen bellow.

## USB disable mode

If you need the pico to not show up as a USB mass storage device for stealth, 
connect a jumper wire between pin `18` and pin `20`.
This will prevent the pico-ducky from showing up as a USB drive when plugged into the target computer.  
