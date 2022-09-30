import os 

response = input('Is this your first time running this program?(Y/N)\n')

while response not in ("Y", "N", "y", "n"):
    response = input("Is this your first time running this program? (Y/N)\n")
if(response == 'Y' or response == 'y'):
    os.system("wget https://data.bnl.lu/open-data/digitization/newspapers/export01-newspapers1841-1878.zip")
    os.system("unzip export01-newspapers1841-1878.zip && rm export01-newspapers1841-1878.zip")
    os.system(" mkdir ADS && find . -name '*ADVERTISEMENT*.xml' -exec cp {} ./ADS/ \;")
elif(response == 'N' or response == 'n'):
    pass
