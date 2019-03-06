#!/usr/bin/env python2.7

"""
Builds directory structure for studio
"""

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

def buildDirectories(relativePaths):
    """
    Builds directorys from a a list.
    :param relativePaths:
        a list of relative paths

    """


    for relPath in relativePaths:
        newdir = os.path.join(STUDIOPATH, relPath)
        if not os.path.exists(newdir):
            print ("Creating directory: {}".format(newdir))
            os.makedirs(newdir)
        else:
            print ("Dir: {} exists".format(newdir))


def flattenDictKeys(d):
    """

    :param d:
        dictionary preferable of a yaml config file
    :return:
        a flattened relative directory structure of the YAML configs keys.
    """
    results = []

    def visit(subdict, results, parent=None ):
        for k, v in subdict.items():
            newKey = k if parent is None else os.path.join(parent, k)
            if isinstance(v, dict):
                visit(v, results, parent=newKey)
            else:
                results.append(newKey)

    visit(d, results)
    return results



if __name__ == "__main__":

    configDict = getConfig()
    paths = flattenDictKeys(configDict)
    buildDirectories(paths)




