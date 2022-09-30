import os 

commands={
        "download": "wget -P . https://data.bnl.lu/open-data/digitization/newspapers/export01-newspapers1841-1878.zip",
        "unzip": 'unzip -q export01-newspapers1841-1878.zip',
        "remove zip": "rm export01-newspapers1841-1878.zip",
        "mkdir ADS": "mkdir ADS",
        "move AD files": "find . -name '*ADVERTISEMENT*.xml' -exec cp {} ./ADS/ \;",
        }

def prepare_package():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Downloading dataset pack...\n')
    os.system(commands['download'])
    print('\nDownload complete! Unzipping file and deleting zip...')
    os.system(commands['unzip'])
    os.system(commands['remove zip'])
    print('\nUnzipping complete! Moving all ADVERTISEMENT files to ADS folder...')
    os.system(commands['mkdir ADS'])
    os.system(commands['move AD files'])
    print('\nOperation complete, you are ready to start!')

def main():        
    response = input('Is this your first time running this program? (Y/y, N/n)\n')
    while response not in ("Y", "N", "y", "n"):
        response = input("Is this your first time running this program? (Y/y, N/n)\n")
    if(response == 'Y' or response == 'y'):
        prepare_package()
    elif(response == 'N' or response == 'n'):
        pass

if __name__=="__main__":
    main()
