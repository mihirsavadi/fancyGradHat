# fancyGradHat

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)  

Undergraduates in the US typically wear a mortarboard (or square academic cap, graduate cap, oxford cap etc...its the one with the tassel dangling off it) during their graduation. My turn to wear one would be around May 2022. At Virginia Tech people typically decorate their hats depending on significant things they did in college or other messages or jokes they might want to display. I wanted to embed a discrete LED matrix under the hat's fabric that could display anything at will.

This has been done many times in the past by people from all over. What makes this project different however is that the entire system is on a single PCB, with no off-the-shelf LED panels or other controls systems being used. The entire 'stack' - from media input and formatting to LED matrix control hardware - is built from the ground up. I use 1024 individual 0805 LED's, which are commodity parts, arranged in a 32x32 grid. These are then driven by a set of 8 bit shift registers. There are currently two revisions: rev1 was based on an FPGA but had flawed 2 layer board design that would have resulted in a host of EMI issues and ultimately non-functionality; rev2 was a ground-up 4-layer redesign based off the RP2040 microcontroller from Raspberry Pi. Rev2 is probably one of my nicest PCB designs to date. rev2 was also done in KiCAD whilst rev1 was done in Diptrace -- I was prompted to make the switch due to the new KiCAD 6.0 release which made it an absolute powerhouse. I also redid the BOM in rev2 to make the most out of the chip shortage -- i.e. there are no weird rare components and most IC's are readily available generic parts.

**NOTE:**

See ./wiki/rev1_design.md for a copy paste of the old README that I wrote when the only revision was rev1. See ./wiki/rev2_design.md for some images of the 3D renderings for rev2 -- I'm too lazy to do a whole write up of rev2, but the design is complete and comprehensive (given no post build testing), with all the design files available in ./pcb_resources/fancyGradCap_rev2, including a pdf of the schematic (which is extremely well commented). This documentation should be sufficient to explain the functionality of everything.

After much sadness I decided to ultimately drop this project primarily due to the cost of parts and ordering the board. Additionally I re-evaluated the amount of time I have to totally flesh out the project before my graduation commencement day and it was not shaping out to be very practical. I might pick this back up after I start work post August 2022 however. Until then, the rev2 hardware is pretty much ready to go.

Below are some images from rev2 :

![alt text](./pics_vids_figures/rev2_1.jpg)
![alt text](./pics_vids_figures/rev2_2.jpg)
![alt text](./pics_vids_figures/rev2_3.jpg)
![alt text](./pics_vids_figures/rev2_4.jpg)