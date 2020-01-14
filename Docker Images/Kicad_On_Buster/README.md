# Kicad_On_Buster

This Dockerfile sets a Debian Buster image and installs Kicad 5.0 and Kiplot on it. It can be used on CI in order to get the manufacture files.

Right now it only generates gerbers, more functionality can be added easily. Not bad for a first stab at it. Let's see where it takes us!

## Versions / Tags

### 19_10_07:

First version of the thing. Managed to get Buster with Kicad and python 2 accepting pcbnew. Kiplot works and generates the requested files.

I realised that the Kicad version availabe in Debian is 5.0, and you have to do some stuff in order to update it, and after I did it I couldn't get python to import pcbnew, so I decided to move on to Ubuntu. I don't know if this image will be updated or if work will carry on on the other image.