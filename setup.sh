#!/bin/bash

case "$OSTYPE" in	#Check OS
  darwin*)  clear ;; 	#OSX
  linux*)   clear ;;	#Linux
  msys*)    cls ;;	#Windows
  cygwin*)  cls ;;	#Windows
esac

#Download dataset from source
echo -e $"Downloading dataset pack...\n"
wget -P . https://data.bnl.lu/open-data/digitization/newspapers/export01-newspapers1841-1878.zip

#Extracting zip and removing zip
echo -e $"\nDownload complete! Unzipping file and deleting zip..." 
unzip -q export01-newspapers1841-1878.zip
rm export01-newspapers1841-1878.zip
echo -e $"Unzipping complete! Moving all ADVERTISEMENT files to ADS folder...(can take up to five minutes)"

#Moving all ADVERTISEMENT files to ADS/
mkdir ADS
find . -name '*ADVERTISEMENT*.xml' -exec cp {} ./ADS/ \;

echo -e $"Operation complete, you are ready to start!"
