"""
    exec(open('C:/Users/m_sav/Documents/SchoolandWork/Projects/fancyGradCap/pcb_resources/fancyGradCap_rev2/placeMatrix.py').read())
"""

import enum
import s_expression_parser

import uuid # to create new part id's by using uuid.uuid4

############### HELPER FUNCTIONS
def getNetNumber(netName: str, pcbFileDir: str) -> int:
    file = open(pcbTextFileDir, "r")
    file_lines = file.readlines()

    netNumber = -1
    for line in file_lines:
        if netName in line:
            lineAsList = line.split()
            netNumber = lineAsList[1]
            break

    return netNumber

###############

if __name__ == '__main__':

    # Parse the pcb text file and organize all LED items into a list of dictionaries, where each dictionary contains the 
    # the LED's refDes, and line number in the file that corresponds to the "(at 250.952 56.134)" line.
    pcbTextFileDir = "C:/Users/m_sav/Documents/SchoolandWork/Projects/fancyGradCap/pcb_resources/fancyGradCap_rev2/fancyGradCap_rev2.kicad_pcb"
    file = open(pcbTextFileDir, "r")
    file_lines = file.readlines()

    LED_parts_dict = {}
    for i, line in enumerate(file_lines):
        if '(footprint "LED_SMD:LED_0603_1608Metric_Pad1.05x0.95mm_HandSolder" (layer "F.Cu")' in line:

            # print(f'idx: {i}, line: {line}')
            # print(f'Position = {file_lines[i+2]}')
            # print(f'RefDes = {file_lines[i+9].split()[2]}')
            refdes = file_lines[i+9].split()[2].replace('"', '')
            refdes = refdes.replace('"', '')

            LED_dict = {
                "titleLineNo.": i,
                "posLineNo.": i+2,
                "refdesLineNo.": i+9,
                "posLine": file_lines[i+2],
                "newPosLine": ""
            }
            LED_parts_dict[refdes] = LED_dict

    file.close()

    # Now run through the LED_parts_dict list, and alter the PCB file so that the LED's are arranged in a grid order.
    # All calculations are done programatically. Origin is top left with positive going right and down.

    #   set constants
    LED_arrangement = 32 # must be square
    totalLEDs = LED_arrangement**2
    boardWidth = 200
    pitch = 5

    #   set variables
    topLeftCoord = (((200-(LED_arrangement*pitch))/2)+(pitch/2), 6.35)

    #   run loop to start assigning values to LED_parts_dict, and re assign to pcb text file.
    for i in range(1, (LED_arrangement**2)+1):
        target_refdes = f'D{i}'
        target_refdes_col = (i-1)%LED_arrangement
        target_refdes_row = (int((i-1)/LED_arrangement))

        dict_item_posline = LED_parts_dict[target_refdes]['posLine'].replace(")", '')
        dict_item_posline_list = dict_item_posline.split()

        currentCoord = (float(dict_item_posline_list[1]), float(dict_item_posline_list[2]))

        newX = target_refdes_col*pitch + topLeftCoord[0]
        newY = target_refdes_row*pitch + topLeftCoord[1]

        LED_parts_dict[target_refdes]['newPosLine'] = f"    (at {newX} {newY})\n"

        # append new information to specific line in file lines
        file_lines[LED_parts_dict[target_refdes]['posLineNo.']] = LED_parts_dict[target_refdes]['newPosLine']

        # place a new via in the appropriate position next to target LED, and add to pcb text file
        newUUID_1 = str(uuid.uuid4())
        newUUID_2 = str(uuid.uuid4())
        netNumber = getNetNumber(f'vout_row{target_refdes_row+1}', pcbTextFileDir)
        newLine = \
            f"""  (via (at {newX-2.5} {newY}) (size 0.8) (drill 0.4) (layers "F.Cu" "B.Cu") (free) (net {netNumber}) (tstamp {newUUID_1}))\n  (segment (start {newX-2.5} {newY}) (end {newX-0.875} {newY}) (width 0.25) (layer "F.Cu") (net {netNumber}) (tstamp {newUUID_2}))\n"""
        file_lines.insert(-2, newLine)
        print(f'%Done = {round( (i/totalLEDs)*100, 2)}, idx: {i}/{totalLEDs}')

    # edit pcb text file with new file lines
    file = open(pcbTextFileDir, 'w')
    file.writelines(file_lines)
    file.close()


    # If you want to, run through LED_parts_dict again and add connected nets and viasgain appropriately.