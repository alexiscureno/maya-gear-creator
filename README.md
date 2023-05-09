![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Autodesk](https://a11ybadges.com/badge?logo=autodesk)
![Qt](https://img.shields.io/badge/Qt-%23217346.svg?style=for-the-badge&logo=Qt&logoColor=white)
# Gear Creator
### maya-gear-creator
The Gear Creator is a Python script that can be used within the Autodesk Maya 3D animation software to create and modify gears. 
The script has a user interface built with PyQt5 and is designed to be easy to use.

## Getting Started
To use the Gear Creator script, you will need to have Autodesk Maya installed on your computer. 
The script was developed and tested on Maya 2023, but it should also work on earlier versions.

To get started, you can download the Gear Creator script from the repository and place it in a directory of your choice. You will also need to download the gear-ui.ui file, which is the user interface design file for the PyQt5 interface.

## Usage
Once you have the script and UI file in your chosen directory, you can run the script by opening Maya and running the following command in the Python console:

```
import importlib
import gearui
importlib.reload(gearui)
```
Alternatively, you can create a shelf button in Maya and add the above code to the command field of the button.

When the Gear Creator UI appears, you can adjust the number of teeth and length of the gear using the sliders. You can then click the "Create" button to create the gear. The gear will be selected in the Maya viewport, so you can modify it further if you wish.

## Modifying Gears
After creating a gear, you can modify it by adjusting the number of teeth and/or length using the sliders in the UI.

## Resetting the UI
If you want to start over with a new gear, you can click the "Reset" button to reset the UI to its default values.


# Contributing
This project is open source and contributions are welcome. To contribute, please fork the repository, make your changes, and submit a pull request.
