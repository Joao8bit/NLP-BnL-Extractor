#!/usr/bin/env python3

import os
import subprocess
from sys import platform
from project_tests.big_test import description_extractor

#Checks and runs the setup.sh file for the first time if the folder ./ADS/ does not yet exist
def initial_setup():
    isExist = os.path.exists('./ADS/')
    if(isExist == False):
        if(platform == "linux" or platform == "linux2" or platform == "darwin"):
            subprocess.run(['bash', 'setup.sh'])
        #if(platform == "win32" or platform == "cygwin"):
        #    subprocess.run(['setup.bat'])
    else:
        pass

def main():
    initial_setup()
    description_extractor()

if __name__=="__main__":
    main()
