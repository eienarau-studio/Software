#!/usr/bin/env python2.7

import yaml
import os

STUDIONAME = "Eienarau"
HOME = os.getenv('HOME')
STUDIOPATH = os.path.join(HOME, STUDIONAME)

YAML="""Projects :
Software :
	python2.7 :
	python3.0 :
DCC :"""
#dump YAML for example

#search for studio config

def getConfig():

    #error check config file.

    configFile = os.path.join(STUDIOPATH, "config.yaml")
    if os.path.exists(configFile):
        d_yaml = yaml.load(configFile)
    else:
        d_yaml = yaml.load(YAML)

    return d_yaml

def buildDirectories(dictOfDict):
    for k, v in dictOfDict.items():
        if isinstance(v, dict):
            buildDirectories(v)

        newdir = os.path.join(STUDIOPATH, k)
        if not os.path.exists(newdir):
            os.makedirs(newdir)


if __name__ == "__main__":

    configObj = getConfig()
    buildDirectories(configObj)




