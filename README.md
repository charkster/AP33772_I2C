# AP33772_I2C

![picture](https://cdn1-shop.mikroe.com/img/product/usb-c-sink-2-click/usb-c-sink-2-click-large_default-1.jpg)

Python driver for [Mikroe USB-C Sink 2 Click](https://www.mikroe.com/usb-c-sink-2-click) board which uses [AP33772](https://www.diodes.com/assets/Evaluation-Boards/AP33772-Sink-Controller-EVB-User-Guide.pdf) to query and control USB PD 3.0 wall adapter. Works on Raspberry Pi and MicroPython. For offical C language support check [here](https://github.com/MikroElektronika/mikrosdk_click_v2/tree/master/clicks/usbcsink2)

I am able to query a USB PD wall adapater and request a specific PDO (including PPS!!). The board costs [$15 from Digikey](https://www.digikey.com/en/products/detail/mikroelektronika/MIKROE-5792/21326383).

Four board connections are needed on the Mikroe board: GND, 3V3 (connects to MCU gpio, not 3.3V rail), SDA and SCL. 

There are [4.7k Ohm I2C pullups](https://download.mikroe.com/documents/add-on-boards/click/usb-c-sink-2-click/usb-c_sink_2_click_v100_Schematic.PDF) already on the Mikroe board. I run the I2C at 100kHz (4.7k Ohms is too large for 400kHz or faster). 

When I powered the Mikroe board's 3V3 pin using a constant 3.3V rail, I was not able to reset the I2C interface (which is needed from time to time). 

The AP33772 needs power from the USB PD wall adapter cable in order to respond to I2C (the 3V3 is for communication only). 
The AN pin is a [7.32 : 1 resistor divider](https://download.mikroe.com/documents/add-on-boards/click/usb-c-sink-2-click/usb-c_sink_2_click_v100_Schematic.PDF) of VBUS (VBUS=20V has AN=2.73V). If you are going to read the AN pin with an ADC, the reference should allow for 2.73V measurements.

The LED labeled "FAULT" is powered by GPIO4, which isn't the interrupt pin (GPIO3). When it is solid (not flashing) it is just an indicator that VSINK (VOUT) is valid and being driven through the protection FETs with a current less than 500mA.


**FAULT LED flickering notified of the system status:**
- Charging: Breathing light (2 sec dimming), 1 cycle is 4 sec.
- Fully charged: Continuously lit Charging current < 500mA.
- Mismatch: 1s flicker Voltage or power mismatch. Non-PD power source, 1 cycle is 2sec.
- Fault: 300ms flicker OVP, 1 cycle is 600ms.
