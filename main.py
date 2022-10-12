#!/usr/bin/python3
from setup import *
initial_setup()

import os
from src.xml.xml_manipulation import *
import src.csv.csv as csv

def main():    
    root_dir = './ADS/'
    files = os.listdir(root_dir)
    csv.write_to_csv(root_dir, files[:5])

if __name__=="__main__":
    main()
