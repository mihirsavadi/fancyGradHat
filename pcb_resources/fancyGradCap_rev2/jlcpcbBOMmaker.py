
import enum


originalBOMdir = 'C:/Users/m_sav/Documents/SchoolandWork/Projects/fancyGradCap/pcb_resources/fancyGradCap_rev2/fancyGradCap_rev2_BOM.csv'

file = open(originalBOMdir, "r")
file_lines = file.readlines()

finalFile = []
finalFile.append('Comment, Designator, Footprint, Quantity, Supplier and Reference')
for i, line in enumerate(file_lines):

    if i < 4:
        continue

    strAsList = line.split(';')
    
    comment = strAsList[4][1:-1]

    # refdes = strAsList[1][1:-1].replace(',', ' ')
    refdes = strAsList[1][1:-1]
    letter = refdes[0]
    refDesList = []
    refDesItem = ''
    for char in refdes:
        if char == ',':
            refDesList.append(int(refDesItem))
            refDesItem = ''
        elif char in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            refDesItem += char
    refDesList.sort()
    newrefDesList = []
    for item in refDesList:
        newrefDesList.append(letter+str(item))
    refdes = " ".join(newrefDesList)

    footprint = strAsList[2][1:-1]
    qty = strAsList[3]
    supplier = strAsList[5]

    finalFile.append(f'{comment}, {refdes}, {footprint}, {qty}, {supplier}')

file.close()

file = open('jlcpcbAssemblyBOM.csv', 'w')
for line in finalFile:
    file.write(line + '\n')

file.close()