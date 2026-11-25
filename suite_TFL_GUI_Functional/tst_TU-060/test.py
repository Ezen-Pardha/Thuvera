
# -*- coding: utf-8 -*-

import names
from common import *


def set_left_frequency_to_1hz():
    for i in range(16):
        clickButton(waitForObject(names.centralWidget_pbReduce_QPushButton_2))
        
    sendEvent("QMouseEvent", waitForObject(names.centralWidget_pbReduce_QPushButton_2),
              QEvent.MouseButtonPress, 28, 33, Qt.LeftButton, 1, 0)
    mouseClick(waitForObject(names.centralWidget_lbValue_FlashableLabel_4),
               29, 57, Qt.NoModifier, Qt.LeftButton)

    mouseClick(waitForObject(names.centralWidget_comboBox_ComboBox),
               306, 40, Qt.NoModifier, Qt.LeftButton)

    mouseClick(waitForObjectItem(names.apollo_aivComboBoxPopup_QTreeView,
                                "Kidney Dust (High)"),
               283, 30, Qt.NoModifier, Qt.LeftButton)
    test.log("Left-side frequency was set to 1 Hz the Click option was disabled.")


def set_right_frequency_to_1hz():
    for i in range(13):
        clickButton(waitForObject(names.centralWidget_pbReduce_QPushButton_3))

    sendEvent("QMouseEvent",
              waitForObject(names.centralWidget_pbReduce_QPushButton_3),
              QEvent.MouseButtonPress, 15, 17, Qt.LeftButton, 1, 0)

    mouseClick(waitForObject(names.centralWidget_comboBox_ComboBox_2),
               218, 35, Qt.NoModifier, Qt.LeftButton)

    mouseClick(waitForObjectItem(names.apollo_aivComboBoxPopup_QTreeView,
                                 "Kidney Dust (High)"),
               217, 33, Qt.NoModifier, Qt.LeftButton)

    test.log("Right-side frequency was set to 1 Hz and the Click option was disabled..")

def main():
    enterpin()
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    clickButton(waitForObject(names.sclProfiles_Default_ProfileButton))
    set_left_frequency_to_1hz()
    set_right_frequency_to_1hz()
    
    
    
