# AP33772_I2C

![picture](https://cdn1-shop.mikroe.com/img/product/usb-c-sink-2-click/usb-c-sink-2-click-large_default-1.jpg)

Python driver for [Mikroe USB-C Sink 2 Click](https://www.mikroe.com/usb-c-sink-2-click) board which uses [AP33772](https://www.diodes.com/assets/Evaluation-Boards/AP33772-Sink-Controller-EVB-User-Guide.pdf) to query and control USB PD 3.0 wall adapter. Works on Raspberry Pi and MicroPython.

I am able to query a USB PD wall adapater and request a specific PDO (including PPS!!). The board costs [$15 from Digikey](https://www.digikey.com/en/products/detail/mikroelektronika/MIKROE-5792/21326383).

Four board connection are needed on the Mikroe board: GND, 3V3 (connects to MCU gpio, not 3.3V rail), SDA and SCL. 

There are [4.7k Ohm I2C pullups](https://download.mikroe.com/documents/add-on-boards/click/usb-c-sink-2-click/usb-c_sink_2_click_v100_Schematic.PDF) already on the Mikroe board. I run the I2C at 100kHz (4.7k Ohms is too large for 400kHz or faster). 

When I powered the Mikroe board's 3V3 pin using a constant 3.3V rail, I was not able to reset the I2C interface (which is needed from time to time). 

The AP33772 needs power from the USB PD wall adapter cable in order to respond to I2C (the 3V3 is for communication only). 
