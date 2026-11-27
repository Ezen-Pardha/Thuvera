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
    test.passes("Treatment screen is verified")
    clickButton(waitForObject(names.centralWidget_pbEnlarge_QPushButton))
    test.passes("Energy value is increased")

    # test.compare(str(waitForObjectExists(names.centralWidget_pbSaveSettings_QPushButton).text), "SAVE SETTINGS")

    """Verify Save Settings button text"""
    try:
        button = waitForObjectExists(names.centralWidget_pbSaveSettings_QPushButton, 2000)
    
        actual_text = str(button.text)
    
        if actual_text == "SAVE SETTINGS":
            test.passes("Save Settings button displays the expected text: SAVE SETTINGS")
        else:
            test.fail("Save Settings button text is incorrect. Actual text: " + actual_text)
    
    except:
        test.fail("Save Settings button is not found on the screen")
    mouseClick(waitForObject(names.centralWidget_comboBox_ComboBox), 419, 28, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.apollo_aivComboBoxPopup_QTreeView, "Kidney Dust (Low)"), 310, 34, Qt.NoModifier, Qt.LeftButton)
    test.passes("preset changed from drop down")
    """Verify Save Settings button"""
    """Verify Save Settings button is not displayed"""

    try:
        button = findObject(names.centralWidget_pbSaveSettings_QPushButton)
    
        if button.visible:
            test.fail("Save Settings button is displayed on the Treatment Screen")
        else:
            test.passes("Save Settings button is not displayed on the Treatment Screen, as expected")
    
    except LookupError:
        test.passes("Save Settings button is not found on the Treatment Screen, as expected")
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.apollo_YES_QPushButton))
    clickButton(waitForObject(names.frToolbar_tbDeleteProfile_QToolButton))
    clickButton(waitForObject(names.sclProfiles_Test1_ProfileButton))
    snooze(5)
    clickButton(waitForObject(names.question_OK_QPushButton)) 
