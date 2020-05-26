# -*- coding: utf-8 -*-

from datetime import date
import time


def writeTerrainFile(finishedTerrain, landTotal, mountainTotal, forestTotal, waterTotal):
    timeStamp = str(date.today())+"-"+str(time.clock())

    # Create String to be written
    out = "LANDTOTAL {0} ; NORMALLAND {1} ; MOUNTAINTOTAL {2} ; FORESTTOTAL {3} ; WATERTOTAL {4} ;\n\n".format(landTotal+mountainTotal+forestTotal, landTotal, mountainTotal, forestTotal, waterTotal)

    out += finishedTerrain

    # Write variable out to TimeStamped file
    f = open("exports/terrain_{}.txt".format(timeStamp), "x", encoding="utf-8")
    f.write(out)
    f.close()
    print ("Terrain Exported!")