# Kicad_On_Ubuntu

This Dockerfile sets an Ubuntu 19.10 image and installs Kicad 5.1.4 and Kiplot on it. It can be used on CI in order to get the manufacture files.

Right now it only generates gerbers, more functionality can be added easily. Not bad for a first stab at it. Let's see where it takes us!

## Versions / Tags

### 19_10_18:

Added all the external modules (Kiplot and KiBom) and dependencies to the image. I linked to my repos as they have issues that I don't know if they will be pulled to the main ones. I'll link to them when they are added.

### 19_10_09:

First version of the thing on Ubuntu after the Debian Fiasco of 2019. `pcbnew` works with python 3, not 2, so I assume that Ubuntu's version comes with python 3 support enabled. I installed everything without the recommended additional packages and it still works and knocked 600MB from the image size.

Cloned the Kiplot project to my personal repo to do a pull request to enable more than 2 layers (go Hacktoberfest!!), as it seems that the guy managing Kiplot is not interested in mantaining it much.
