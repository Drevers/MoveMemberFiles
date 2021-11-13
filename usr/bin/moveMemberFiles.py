#!/usr/bin/python3

import os
import shutil
import grp
import pwd
import logging
import time
import sys



#searches for files of users of the specified group in the given directory and its children
def findAndMoveFiles(searchPath:str ='/'):
    logging.warning("Start searching and moving process")
    count = 0
    for path, dirs, files in os.walk(searchPath):
        for file in files:
            location = os.path.join(path,file)
            try:
                if os.stat(location).st_uid in membersOfGroup: #check if the file is owned by a user of the group
                    shutil.move(location,ARCHIVE)
                    logging.info("Moved %s from %s to %s." %(file,path,ARCHIVE))
                    count += 1
            except:
                pass
    logging.warning("Moved %d files."%(count))            
    logging.warning("Finished searching and moving process.")

if (len(sys.argv) > 2):
    try:
        GRPNAME = sys.argv[1]
        ARCHIVE = sys.argv[2] #destiny of the files
        groupID = grp.getgrnam(GRPNAME)[2] #get id for the corresponding group
        groupInfos = grp.getgrgid(groupID) #get infos about the group
        membersOfGroup = set() #save ids of group members
        for user in groupInfos[3]: #get all members of the corresponding group
            membersOfGroup.add(pwd.getpwnam(user).pw_uid)
    except:
        print("The group name you provided doesn't exist! Please check your input.") 
        
    try:
        if (os.path.exists(sys.argv[2])): #check if the archive folder exists
            ARCHIVE = sys.argv[2] #destiny of the files
        else:
            raise Exception()
        logging.basicConfig(filename="log_group_%s_%s.log"%(groupID,time.strftime("%Y:%m:%d-%H:%M:%S")),level=logging.DEBUG,format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
        if len(sys.argv) > 3:
            findAndMoveFiles(sys.argv[3])
        else:
            findAndMoveFiles()
        print("Task completed") 
    except:
        print("The archive location doesn't exist! Please provide a valid location.")   
else:
    print("Please provide the name of the group and the archive location! Optionally you can also limit the search space by providing a path to a specific folder that contains the members' files.")

















