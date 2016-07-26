#!python

import os

from shutil import copyfile

remote = "ec2-52-41-73-252.us-west-2.compute.amazonaws.com"

source = "SeattleIntroToPython.ipynb"

with open("signups.txt") as namefile:
    for name in namefile:
        name = name.strip()
        target = name + ".ipynb"
        copyfile(source, target)
        os.system("scp -i ~/.ssh/awskey.pem {0} ubuntu@{1}:~/meetup/".format(target, remote))

os.system("scp -i ~/.ssh/awskey.pem ls data/Hotel_Occupancy_Tax_Receipts__Monthly.csv ubuntu@{0}:~/meetup/data/".format(remote))

