# TXT Terrain Generator
This is a simple project which can generate CIV like terrain in text form.
It can also export this generated terrain and its statistics to a txt File.

## Usage
This project does not require any 3rd party libraries for Python 3.
It can simply be executed by typing `python3 main.py`.

### Changing up the Parameters
Most of the Generators Parameters can be set right at the beginning of the file.
There are currently 5 Parameters:
* `size` The Size of the field. Which is the Square root of total Tiles you want.
* `forrestChance` The chance of a forest replacing a Normal Land Tile.
* `mountainChance` The chance of a mountain replacing a Normal Land Tile.
* `desertChance` The chance of a desert replacing a Normal Land Tile.
* `ravineChance` The chance of a ravine replacing a Normal Land Tile.

### Exporting Terrain
The terrain is exported by default. If you do not want this to occur,
change the variable `exportTerrainToTXT` from `True` to `False`.
The generated terrain will then be exported into the directory `exports`
where it can be found with a time stamp and the extension `pterrain`.

#### Errors when Exporting
One error that might occur is the
`FileNotFoundError: [Errno 2] No such file or directory: 'exports/<file>`
which can simply be fixed by creating a directory called `exports` in the root directory
of the project.

## PTerrain
PTerrain stands for "Python Terrain" and is a custom file format used by this generator.
It contains all information about the generated terrain, e.g. Its size, the terrain itself
 and the amount of tiles.
A Parser and Interpreter a currently worked on.

## License
This Project is lincesed under the BSD 3 Clause License, which can be found in the `LICENSE` file