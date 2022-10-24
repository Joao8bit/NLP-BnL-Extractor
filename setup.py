import os
import subprocess
from sys import platform

def initial_setup():
    """
    We check if the ADS/ folder exists, as it is created with this precise script.
    If it does not yet exist, we run setup.sh.
    """
    isExist = os.path.exists('./ADS/')
    if(isExist == False):
        if(platform == "linux" or platform == "linux2" or platform == "darwin"):
            subprocess.run(['bash', 'setup.sh'])
        #if(platform == "win32" or platform == "cygwin"):
        #    subprocess.run(['setup.bat'])
    else:
        pass

initial_setup()
