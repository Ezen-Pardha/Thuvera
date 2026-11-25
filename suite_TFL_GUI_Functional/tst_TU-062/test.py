import names
from common import *

def set_left_pedal_energy():
    for i in range(6):
        clickButton(waitForObject(names.centralWidget_pbReduce_QPushButton))

    sendEvent("QMouseEvent",
              waitForObject(names.centralWidget_pbReduce_QPushButton),
              QEvent.MouseButtonPress, 42, 36, Qt.LeftButton, 1, 0)

    mouseClick(waitForObject(names.centralWidget_lbValue_FlashableLabel_3),
               95, 47, Qt.NoModifier, Qt.LeftButton)

    mouseClick(waitForObject(names.centralWidget_comboBox_ComboBox),
               297, 35, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.apollo_aivComboBoxPopup_QTreeView,
                                 "Kidney Dust (High)"),
               254, 36, Qt.NoModifier, Qt.LeftButton)

    test.log("Left pedal energy value was set to 0.025 and the Click option was disabled.")
    
def set_right_pedal_energy():
    for i in range(6):
        clickButton(waitForObject(names.centralWidget_pbReduce_QPushButton_4))
    sendEvent("QMouseEvent",
              waitForObject(names.centralWidget_pbReduce_QPushButton_4),
              QEvent.MouseButtonPress, 34, 44, Qt.LeftButton, 1, 0)

    mouseClick(waitForObject(names.centralWidget_comboBox_ComboBox_2),
               167, 27, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.apollo_aivComboBoxPopup_QTreeView,
                                 "Kidney Dust (High)"),
               174, 27, Qt.NoModifier, Qt.LeftButton)
    test.log("Right pedal energy value was set to 0.025 and the Click option was disabled.")
    
def main():
    enterpin()
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    clickButton(waitForObject(names.sclProfiles_Default_ProfileButton))
    set_left_pedal_energy()
    set_right_pedal_energy()