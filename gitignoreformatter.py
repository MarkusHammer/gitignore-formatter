'''
.gitignore formatter
By Markus Hammer 2022

Licenced under the Mozilla Public License 2.0 (MPL 2.0)

See the github repo for more info!
https://github.com/MarkusHammer/gitignore-formatter
'''

import argparse
from sys import exit

def __main__():
    parser = argparse.ArgumentParser(description='A basic CLI program that allows for quick formatting of a .gitignore file')
    parser.add_argument('inFilePath', action='store', help='The input filepath')
    parser.add_argument('-o','--out', '--outfile', dest='outFilePath', action='store', default=None,
                        help='The output filepath, if not set, it defaults to the overwriting the input file')
    parser.add_argument('-v', '--verbose', dest='verbose', action='store_true', default=False,
                        help="Print a verbose output of the process")
    parser.add_argument('-c', '--comment', '--comments', dest='comments', action='store', default="Ignore",
                        choices=["RemoveAll", "Ignore", "RemoveRepeated", "MakeAllBlank"],
                        help="What should be done to the comments")
    parser.add_argument('-b', '--blank', '--blanks', dest='blank', action='store', default="Ignore",
                        choices=["RemoveAll", "Ignore", "RemoveRepeated", "MakeAllComment"],
                        help="What should be done to the blank lines")
    parser.add_argument('-p','--path', '--paths', dest='paths', action='store', default="Ignore",
                        choices=["RemoveAll", "Ignore", "RemoveRepeated", "MakeAllComment", "MakeAllBlank"],
                        help="What should be done to the paths/patterns listed in the file")
    parser.add_argument("--ver", "--version", action='version', version="1.1.2")#don't forget to update it in the pyproject.toml to!
    parser.add_argument("--git", "--github", action='version', help="Give a link to the github repo page", version="https://github.com/MarkusHammer/gitignore-formatter")
    args = parser.parse_args()
    
    if (args.verbose):
        print("Parsing")
    
    #allows for pathlib to be optional
    try:
        from pathlib import Path
    except ImportError:
        if (args.verbose):
            print("pip package 'pathlib' has not been detected. This is not required but does assist in the parsing of pathnames. Feel free to install this if you prefer to enter path strings with less formating on your end.")
        def Path(inp):
            return inp
    
    #arg correction
    if (args.outFilePath == None):
        args.outFilePath = args.inFilePath

    remember = [] #holds the end result

    args.inFilePath = Path(args.inFilePath.strip("'").strip('"'))
    args.outFilePath = Path(args.outFilePath.strip("'").strip('"'))

    if (args.verbose):
        if (str(args.inFilePath) == str(args.outFilePath)):
            print("modifying file " + str(args.inFilePath))
        else:
            print("opening file " + str(args.inFilePath) + " to transfer into file " + str(args.outFilePath))

    try:
        file = open(args.inFilePath, "rt", encoding="utf8")
    except FileNotFoundError:
        print("The input file path (" + str(args.inFilePath) + ") was not found as a text file with acessable text in it. Check if the path is typed properly, or if you ran this with the proper permissions to access that file.")
        exit(-1)
    if (args.verbose):
        print("Modifying...")
    for line in file:
        line = line.replace("\n","")
        
        isComment = len(line) >= 1 and (line[0] == '#')
        
        if isComment: line = line.lstrip('#') #temporarily remove the comment #
        
        lineStriped = line.strip()
        
        isBlank = (lineStriped == "")
        
        if isBlank or isComment:
            line = lineStriped
        
        if len(line) >= 1 and (line[-1] == "\\"):
            line += " "
        
        allreadyRemembered = (line in remember)
        
        if isComment: line = '#' + line #replace the comment #
        
        rememberTest = True #default to allowing the line through
        if isBlank:
            if args.blank == "RemoveAll":
                rememberTest = False
            elif args.blank == "Ignore":
                rememberTest = True
            elif args.blank == "MakeAllComment":
                rememberTest = True
                line = "#" + line
            else: #args.blank == "RemoveRepeated"
                rememberTest = not (remember[-1] == "")
        elif isComment:
            if args.comments == "RemoveAll":
                rememberTest = False
            elif args.comments == "Ignore":
                rememberTest = True
            elif args.comments == "MakeAllBlank":
                rememberTest = True
                line = ""
            else: #args.comments == "RemoveRepeated"
                rememberTest = not allreadyRemembered
        else: #isNormalPathargs.paths
            if args.paths == "RemoveAll":
                rememberTest = False
            elif args.paths == "Ignore":
                rememberTest = True
            elif args.paths == "MakeAllComment":
                rememberTest = True
                line = "#" + line
            elif args.paths == "MakeAllBlank":
                rememberTest = True
                line = ""
            else: #args.paths == "RemoveRepeated"
                rememberTest = not allreadyRemembered
        
        if rememberTest:
            remember.append(line)
    file.close()

    remember = remember[0:-1]

    try:
        file = open(args.outFilePath, "wt+", encoding="utf8")
    except FileExistsError:
        print("The output file path (" + str(args.outFilePath) + ") is not able to be created or overwritten. Check if you ran this with the proper permissions to access this file, or if there is some other form of write protection to that location.")
        exit(-1)
    if (args.verbose):
        print("Writing...")
    for line in remember[:-1]:
        file.write(line + "\n")
    file.write(remember[-1])
    file.close()

class NotAModuleError(Exception):
    def __str__(self):
        return "gitignoreformatter is not to be used as a module; only as a CLI program. Please remove this import."

if __name__ == "__main__":
    __main__()
else:
    raise NotAModuleError