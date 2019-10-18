import enum
import collections # for the OrderedDict

################################################################################
# LIST OF COLOURS FOR THE DIFFERENT LAYERS

# I'll leave it as a list, just in case we want to tweak them

# Colours BEFORE
B_DrillsPlated =    "0     65535 65535"
B_DrillsNonPlated = "0     65535 65535"
B_CopperTop =       "0     65535 65535"
B_CopperBottom =    "0     65535 65535"
B_CopperIn1 =       "0     65535 65535"
B_CopperIn2 =       "0     65535 65535"
B_SolderTop =       "0     65535 65535"
B_SolderBottom =    "0     65535 65535"
B_SilkTop =         "0     65535 65535"
B_SilkBottom =      "0     65535 65535"
B_MaskTop =         "0     65535 65535"
B_MaskBottom =      "0     65535 65535"
B_Drawings =        "0     65535 65535"
B_Comments =        "0     65535 65535"
B_Profile =         "0     65535 65535"
B_Eco =             "0     65535 65535"
B_Undefined =       "0     65535 65535"

# Colours AFTER
A_DrillsPlated =    "65535 0     0    "
A_DrillsNonPlated = "65535 0     0    "
A_CopperTop =       "65535 0     0    "
A_CopperBottom =    "65535 0     0    "
A_CopperIn1 =       "65535 0     0    "
A_CopperIn2 =       "65535 0     0    "
A_SolderTop =       "65535 0     0    "
A_SolderBottom =    "65535 0     0    "
A_SilkTop =         "65535 0     0    "
A_SilkBottom =      "65535 0     0    "
A_MaskTop =         "65535 0     0    "
A_MaskBottom =      "65535 0     0    "
A_Drawings =        "65535 0     0    "
A_Comments =        "65535 0     0    "
A_Profile =         "65535 0     0    "
A_Eco =             "65535 0     0    "
A_Undefined =       "65535 0     0    "

# The transparency of the BEFORE layer, which sits below the AFTER layer, can be
# set to fully opaque. The AFTER layer is set to half transparency
alphaAfter = 32767
alphaBefore = 65535

################################################################################
# Dictionary with the layer colours
#
# The Key of each dictionary is the string used in the project file made by
# KiCad to identify each layer.
#
# The value of each key it's a tuple with the layer colour, a string to mark
# if the layer will be visible or not by default, and the layer order
# "layerDenominator": [layerColour, isVisible, layerOrder]

# It will contain a third element on the list, with the layer order, but
# we add it programatically because it's a forking pain in the ass to do it
# every time we change the order

# A_ for After, gerbers that have the current set of changes
A_layerPropertiesDict = collections.OrderedDict()
A_layerPropertiesDict = {
    #drills
    "Drills,Plated":        [A_DrillsPlated, "t"],
    "Drills,PlatedMap":     [A_DrillsPlated, "t"],
    "Drills,NonPlated":     [A_DrillsNonPlated, "t"],
    "Drills,NonPlatedMap":  [A_DrillsNonPlated, "t"],
    "Profile":              [A_Profile, "t"], # Edge_Cuts
    "Drawings":             [A_Drawings, "t"], # Dwgs.User
    "Comments":             [A_Comments, "t"], # Cmts.User
    "Eco1.User":            [A_Eco, "f"],
    "Eco2.User":            [A_Eco, "f"],
    "Margin":               [A_Comments, "t"],
    "Glue,Top":             [A_Undefined, "f"], # Adhes
    "Courtyard,Top":        [A_Comments, "f"],
    "AssemblyDrawing,Top":  [A_Undefined, "f"],# F_Fab
    "Legend,Top":           [A_SilkTop, "t"],
    "SolderPaste,Top":      [A_SolderTop, "t"],
    "SolderMask,Top":       [A_MaskTop, "t"],
    "Copper,L1,Top":        [A_CopperTop, "t"],
    "Copper,L2,Inr":        [A_CopperIn1, "t"],
    "Copper,L3,Inr":        [A_CopperIn2, "t"],
    "Glue,Bot":             [A_Undefined, "f"],
    "Courtyard,Bot":        [A_Comments, "f"],
    "AssemblyDrawing,Bot":  [A_Undefined, "t"],
    "Legend,Bot":           [A_SilkBottom, "t"],
    "SolderPaste,Bot":      [A_SolderBottom, "t"],
    "SolderMask,Bot":       [A_MaskBottom, "t"],
    "Copper,L2,Bot":        [A_CopperBottom, "t"],
    "Copper,L4,Bot":        [A_CopperBottom, "t"],
}

# B_ for Before, gerbers with the previous state of things
B_layerPropertiesDict = collections.OrderedDict()
B_layerPropertiesDict = {
    #drills
    "Drills,Plated":        [B_DrillsPlated, "t"],
    "Drills,PlatedMap":     [B_DrillsPlated, "t"],
    "Drills,NonPlated":     [B_DrillsNonPlated, "t"],
    "Drills,NonPlatedMap":  [B_DrillsNonPlated, "t"],
    "Profile":              [B_Profile, "t"], # Edge_Cuts
    "Drawings":             [B_Drawings, "t"], # Dwgs.User
    "Comments":             [B_Comments, "t"], # Cmts.User
    "Eco1.User":            [B_Eco, "f"],
    "Eco2.User":            [B_Eco, "f"],
    "Margin":               [B_Comments, "t"],
    "Glue,Top":             [B_Undefined, "f"], # Adhes
    "Courtyard,Top":        [B_Comments, "f"],
    "AssemblyDrawing,Top":  [B_Undefined, "f"],# F_Fab
    "Legend,Top":           [B_SilkTop, "t"],
    "SolderPaste,Top":      [B_SolderTop, "t"],
    "SolderMask,Top":       [B_MaskTop, "t"],
    "Copper,L1,Top":        [B_CopperTop, "t"],
    "Copper,L2,Inr":        [B_CopperIn1, "t"],
    "Copper,L3,Inr":        [B_CopperIn2, "t"],
    "Glue,Bot":             [B_Undefined, "f"],
    "Courtyard,Bot":        [B_Comments, "f"],
    "AssemblyDrawing,Bot":  [B_Undefined, "t"],
    "Legend,Bot":           [B_SilkBottom, "t"],
    "SolderPaste,Bot":      [B_SolderBottom, "t"],
    "SolderMask,Bot":       [B_MaskBottom, "t"],
    "Copper,L2,Bot":        [B_CopperBottom, "t"],
    "Copper,L4,Bot":        [B_CopperBottom, "t"],
}

# We'll use this enum to choose between the two sets
class gerberSet(enum.Enum):
    BEFORE = 1
    AFTER = 2

# Initially, I thought it was going to do more stuff :D
def returnLayerProperties(fileFunction, colourSet):
    if (colourSet == gerberSet.BEFORE):
        return B_layerPropertiesDict[fileFunction]
    elif (colourSet == gerberSet.AFTER):
        return A_layerPropertiesDict[fileFunction]

# Initialises the layer dictionaries, by appending a third element to each
# key with it's relative position.
# I do it this because ordered dicts don't know their keys' order
def initialiseDictionary():
    for i, key in enumerate(A_layerPropertiesDict):
        A_layerPropertiesDict[key] = A_layerPropertiesDict[key]+[i]
        # print(A_layerPropertiesDict[key])
    for i, key in enumerate(B_layerPropertiesDict):
        B_layerPropertiesDict[key] = B_layerPropertiesDict[key]+[i]
        # print(B_layerPropertiesDict[key])

### Run this on import
initialiseDictionary()
print("Layer order appended to dicts")