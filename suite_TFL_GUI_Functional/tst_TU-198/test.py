# -*- coding: utf-8 -*-

import names
from common import *

def main():
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    clickButton(waitForObject(names.frToolbar_tbAddProfile_QToolButton))
    type(waitForObject(names.editFrame_edEditText_QLineEdit), "Test1")
    clickButton(waitForObject(names.keyboardFrame_Enter_KeyButtonEnter))
    clickButton(waitForObject(names.sclProfiles_Test1_ProfileButton))
    mouseClick(waitForObject(names.centralWidget_comboBox_ComboBox), 460, 42, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.apollo_aivComboBoxPopup_QTreeView, "Tissue Vaporize (CW)"), 279, 18, Qt.NoModifier, Qt.LeftButton)
    """Verify CW Mode button is active"""
    try:
        button = waitForObjectExists(names.centralWidget_pbCwMode_QToolButton, 2000)
        if button.enabled:
            test.passes("left Pedal CW Mode button is active")
        else:
            test.fail("CW Mode button is not active")
    
    except LookupError:
        test.fail("CW Mode button is not found on the Treatment Screen")

    mouseClick(waitForObject(names.centralWidget_comboBox_ComboBox_2), 393, 26, Qt.NoModifier, Qt.LeftButton)     
    mouseClick(waitForObjectItem(names.apollo_aivComboBoxPopup_QTreeView, "Tissue Vaporize (CW)"), 280, 47, Qt.NoModifier, Qt.LeftButton)
    """Verify Right Pedal CW Mode button is active"""
    try:
        button = waitForObjectExists(names.centralWidget_pbCwMode_QToolButton_2, 2000)
    
        if button.enabled:
            test.passes("Right Pedal CW Mode button is active")
        else:
            test.fail("Right Pedal CW Mode button is not active")
    
    except LookupError:
        test.fail("Right Pedal CW Mode button is not found on the Treatment Screen")
        
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.apollo_YES_QPushButton))
    clickButton(waitForObject(names.frToolbar_tbDeleteProfile_QToolButton))
    clickButton(waitForObject(names.sclProfiles_Test1_ProfileButton))
    snooze(5)
    clickButton(waitForObject(names.question_OK_QPushButton))
