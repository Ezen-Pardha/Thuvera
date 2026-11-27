# -*- coding: utf-8 -*-

import names
from common import *

def main():
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    clickButton(waitForObject(names.frToolbar_tbAddProfile_QToolButton))
    type(waitForObject(names.editFrame_edEditText_QLineEdit), "Test1")
    clickButton(waitForObject(names.keyboardFrame_Enter_KeyButtonEnter))
    clickButton(waitForObject(names.sclProfiles_Test1_ProfileButton, 57246))
    test.passes("Treatment screen is verified")
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 14, 26, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.apollo_aivComboBoxPopup_QTreeView, "Tissue Vaporize (Pulsed)"), 284, 33, Qt.NoModifier, Qt.LeftButton)
    test.passes("Pulsemode preset is selected from drop down")
    
    """Verify Pulsed indicator is active"""

    try:
        button = waitForObjectExists(names.centralWidget_btMiddlePulse_ButtonWithClickSound, 2000)
    
        if button.enabled:
            test.passes("Pulsed indicator is active")
        else:
            test.fail("Pulsed indicator is not active")
    
    except LookupError:
        test.fail("Pulsed indicator is not found on the Treatment Screen")
    
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel_2), 23, 15, Qt.NoModifier, Qt.LeftButton) 
    mouseClick(waitForObjectItem(names.apollo_aivComboBoxPopup_QTreeView, "Tissue Vaporize (Pulsed)"), 302, 29, Qt.NoModifier, Qt.LeftButton)
    """Verify Right Pedal Pulsed indicator is active"""

    try:
        button = waitForObjectExists(names.centralWidget_btMiddlePulse_ButtonWithClickSound_2, 2000)
    
        if button.enabled:
            test.passes("Right Pedal Pulsed indicator is active")
        else:
            test.fail("Right Pedal Pulsed indicator is not active")
    
    except LookupError:
        test.fail("Right Pedal Pulsed indicator is not found on the Treatment Screen")
    
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.apollo_YES_QPushButton))
    clickButton(waitForObject(names.frToolbar_tbDeleteProfile_QToolButton))
    clickButton(waitForObject(names.sclProfiles_Test1_ProfileButton))
    snooze(5)
    clickButton(waitForObject(names.question_OK_QPushButton))
    
     
    
   
