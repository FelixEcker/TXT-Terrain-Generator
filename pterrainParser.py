# -*- coding: utf-8 -*-

#######################################
# PTerrain Parser 1.0 by Felix Eckert #
# Copyright (c) 2020 Felix Eckert     #
# This Project is lincesed under the  #
# 3 Clause BSD License                #
#######################################
# The Parser standard config is set   #
# for the TXT Terrain Gen Project.    #
# If you wish to apply this parser to #
# your custom map, change the list    #
# "terrainDataKeys" to only include   #
# the data keys you put into your     #
# pterrain file!                      #
#######################################

terrainDataKeys = ["LANDTOTAL",
                   "NORMALLAND" ,
                   "MOUNTAINTOTAL",
                   "FORESTTOTAL",
                   "DESERTTOTAL",
                   "RAVINETOTAL",
                   "WATERTOTAL"
                   ]

def main():
    print ("PTerrain Parser 1.0 Information")
    print ("""
#######################################
# PTerrain Parser 1.0 by Felix Eckert #
# Copyright (c) 2020 Felix Eckert     #
# This Project is lincesed under the  #
# 3 Clause BSD License                #
#######################################
# The Parser standard config is set   #
# for the TXT Terrain Gen Project.    #
# If you wish to apply this parser to #
# your custom map, change the list    #
# "terrainDataKeys" to only include   #
# the data keys you put into your     #
# pterrain file!                      #
#######################################
""")
    

def parseTerrainFile(name):
    print ("Parsing "+name)
    
    f = open(name, "r").read()
    pterrainSplit = f.split(";")
    cleanedPTerrainSplit = []
    for i in pterrainSplit:
        if not i == pterrainSplit[0]:
            cleanedPTerrainSplit.append(i)

    terrainMap = []
    terrainMapLocation = 0
    terrainStartKey = ""

    terrainData = []

    c = 0

    print ("Parsing Terrain Information and Searching for Terrain Map Start...")
    for i in cleanedPTerrainSplit:
        if "TERRAIN START" in i:
            print ("Found Terrain Map Start! (C {})".format(c))
            terrainMapLocation = c
            terrainStartKey = i
            break

        for j in terrainDataKeys:
              if j in i:
                  print ("Found Terrain Information! (C {})".format(c))
                  j = i.replace(j, '')
                  j = j.replace(' ', '')
                  terrainData.append(j)

        c += 1

    for i in range(terrainMapLocation, len(cleanedPTerrainSplit)):
        terrainMap.append(cleanedPTerrainSplit[i])


    terrainMap[0] = terrainMap[0].replace("TERRAIN START", '')
    terrainMap[0] = terrainMap[0].replace("\n", '')

    print  ("Finished Parsing!")
    print  ("#################")
    print  ("Retrieved Data: ")
    print  (terrainData)
    print  (terrainMap)
    return [terrainData, terrainMap]
            

if __name__ == "__main__":
    main()
