from PyQt5.QtWidgets import QDialog, QPushButton, QSlider, QLabel
from PyQt5 import uic
from gearClassCreator import Gear
from maya import cmds


class GearCreator(QDialog):

    def __init__(self):
        super().__init__()

        self.gear = None
        uic.loadUi(r'C:\Users\user\Documents\maya\2023\scripts\gear-ui.ui', self)

        self.label_teeth = self.findChild(QLabel, 'num_teeth')
        self.label_length = self.findChild(QLabel, 'num_length')

        self.create_btn = self.findChild(QPushButton, 'create_button')
        self.create_btn.clicked.connect(self.create_gear)

        self.close_btn = self.findChild(QPushButton, 'close_button')
        self.close_btn.clicked.connect(self.close)

        self.reset_btn = self.findChild(QPushButton, 'reset_button')
        self.reset_btn.clicked.connect(self.reset)

        self.teeth_sld = self.findChild(QSlider, 'teeth_slider')
        self.teeth_sld.valueChanged.connect(self.set_teeth_value)

        self.length_sld = self.findChild(QSlider, 'length_slider')
        self.length_sld.valueChanged.connect(self.set_length_value)

    def create_gear(self):
        self.gear = Gear()
        self.gear.createGear(teeth=self.teeth_sld.value(), length=self.length_sld.value() / 10.0)
        cmds.select(self.gear.transform)

    def set_teeth_value(self, value):
        self.label_teeth.setText(str(value))
        if self.gear is not None:
            self.gear.changeTeeth(teeth=self.teeth_sld.value(), length=self.length_sld.value() / 10.0)

    def set_length_value(self, value):
        self.label_length.setText(str(value))
        if self.gear is not None:
            self.gear.changeTeeth(teeth=self.teeth_sld.value(), length=self.length_sld.value() / 10.0)

    def reset(self):
        self.gear = None
        self.teeth_sld.setValue(4)
        self.length_sld.setValue(3)
        self.set_teeth_value(4)
        self.set_length_value(3)


window = GearCreator()
window.show()
