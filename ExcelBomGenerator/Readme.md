# Excel BOM Generator

This script generates a BOM from your current project from the command line, and outputs a nicely formatted Excel workbook.

Although there's nothing wrong with the current plugin system in KiCad, it doesn't do all the stuff that I need, so I put together this script. The main advantage is that is callable from the command line.

## Requirements

* A netlist in XML format. Not a .net netlist, or an eeschema file.

> **BIG NOTE**
>
> I said that it's callable from the command line, but the for that you need to have a netlist in XML format. This file is not normally updated by KiCad, and there's no way (that I know) to get it from the command line, as EEschema won't get python support until KiCad 6. That means that you have to remember to update it by hand to keep it in sync with your schematic or you will generate the BOM of an older version of your schematic. I might add a date check or something...

* The template to your .xlsx file. The script will strip the table of components from an intermediate BOM, and paste it in the template.

* KiBom config file (optional): the script uses KiBom to generate the bom items, and then parses them, so you need to have it set it up according to your project. Please check KiBom's repo for instructions, or just use the one provided as a starting point. If none given, the provided config file will be used.
I use the `KiBom_config.ini` to generate an intermediate .csv BOM. I added some extra columns (like MPN or Digikey links) that I added to my parts library. You might have similar attributes with a different name, so check it out and tweak it accordingly

* Variant (optional): if you want to create a BoM for a variant. See KiBom's instructions on how to use it.

## Usage Example

```
ExcelBomGenerator.py project.xml ExcelTemplate.xlsx
```