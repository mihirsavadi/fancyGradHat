# fancyGradHat

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)  

**Project Status: Hardware not yet in hand. High level architecture, schematics, and PCB design sorted. RTL being written.**

It is tradition in the United States for undergraduates to wear a mortarboard (or square academic cap, graduate cap, oxford cap etc...its the one with the tassel dangling off it) during their graduation. My turn to wear one would be around May 2022. Im not sure how widespread this is throughout the country, but at Virginia Tech people typically decorate their hats as well depending on significant things they did in college or other messages or jokes they might want to display. I wanted to embed a discrete LED matrix under the hat's fabric that could display anything at will.

This has been done many times in the past by people from all over. What makes this project different however is that the entire system is on a single PCB, with no off-the-shelf LED panels or driving systems being used - the entire 'stack', from media input and formatting to LED matrix control hardware, is bespoke. I use 1024 individual 0805 LED's, which are commodity parts, arranged in a 32x32 grid. These are then driven by four [STMicroelectronic's STP16CPC26PTR LED Display Driver IC's](https://www.mouser.com/ProductDetail/STMicroelectronics/STP16CPC26PTR?qs=GkDVaEP5dcsHBCBm3pftPw%3D%3D). The FGPA in the [Arduino MKR VIDOR 4000](https://store.arduino.cc/usa/mkr-vidor-4000) runs custom RTL (register transfer level) that is used to drive these IC's, as well as interface the user input and other controls with a Microcontroller (which is also on-board the Arduino MKR VIDOR 4000). Details about the entire architecture can be found further below. The goal is to have a very thin, lightweight, independent, and power efficient system that can slip in between the mortarboard and top-fabric of a typical square 9.5"x9.5" graduation cap. The Arduino MKR VIDOR 4000 - the brains of the system - lends to these goals excellently, with tight integration of a multitude of features (including WiFi and Bluetooth connectivity) all of which are easy to use. It's Mini PCIE connector is especially exploited in this project.  



Going this route has a lot of tradeoffs - a lot more complexity; monochromic media only; relatively low resolution. But, given the cheapness of PCB fabrication and assembly services from jlcpcb.com and pcbway.com, and the use of mostly commodity parts, this approach is relatively cheaper. Also, because of the use of the FPGA, the entire Signal Processing architecture is extremely flexible, and the microcontroller is free to do a whole host of other tasks - all of which allow a huge margin for feature-expandability with no change in hardware. Finally, despite the significant extra complexity, I much prefer (and enjoy) the freedom of implementation and control, as opposed to having spend unreasonable amounts of time rummaging through opaque documentation of some one particular DSP microcontroller. I'm also fairly comfortable with digital design, and I have a year until I graduate and have complete this project. I don't anticipate this to be too painful. We'll see.  

## System Architecture



<!-- [This](https://nathanpetersen.com/2018/11/11/gradled-mini-prototype-modular-discrete-led-display/) project parallels this one quite a bit. Follow the USB and peripherals setup from here -->