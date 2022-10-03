import os 
import subprocess

def main():        
    response = input('Is this your first time running this program? (Y/y, N/n)\n').lower()
    while response not in ("y", "n"):
        response = input("Is this your first time running this program? (Y/y, N/n)\n")
    if(response == 'Y' or response == 'y'):
        subprocess.run(['bash', 'startHere.sh'])
    elif(response == 'N' or response == 'n'):
        pass

if __name__=="__main__":
    main()
