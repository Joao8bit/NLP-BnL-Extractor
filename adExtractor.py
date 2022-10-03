import subprocess

#Checks and runs the setup.sh file for the first time
def initial_setup():
    response = input('Is this your first time running this program? (Y/y, N/n)\n').lower()
    while response not in ("y", "n"):
        response = input("Is this your first time running this program? (Y/y, N/n) ").lower()
    if(response == 'y'):
        subprocess.run(['bash', 'setup.sh'])
    elif(response == 'n'):
        pass
    
def main():
    initial_setup()

if __name__=="__main__":
    main()
