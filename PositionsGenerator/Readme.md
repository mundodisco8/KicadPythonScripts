# Position Generator

This script generates the positions for all the parts in your PCB, and stores them in a nicely formatted Excel Workbook.

This is my first stab at scripting in KiCad with the `pcbnew` library. You will need to have the paths set so Python can see it. In Windows it's a nightmare...

It's pretty much self-explanatory. It loops through all the parts in the PCB file. If the part is marked as SMD, then it adds it to the list. It gets its Reference, Footprint name, Value, X and Y position, Rotation and PCB side. It also prints a couple of notes regarding the origin of coordinates to avoid ambiguity during manufacture.

You can use the `--all` modifier to include all the parts (useful if you also have bits like fiducials or mounting holes, that type of stuff).

## Use

``` bash
python3 PositionsGenerator.py PCB_TO_PROCESS.kicad_pcb
```
