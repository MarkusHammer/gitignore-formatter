# .gitignore Formatter

A simple CLI .gitignore formatter. Allows for the blank lines, comments, and paths in the file to be changed, removed or converted independently, allowing for quick editing of huge .gitignore files without the fuss.

## Setup
This module can be installed via pip. You can do so by typing in your terminal:

```pip install gitignoreformatter```

If not installed via pip, than the requirements for this script must be installed in the python environment. This script requires the ```argparse``` python module in order to run. This can also use the ```pathlib``` module optionally. These can be install using:

```pip install argparse pathlib```

## Command Options
Call the script by ```python -m gitignoreformatter FILEPATH``` or by downloading the ```gitignoreformatter.py``` file and running that with ```python ./gitignoreformatter.py FILEPATH```. ```FILEPATH``` is the path to the file you want to format. This is the only required argument; the rest, listed below, are optional.

NOTE: If the output file path is not set this writes back to the file path that was given as the input.

- ```-o FILEPATH``` or ```--out FILEPATH``` or ```--outfile FILEPATH``` changes the output destination to wherever the ```FILEPATH``` is. If this is not set this writes back to the path that was given as the input.

- ```-v``` or ```--verbose``` gives a verbose output of the process

- ```-c OPTION``` or  ```--comment OPTION``` or  ```--comments OPTION``` has the following set of valid OPTIONs:
  - ```Ignore``` leaves all the comments as they are
  - ```RemoveAll``` removes all comments from the file
  - ```RemoveRepeated``` removes any comments that are exctally the same, except for the first occurrence
  - ```MakeAllBlank``` turns all comment lines into blank lines

- ```-b OPTION``` or  ```--blank OPTION``` or  ```--blanks OPTION``` has the following set of valid OPTIONs:
  - ```Ignore``` leaves all the blank lines as they are
  - ```RemoveAll``` removes all blank lines from the file
  - ```RemoveRepeated``` removes any extra blank lines (any blank lines that come right after a blank line)
  - ```MakeAllComment``` turns all blank lines into empty comments (like ```#```)

- ```-p OPTION``` or  ```--path OPTION``` or  ```--paths OPTION``` has the following set of valid OPTIONs:
  - ```Ignore``` leaves all the paths as they are
  - ```RemoveAll``` removes all paths from the file (not recommended)
  - ```RemoveRepeated``` removes any paths that are exctally the same, except for the first occurrence
  - ```MakeAllBlank``` turns all path lines into blank lines
  - ```MakeAllComment``` comments out all the paths in the file

- ```--ver``` or ```--version``` prints the program version and then exits. You don't need a input file if you run this command.

- ```-h``` or ```--help``` prints some details about the programs arguments and then exits. You don't need a input file if you run this command.

- ```--git``` or ```--github``` prints a like to the github repository and then exits. You don't need a input file if you run this command.

## Licence
This is licenced under the Mozilla Public License 2.0 (MPL 2.0) Licence. See the ```Licence``` file in this repository for more information.

## Credits
This project uses the ```argparse``` and optionally ```pathlib``` modules, both very usefull python modules. Check them out if you want to make a simple CLI script like this, or for whatever else you might be up to in python.

While not required, feel free to credit "Markus Hammer" (or just "Markus") if you find this code or script usefull for whatever you may be doing with it.
