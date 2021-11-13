## MoveMemberFiles
Move all files of members of a specified linux group to a specified archive location.

## How to
To run the script either build the .deb package by downloading the repository and executing ```dpkg -b moveMemberFiles-1.0``` in the parent folder of the repository or simply run the python script in the repositories's folder ```usr/bin``` by typing ```python moveMemberFiles.py```.\
The script will require the name of a group and an archive location as inputs.\
Optionally you can also limit the search space of the script by providing a path to a specific location that holds the users' files you're interested in.\
If you don't provide a specific location the script will start searching and moving from root.\
Example: ```python moveMemberFiles.py "myGroup" "/home/user/archive/" "/"```\
The script will also log all files that were moved.\
This log file is created in the same folder the script is located.
