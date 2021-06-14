# fancyGradHat

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)  

It is tradition in the United States for undergraduates to wear a mortarboard (or square academic cap, graduate cap, oxford cap etc...its the one with the tassel dangling off it) during their graduation. My turn to wear one would be around May 2022. Im not sure how widespread this is throughout the country, but at Virginia Tech people typically decorate their hats as well depending on significant things they did in college or other messages or jokes they might want to display. I wanted to embed a discrete LED matrix under the hat's fabric that could display anything at will.

Because of the large amount of time I have before I start, I wanted a bit of a challenge. I started mocking up schematics for discrete Red, Green, and Blue 0805 SMD LED's in a grid-array on a single PCB with multiplexed controls. However, to even achieve a 32x32 pixel resolution would require soldering 3072 LED's, not to mention the same amount of current limiting resistors. A 64x64 resolution would have been even more taxing: 12288 LED's. The cost of this would have also been impractical even if I had a unit price of around $0.02 or less from lcsc.com or some other chinese mass distributer. Each individual LED would also require some structure to limit its field of view or radiation angle to not be almost 180 degrees, which it would be if I used standard SMD LED's - this would also require lots of time and effort to figure out and implement for each and every LED. Additionally, I would need to put in significant effort learning the nitty gritties of the interrupt and timing controls for any one particular microcontroller (which I don't like doing); or (and this is what I probably would have done) get a small FPGA board and write my own DSP hardware accelerator and interface with it via a microcontroller. Either option would have been expensive in terms of money and/or time. If I had unreasonable amounts of money and time, I would definitely still do this, but unfortunately being an undergrad I have neither, even despite starting this project a year before its intended delivery.

So instead I just opted to get a 32x32 off-the-shelf LED matrix from adafruit, a teensy 4.0, the SmartMatrix SmartLED shield for the Teensy 4.0, and make the whole thing mostly a software project, all for under $150. Abstraction truly is a marvelous thing. I do however want to integrate a battery power and charging management circuitry within the cap assembly, as well as some way to manipulate the display - either via accessible buttons (which would provide limited functionality), or integrate an ESP32 which would host a server broadcasted over its own local WiFi network which I would use to command the Teensy4.0 via my phone or whatever else.  

Work for this is still in progress, so please forgive the general emptiness of this repository.  

[This](https://nathanpetersen.com/2018/11/11/gradled-mini-prototype-modular-discrete-led-display/) project parallels this one quite a bit. Follow the USB and peripherals setup from here


Alternative idea, cos who cares about features i just want this to be cool:
- use this fpga https://numato.com/product/mimas-spartan-6-fpga-development-board/
- get 1024 of these led's for a 32x32 grid https://lcsc.com/product-detail/Light-Emitting-Diodes-LED_0805-Red-LED-Iv-61mcd-Typ-atIF-20mA_C72037.html
- use x2 of these cool shift register led driver thing - it controls negative end of each row, u drive top mosfet circuitry - https://www.mouser.com/ProductDetail/STMicroelectronics/STP16CPC26PTR?qs=GkDVaEP5dcsHBCBm3pftPw%3D%3D
- use these 1A P channel mosfets to control the positive rail. needs to be p channel since positive rail (high side) is switched, while the led driver controls low side check if already have (https://lcsc.com/product-detail/MOSFET_TOSHIBA_SSM3J338R-LF_TOSHIBA-SSM3J338R-LF_C146352.html)
- add a teensy, esp32 or other microcontroller. This will connect to user interface and memory, like an sd card or wtvr. When user selects new image or video, it will prompt fpga that will load new data into itself and display it (or on loop if its a gif or whatever). Need to figure out encoding of data, and a python or wtvr that can decode images into this encoded data.
- USE RP2040 Microcontroller!!!!!! Use one core to control matrix and other core to do other shit like deal with fetching data etc
- use this shift register for each of the columns!!! https://www.mouser.com/ProductDetail/STMicroelectronics/HCF4021YM013TR?qs=wkiPY8TIIKfARqeH6MSyJw%3D%3D that way can use microcontroller!!

[ignore below]
use a bunch of these muxes maybe? if needed idk: https://www.mouser.com/ProductDetail/Texas-Instruments/MUX506IDWR?qs=7EBvPakHacVyv2nASLrMzg%3D%3D

