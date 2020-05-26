import random
import re

import terrainExporter
import terrainTypes

# General Config
exportTerrainToTXT = True

# Generator Parameters
size           = 64 # Size of the Terrain to be generated
forestChance   = 20 # Chance of Forests Replacing a normal land tile
mountainChance = 80 # Chance of Mountains Replacing a normal land tile
desertChance   = 100 # Chance of a Desert Replacing a normal land tile
ravineChance   = 200 # Chance of a Ravine Replacing a normal land tile

# Statistics
landTotal     = 0
forestTotal   = 0
mountainTotal = 0
desertTotal   = 0
ravineTotal   = 0
waterTotal    = 0

# Important Variables for Generation
totalSize        = size*size
baseField        = ""
tiles            = terrainTypes.terrainTypes
generatedTileArr = []

finishedTerrain  = ""

def main():
    global finishedTerrain, landTotal, mountainTotal, forestTotal, waterTotal, desertTotal, ravineTotal
    print ("ASCII Terrain Generator by Felix Eckert")
    print ("Starting Generation...")
    startGeneration()
    print ("Cleaning Terrain Up...")
    newTerrainArray = cleanupTerrain()

    finishedTerrain = re.sub("(.{" + str(size) + "})", "\\1\n", ''.join(newTerrainArray), 0, re.DOTALL)

    if exportTerrainToTXT:
        print ("Exporting...")
        terrainExporter.writeTerrainFile(finishedTerrain, size, landTotal, mountainTotal, forestTotal, waterTotal, ravineTotal, desertTotal)
        print ()

    print("Statistics:")
    print("[Land Total] " + str(landTotal + mountainTotal + forestTotal + ravineTotal + desertTotal))
    print(" [Normal " + str(landTotal))
    print(" [Forests] " + str(forestTotal))
    print(" [Mountains] " + str(mountainTotal))
    print(" [Deserts] "+str(desertTotal))
    print(" [Ravines] "+str(ravineTotal))
    print("[Water Total] " + str(waterTotal))
    print()
    print ("Terrain Legend: ")
    for i in tiles:
        print (i + " : " + terrainTypes.terrainLegend.get(i))
    print("====================")
    print()
    print(finishedTerrain)


def startGeneration():
    previousTile = ""
    landCount    = 0
    waterCount   = 0
    row          = 0

    # Generate the Base Field with Randoms
    for i in range(totalSize):
        global waterTotal, landTotal, forestTotal, mountainTotal, generatedTileArr, desertTotal, ravineTotal
        row += 1

        tile = random.randint(0, 1) # Generate Random Tile (Water or Land)

        # Increment the aprropriate Counters for the Tile
        if tile == 0: # Water Counters
            waterCount += 1
            waterTotal += 1
        else: # Land Counters
            landCount += 1
            landTotal += 1

        # Change up the Tile if the tile counter matches the random number
        if waterCount == random.randint(2,size/2):
                waterCount = 0 # Reset the Water Counter
                tile = 1      # Set the Tile to land

        if landCount == random.randint(4,size-4):
                landCount = 0 # Reset the Land Counter
                tile = 0      # Set the Tile to Water

        # If its a Land Tile, run it through these if statements to (potentially) make it a forrest or a mountain
        if tile == 1:
            if random.randint(1, mountainChance) == mountainChance:  # Mountains
                tile = 2
                mountainTotal += 1
            elif random.randint(1, forestChance) == forestChance:  # Forests
                tile = 3
                forestTotal += 1
            elif random.randint(1, desertChance) == desertChance: # Deserts
                tile = 4
                desertTotal += 1
            elif random.randint(1, ravineChance) == ravineChance: # Ravines
                tile = 5
                ravineTotal += 1


        generatedTileArr.append(tiles[tile]) # Append the now Finished tile to the geenerated tile array.


# Used to Clean Up the terrain (removes water with land on both of its sides)
def cleanupTerrain():
    global waterTotal, landTotal, forestTotal, mountainTotal, generatedTileArr

    lastfield = ""
    c = 0
    nextfield = ""
    newfieldarr = [""] * (size * size)
    for i in generatedTileArr:
        if c == 0:  # If its the first field, do nothing and just continue
            lastfield = i
            newfieldarr[c] = i
            c += 1
            continue
        elif c < (size * size) - 1:  # Check if its the last field or not
            nextfield = generatedTileArr[c + 1]
            if nextfield == "#" and lastfield == "#" and i == "~":  # If a water field has Land on the left and right, make it land
                newfieldarr[c] = "#"  # update water field
                lastfield = "#"  # change last field
                waterTotal -= 1  # reduce water count
                landTotal  += 1  # increment land count
            else:  # Just add the current field as the last field and add it to the newfield array
                lastfield = i
                newfieldarr[c] = i
        else:
            newfieldarr[c - 1] = i
        c += 1  # increment counter

    return newfieldarr


if __name__ == "__main__":
    main()
