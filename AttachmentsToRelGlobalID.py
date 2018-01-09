import arcpy
from arcpy import da
import os

inTable = arcpy.GetParameterAsText(0)
fileLocation = arcpy.GetParameterAsText(1)

with da.SearchCursor(inTable, ['DATA', 'GLOBALID', 'REL_GLOBALID', 'ATT_NAME']) as cursor:
    for item in cursor:
        attachment = item[0]
        filenum = str(item[2])
        filename = filenum + "_" + str(item[1]) + "_" + str(item[3])
        open(fileLocation + os.sep + filename, 'wb').write(attachment.tobytes())
        del item
        del filenum
        del filename
        del attachment
