# TXT Terrain Generator
This is a simple project which can generate CIV like terrain in text form.
It can also export this generated terrain and its statistics to a txt File.

## Usage
This project does not require any 3rd party libraries for Python 3.
It can simply be executed by typing `python3 main.py`.

### Changing up the Parameters
Most of the Generators Parameters can be set right at the beginning of the file.
There are currently 3 Parameters:
* `size` The Size of the field. Which is the Square root of total Tiles you want.
* `forrestChance` The chance of a forest replacing a Normal Land Tile.
* `mountainChance` The chance of a mountain replacing a Normal Land Tile.

### Exporting Terrain
The terrain is exported by default. If you do not want this to occur,
change the variable `exportTerrainToTXT` from `True` to `False`.

#### Errors when Exporting
One error that might occur is the
`FileNotFoundError: [Errno 2] No such file or directory: 'exports/<file>`
which can simply be fixed by creating a directory called `exports` in the root directory
of the project.

## License
This Project is lincesed under the BSD 3 Clause License, which can be found in the `LICENSE` file