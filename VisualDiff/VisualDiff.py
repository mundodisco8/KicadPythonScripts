################################################################################
# First stab at trying to get a visual diff for the gerbers
#
# This script gets the gerbers in two subfolders, "After" and "Before", and
# creates a GerbV project that displays them in a way that is easy to see the
# changes between versions.
#
# Caveats: many!
# - You need to have GerbV installed, and indicate the path manually.
# - Both Before and After gerber sets need a kicad gerber project file (for now,
#   at least).
# - If Before and After have different number of gerbers, the thing just doesn't
#   know what to do.
#
# TODO:
# - Remove the dependency on the gerber project file, and search for gerbers in
#   the directories.
# - If a gerber is only present in one of the sets, consider it a new gerber or
#   a deleted gerber, and show it with a different colour.
################################################################################

import os
from os import path
import json
import subprocess
from GerberLayerColours import A_layerPropertiesDict, B_layerPropertiesDict
from GerberLayerColours import alphaBefore, alphaAfter
from GerberLayerColours import gerberSet, returnLayerProperties

### Some global variables

pathToGerbv = "C:/Users/Joel/Desktop/Gerb/App/gerbv64/bin/gerbv.exe"
projectFileName = "Gerbv_Project.gvp"

###
# This function does all the layer info gathering for a certain set (BEFORE or
# AFTER) and returns something with it
def gatherLayerInformation(set):

    ### Read the json from Kicad with the gerbers info
    # Search for the project file
    gerberJobFile = ""
    currentDir = ""

    # path.isfile only returns true if cwd is the same as the files are, so we need
    # to add the folder name to the command in path.isfile
    if (set == gerberSet.AFTER):
        currentDir = "After"
        layerPropertiesDict = A_layerPropertiesDict
    elif (set == gerberSet.BEFORE):
        currentDir = "Before"
        layerPropertiesDict = B_layerPropertiesDict

    files = [currentDir + "/" + f for f in os.listdir("After") if path.isfile(currentDir + "/"+ f)]
    for file in files:
        # print(file)
        #file = currentDir + "/" + file
        if file.endswith("-job.gbrjob"):
            gerberJobFile = file
            print("\nFound project file! %s\n" % gerberJobFile)
            break
    else:
        print("\n**** No project file found! ****\n")
        print("\n**** Tweak this so we do a manual search of files! ****\n")
        input("\nPress Enter to close this window...")
        exit()

    # Load the present files / layers from the project file
    with open(gerberJobFile, 'r') as f:
        layers_dict = json.load(f)

    stackUp = [None] * len(layerPropertiesDict) # will contain the layer file and colour, and it will be in the right order

    ### Get the present gerbers in this project from the project file, find their
    # colour and what's their relative order in the stackup
    print("Searching for layers in the project file...")
    for layer in layers_dict["FilesAttributes"]:
        # List of files in project
        filename = currentDir + "/" + layer["Path"]
        print("Found layer %s" % (layer["FileFunction"]))
        (layerColour, layerVisibility, layerOrder) = returnLayerProperties(layer["FileFunction"], set)
        # print("%s: %s, %s" % (filename, layerColour, layerOrder))
        stackUp[layerOrder] = (filename, layerVisibility, layerColour)

    ### Now, some files are not in the gerber job file, and I really don't know why
    # They are not manufacturing files, so I guess that's the reason. Let's check
    # for them manually. Surprisingly, the drill files are not in the project file
    # either
    print("\nSearching for gerber files in the directory...")
    for file in files:
        # Eco2 Layer
        key = None
        # print(file)
        if file.endswith("Eco2_User.gbr"):
            print("Found layer Eco2")
            key = returnLayerProperties("Eco2.User", set)
        elif file.endswith("Eco1_User.gbr"):
            print("Found layer Eco1")
            key = returnLayerProperties("Eco1.User", set)
        elif file.endswith("Dwgs_User.gbr"):
            print("Found layer Drawings")
            key = returnLayerProperties("Drawings", set)
        elif file.endswith("Cmts_User.gbr"):
            print("Found layer Comments")
            key = returnLayerProperties("Comments", set)
        elif file.endswith("F_CrtYd.gbr"):
            print("Found layer Courtyard top")
            key = returnLayerProperties("Courtyard,Top", set)
        elif file.endswith("B_CrtYd.gbr"):
            print("Found layer Courtyard Bottom")
            key = returnLayerProperties("Courtyard,Bot", set)
        elif file.endswith("-PTH.drl"):
            print("Found layer PTH drill")
            key = returnLayerProperties("Drills,Plated", set)
        elif file.endswith("-NPTH.drl"):
            print("Found layer NPTH drill")
            key = returnLayerProperties("Drills,NonPlated", set)
        elif file.endswith("-PTH-drl_map.gbr"):
            print("Found layer PTH drill map")
            key = returnLayerProperties("Drills,PlatedMap", set)
        elif file.endswith("-NPTH-drl_map.gbr"):
            print("Found layer NPTH drill map")
            key = returnLayerProperties("Drills,NonPlatedMap", set)
        if key != None:
            # just for an extra readibility
            (layerColour, layerVisibility, layerOrder) = key
            stackUp[layerOrder] = (file, layerVisibility, layerColour)

    # Some of the layers will be missing, delete the layers that don't have a file
    stackUp = [layer for layer in stackUp if (layer != None)]
    return stackUp

################################################################################


# Time to build the layer properties for the project file, it has this format
# (define-layer! (LAYERNUMBER) (cons "[FILENAME])
#     (cons 'visible #(t or f))
#     (cons 'color #( R G B ))
#     (cons 'alpha #( ALPHA))
# )
stackUpAfter = gatherLayerInformation(gerberSet.AFTER)
stackUpBefore = gatherLayerInformation(gerberSet.BEFORE)
# Layer properties will contain each layer's properties
# This is the text that will go into the file
if (len(stackUpAfter) != len(stackUpBefore)):
    print("Different number of gerbers in Before and After?")
    input("Fix this so it's not an issue!")
    input("\nPress Enter to close this window...")
    exit()

layerProperties = [None] * len(stackUpAfter)

# These are the strings we have to modify to build the project file
layerNoAndFilenameString = """(define-layer! %d (cons 'filename \"%s\")"""
propertiesString = """    (cons 'visible #%s)
    (cons 'color #(%s))
    (cons 'alpha #(%d))
)\n"""

# for i, (filename, layerVisibility, layerColour) in enumerate(stackUpAfter):
    # layerProperties[i] = layerString % (i, filename, layerVisibility, layerColour)

numberOfLayers = max(len(stackUpAfter), len(stackUpBefore))

# Write the file!
f = open(projectFileName, "w+")
f.write("(gerbv-file-version! \"2.0A\")\n")
for i in range(numberOfLayers):
    f.write(layerNoAndFilenameString % ((i * 2), stackUpAfter[i][0]))
    f.write(propertiesString % (stackUpAfter[i][1], stackUpAfter[i][2], alphaAfter))
    f.write(layerNoAndFilenameString % ((i * 2 + 1), stackUpBefore[i][0]))
    f.write(propertiesString % (stackUpBefore[i][1], stackUpBefore[i][2], alphaBefore))
# and close
f.write("""(define-layer! -1 (cons 'filename "%s")
    (cons 'color #(5200 5200 5200))
)
(set-render-type! 2)""" % (os.getcwd()+"/"+projectFileName))
f.close()

### Search for gerbv and open it if it finds it
exists = os.path.isfile(pathToGerbv)
if (exists):
    print(projectFileName)
    # Opens Gerbv in mm and with the right project file
    # Open Process, don't wait for it to end and ignore output
    process = subprocess.Popen([pathToGerbv, "--units=mm", "-p" + projectFileName], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).pid
else:
    print("Doh!")

if path.isdir("__pycache__"):
    for file in os.listdir("__pycache__"):
        os.remove("__pycache__/" + file)
    os.rmdir("__pycache__")

print("DONE")
input("\nPress Enter to close this window...")