# -*- coding: utf-8 -*-

from datetime import date
import time
import terrainTypes

def writeTerrainFile(finishedTerrain, size, landTotal, mountainTotal, forestTotal, waterTotal, ravineTotal, desertTotal):
    timeStamp = str(date.today())+"-"+str(time.clock())

    # Create String to be written
    out = "█ TERRAIN TILE LEGEND: \n"
    for i in terrainTypes.terrainTypes:
        out += "█ " + i + " : " + terrainTypes.terrainLegend.get(i) + "\n"

    out += "\n"

    out += "LANDTOTAL {0} ; NORMALLAND {1} ; MOUNTAINTOTAL {2} ; FORESTTOTAL {3} ; DESERTTOTAL {4} ; RAVINETOTAL {5} ; WATERTOTAL {6} ;\n\n".format(
        landTotal+mountainTotal+forestTotal+ravineTotal+desertTotal, landTotal, mountainTotal, forestTotal, desertTotal, ravineTotal, waterTotal,)
    out += "SIZE {} ;\n\n".format(size)

    out += "TERRAIN START\n"
    out += finishedTerrain

    # Write variable out to TimeStamped file
    f = open("exports/terrain_{}.pterrain".format(timeStamp), "x", encoding="utf-8")
    f.write(out)
    f.close()
    print ("Terrain Exported!")