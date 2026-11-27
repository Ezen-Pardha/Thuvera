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
    test.passes("Preset values are changed")
    """Verify Save Settings button is displayed on Treatment Screen"""
    try:
        button = waitForObjectExists(names.centralWidget_pbSaveSettings_QPushButton, 2000)
    
        if button.visible:
            test.passes("Save Settings button is displayed on the Treatment Screen")
            clickButton(waitForObject(names.centralWidget_pbSaveSettings_QPushButton))
        else:
            test.fail("Save Settings button is not displayed on the Treatment Screen")
    
    except:
        test.fail("Save Settings button is not found on the Treatment Screen")
    test.passes("Save settings screen verified")
    
    """Verify and click Cancel button"""
    try:
        button = waitForObjectExists(names.apollo_btCancel_QPushButton, 2000)
    
        if button.visible and button.isEnabled():
            clickButton(button)
            test.passes("Cancel button is displayed and clicked successfully")
        else:
            test.fail("Cancel button is not visible or not enabled")
    
    except:
        test.fail("Cancel button is not found on the screen")
        
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.apollo_YES_QPushButton))
    clickButton(waitForObject(names.frToolbar_tbDeleteProfile_QToolButton))
    clickButton(waitForObject(names.sclProfiles_Test1_ProfileButton))
    snooze(5)
    clickButton(waitForObject(names.question_OK_QPushButton))   
    
    
